"""This module contains:
- the Weclapp class, which provides methods to interact
with the Weclapp API. It includes methods for sending GET, PUT, POST, and DELETE
requests, as well as an iterator for paginated results.
- the WeclappError class, which is a custom exception class for handling errors
from the Weclapp API.
"""

import json
import os
import random
import time
import logging
from importlib.metadata import PackageNotFoundError, version as _pkg_version
from typing import Optional, Union, Generator
import requests
from . import config

try:
    PYWECLAPP_VERSION = _pkg_version("pyweclapp")
except PackageNotFoundError:
    PYWECLAPP_VERSION = "0.0.0+unknown"


class WeclappError(Exception):
    """Custom exception class for Weclapp API errors."""

    def __init__(
        self, error_response: requests.Response, api_version: str = config.API_VERSION
    ):
        self.response = error_response
        self.status_code = error_response.status_code
        self.url = str(self.response.url).split(f"/api/{api_version}", maxsplit=1)[-1]
        self.wait_ms = _parse_wait_ms(error_response.headers.get("X-Weclapp-Wait-Ms"))
        self.wait_reason = error_response.headers.get("X-Weclapp-Wait-Reason")
        self.is_json = False
        try:
            error_response = self.response.json()
            self.detail = error_response.get("detail", "")
            self.error = error_response.get("error", "")
            self.status = error_response.get("status", 400)
            self.title = error_response.get("title", "")
            self.error_type = error_response.get("type", "")
            self.validation_errors = error_response.get("validationErrors", [])
            self.messages = error_response.get("messages", [])
            self.is_json = True

        except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
            self.detail = error_response.text

        super().__init__(self.detail)

    @property
    def is_optimistic_lock(self) -> bool:
        """Checks if the error is an optimistic lock error."""
        if self.detail == config.OPTIMISTIC_LOCK_IDENTIFIER:
            logging.error("Optimistic lock error found.")
            return True
        return False

    @property
    def is_rate_limited(self) -> bool:
        """Checks if the error was caused by weclapp's load management (HTTP 429)."""
        return self.status_code == 429

    def __str__(self) -> str:
        """Returns a string representation of the WeclappError."""
        if not self.is_json:
            error_message = (
                f"{self.response.status_code}: {self.detail} when sending "
                f"request to {self.url}"
            )
        else:
            error_message = (
                f"Error {self.title} with code {self.response.status_code}: "
                f"{self.error}, when sending request to {self.url}."
            )
            for message in self.messages:
                if isinstance(message, dict):
                    error_message += (
                        f"\n\t\t{message.get('severity')}={message.get('message')};"
                    )
            for message in self.validation_errors:
                error_message += f"\n\t\t{message};"

        if self.wait_ms is not None:
            reason = self.wait_reason or "unspecified"
            error_message += (
                f"\n\t\tWaited {self.wait_ms} ms before failing (reason: {reason})."
            )
        if self.is_rate_limited:
            error_message += (
                "\n\t\tHint: client exceeded the platform's concurrency/load "
                "budget. Reduce parallelism or distribute load over time."
            )
        return error_message


class WeclappDeadlineError(Exception):
    """Raised when a single request attempt exceeds the hard wall-clock deadline.

    Treated as a retryable transient failure by the request loop, the same way
    a connection/read timeout is.
    """


def _parse_wait_ms(raw: Optional[str]) -> Optional[int]:
    """Parses the X-Weclapp-Wait-Ms header into an int, returning None if absent or invalid."""
    if raw is None:
        return None
    try:
        return int(raw)
    except (TypeError, ValueError):
        return None


def _backoff_seconds(attempt: int) -> float:
    """Exponential backoff with +/-25% jitter, capped at config.RETRY_MAX_BACKOFF_S.

    `attempt` is zero-based; the sleep happens between attempts.
    """
    base = min(
        config.RETRY_INITIAL_BACKOFF_S * (2 ** attempt),
        config.RETRY_MAX_BACKOFF_S,
    )
    jitter = base * 0.25 * (2 * random.random() - 1)
    return max(0.0, base + jitter)


_rollbar = None
_rollbar_checked = False


def _get_rollbar():
    """Lazily import rollbar iff reporting is enabled. Returns the module or None."""
    global _rollbar, _rollbar_checked
    if _rollbar_checked:
        return _rollbar
    _rollbar_checked = True
    enabled = os.environ.get(config.ROLLBAR_REPORTING_ENV_VAR, "").lower() in (
        "1", "true", "yes",
    )
    if not enabled:
        return None
    try:
        import rollbar as _rb

        _rollbar = _rb
    except ImportError:
        logging.warning(
            "weclapp: %s is set but the 'rollbar' package is not installed; "
            "load-header reporting disabled. Install pyweclapp[rollbar].",
            config.ROLLBAR_REPORTING_ENV_VAR,
        )
    return _rollbar


def _report_wait_to_rollbar(method, url, status_code, wait_ms, wait_reason, attempt):
    """Best-effort Rollbar report for a throttled response. Never raises."""
    rb = _get_rollbar()
    if rb is None:
        return
    try:
        rb.report_message(
            f"weclapp request queued {wait_ms} ms "
            f"(reason: {wait_reason or 'unspecified'})",
            level="warning",
            extra_data={
                "method": method,
                "url": url,
                "status_code": status_code,
                "wait_ms": wait_ms,
                "wait_reason": wait_reason,
                "attempt": attempt,
            },
        )
    except Exception as exc:  # reporting must never break the request
        logging.warning(
            "weclapp: failed to report wait headers to Rollbar: %r", exc
        )


def _request_with_deadline(
    method: str,
    url: str,
    *,
    headers: dict,
    params: Optional[dict],
    data: Union[str, bytes, None],
) -> requests.Response:
    """Performs one request, enforcing a hard wall-clock cap on the response body.

    The (connect, read) timeout still guards connection setup and inter-byte
    gaps. On top of that, the body is streamed and aborted once the total elapsed
    time exceeds config.REQUEST_HARD_DEADLINE_S -- the backstop that the requests
    timeout cannot provide for a slow-trickling server.

    Raises:
        WeclappDeadlineError: if the hard deadline is exceeded while reading.
    """
    started = time.monotonic()
    response = requests.request(
        method,
        url,
        headers=headers,
        params=params,
        data=data,
        timeout=config.REQUEST_TIMEOUT,
        stream=True,
    )

    chunks = []
    for chunk in response.iter_content(chunk_size=64 * 1024):
        if time.monotonic() - started > config.REQUEST_HARD_DEADLINE_S:
            response.close()
            raise WeclappDeadlineError(
                f"{method} {url} exceeded the "
                f"{config.REQUEST_HARD_DEADLINE_S}s hard deadline"
            )
        chunks.append(chunk)

    # Reattach the fully-read body so callers can use .json()/.content/.text
    # exactly as with a non-streamed response.
    response._content = b"".join(chunks)
    return response


class Weclapp:
    """A class to interact with the Weclapp API.

    Attributes:
        api_token (str): The API token for authentication. If not provided, it will be
            fetched from the environment variable "weclappApiToken".
        domain (str): The Weclapp domain to connect to. If not provided, it will be
            fetched from the environment variable "weclappDomain".
        base_url (str): The base URL for the Weclapp API. Generated from domain
            and API version.
        headers (dict): The headers to use for API requests. Generated from the
            authentication token and content type.

    Methods:
        get: Sends a GET request to the Weclapp API.
        put: Sends a PUT request to update an entity in the Weclapp API.
        post: Sends a POST request to create or update an entity in the Weclapp API.
        delete: Sends a DELETE request to remove an entity from the Weclapp API.
        iterator: Yields entities from the Weclapp API based on the provided query.
    """

    def __init__(
        self,
        api_token: str = None,
        domain: str = None,
        api_version: str = config.API_VERSION,
    ):
        if not api_token:
            api_token = os.environ.get(config.API_TOKEN_ENV_VAR)
        if not domain:
            domain = os.environ.get(config.DOMAIN_ENV_VAR)
        domain = self._check_domain(domain)
        self.base_url = f"https://{domain}/webapp/api/{api_version}"
        self.headers = self._get_headers(api_token)

    def _get_headers(self, api_token: str) -> dict:
        """Returns the headers for the weclapp API request."""
        if not api_token:
            raise ValueError(
                "Authentication token for weclapp must be provided as a non-empty string."
            )

        if not isinstance(api_token, str):
            raise TypeError(
                f"Authentication token for weclapp must be a string, but is {type(api_token)}."
            )

        return {
            config.AUTHENTICATION_TOKEN_NAME: api_token,
            "Content-Type": config.DEFAULT_CONTENT_TYPE,
            "Accept": config.DEFAULT_CONTENT_TYPE,
            "Accept-Encoding": "gzip",
            "User-Agent": (
                f"pyweclapp/{PYWECLAPP_VERSION} "
                f"(Altruan GmbH; +{config.USER_AGENT_CONTACT})"
            ),
            "X-Weclapp-Request-Timeout-Ms": config.REQUEST_TIMEOUT_MS,
            "X-Weclapp-Wait-Timeout-Ms": config.REQUEST_WAIT_TIMEOUT_MS,
        }

    def _request(
        self,
        method: str,
        url: str,
        *,
        params: Optional[dict] = None,
        data: Union[str, bytes, None] = None,
    ) -> requests.Response:
        """Sends an HTTP request to the weclapp API with retry on transient failures.

        Retries on configured status codes (429, 5xx), on connection/timeout
        errors, and on the hard wall-clock deadline (WeclappDeadlineError) with
        exponential backoff + jitter. Honors weclapp's load-management
        guidance: backs off rather than hammering the API when the platform signals
        load pressure via 429.

        Args:
            method: HTTP verb ("GET", "PUT", "POST", "DELETE").
            url: Fully-qualified request URL.
            params: Query parameters.
            data: Request body (already serialized to str/bytes).

        Returns:
            The final requests.Response. Callers handle response.ok / WeclappError.
        """
        last_response: Optional[requests.Response] = None
        for attempt in range(config.RETRY_MAX_ATTEMPTS):
            try:
                response = _request_with_deadline(
                    method,
                    url,
                    headers=self.headers,
                    params=params,
                    data=data,
                )
            except (
                requests.exceptions.ConnectionError,
                requests.exceptions.Timeout,
                WeclappDeadlineError,
            ) as exc:
                if attempt + 1 >= config.RETRY_MAX_ATTEMPTS:
                    raise
                sleep_s = _backoff_seconds(attempt)
                logging.warning(
                    "weclapp %s %s: network error %r (attempt %s/%s), retrying in %.2fs",
                    method, url, exc, attempt + 1, config.RETRY_MAX_ATTEMPTS, sleep_s,
                )
                time.sleep(sleep_s)
                continue

            wait_ms = _parse_wait_ms(response.headers.get("X-Weclapp-Wait-Ms"))
            wait_reason = response.headers.get("X-Weclapp-Wait-Reason")
            if wait_ms is not None:
                _report_wait_to_rollbar(
                    method, url, response.status_code, wait_ms, wait_reason, attempt + 1
                )

            if response.status_code in config.RETRY_STATUS_CODES:
                last_response = response
                if attempt + 1 >= config.RETRY_MAX_ATTEMPTS:
                    return response
                sleep_s = _backoff_seconds(attempt)
                logging.warning(
                    "weclapp %s %s: status %s (attempt %s/%s, wait_ms=%s, reason=%s), retrying in %.2fs",
                    method, url, response.status_code,
                    attempt + 1, config.RETRY_MAX_ATTEMPTS,
                    wait_ms, wait_reason, sleep_s,
                )
                time.sleep(sleep_s)
                continue

            if wait_ms is not None:
                logging.info(
                    "weclapp %s %s: server queued request for %s ms (reason: %s)",
                    method, url, wait_ms, wait_reason,
                )
            return response

        # Unreachable in practice — the loop returns or raises on every path —
        # but keep a safety return for the type checker.
        return last_response  # type: ignore[return-value]

    def _check_domain(self, url: str) -> str:
        """Checks if the provided URL is a valid Weclapp domain."""
        if not url:
            raise ValueError("Weclapp domain must be provided as a non-empty string.")
        url = str(url).strip()
        if not url.endswith(config.WECLAPP_DOMAIN_ENDING):
            raise ValueError(
                f"Weclapp domain {url} must end with {config.WECLAPP_DOMAIN_ENDING}."
            )
        return url

    def _parse_response(
        self,
        response: requests.Response,
        as_type: Union[dict, bytes, list] = dict,
        return_full_result: bool = False,
    ) -> Union[dict, list, bytes, int]:
        """
        Parses the response from the Weclapp API and returns it in the specified format.

        Args:
            response (requests.Response): The response object from the Weclapp API.
            as_type (Union[dict, bytes, list]): The type to return the parsed response as.
            return_full_result (bool): If True, returns the full result including metadata.
                If set to True, the function will always return a dict.

        Returns:
            result (Union[dict, list, bytes, int]): The parsed response in the specified format.
        """
        if not response.ok:
            raise WeclappError(response)

        if as_type == bytes:
            return response.content

        json_response = response.json()

        if return_full_result is True:
            if as_type != dict:
                logging.warning(
                    "If return_full_result is True, function will always return a dict."
                )
            return json_response

        result = (
            json_response[config.DEFAULT_RESPONSE_CONTAINER]
            if config.DEFAULT_RESPONSE_CONTAINER in json_response
            else json_response
        )

        if config.COUNT_REQUEST_IDENTIFIER in response.url:
            if isinstance(result, int):
                return result
        elif as_type == dict:
            if not isinstance(result, dict):
                logging.info(
                    "Not a dict object was returned by Weclapp -> turned it into dict"
                )
                result = {config.DEFAULT_RESPONSE_CONTAINER: result}
            return result
        elif as_type == list:
            if not isinstance(result, list):
                logging.info(
                    "Not a list object was returned by Weclapp -> turned it into list"
                )
                result = [result]
            return result
        else:
            raise TypeError("as_type must be one of dict, list, bytes")

        return result

    def get(
        self,
        entity_name: str,
        entity_id: str = None,
        query: dict = None,
        as_type: Union[dict, bytes, list] = dict,
        include_result: bool = False,
        include_additional_properties: bool = False,
        include_referenced_entities: bool = False,
    ) -> Union[dict, list, bytes, int]:
        """Sends a GET request to the Weclapp API.
        Arguments:
            entity_name (str): The name of the entity to retrieve.
            entity_id (str, optional): The ID of the specific entity to retrieve.
            query (dict, optional): Additional query parameters for the request.
            as_type (Union[dict, bytes, list], optional): The type to return the
                parsed response as.
            include_result (bool, optional): If True, returns the full result
                including metadata.
                In this case, the function will always return a dict.
            include_additional_properties (bool, optional): If True, merges
                additionalProperties from the API response into each entity.
                Use this when the query includes additionalProperties parameter.
            include_referenced_entities (bool, optional): If True, adds
                referencedEntities to each entity under '_referencedEntities' key.
                Use this when the query includes includeReferencedEntities parameter.
        Returns:
            result (Union[dict, list, bytes, int]): The parsed response in the
                specified format. When enrichment is requested, returns a list of
                enriched entities.
        """
        query = query or {}
        if not isinstance(query, dict):
            raise TypeError(f"query must be a dict, but got {type(query).__name__}")

        url = f"{self.base_url}/{entity_name}"

        if entity_id is not None:
            url += f"/id/{entity_id}"

        response = self._request("GET", url, params=query)

        if include_additional_properties or include_referenced_entities:
            full_result = self._parse_response(
                response, as_type=dict, return_full_result=True
            )
            return self._enrich_entities(
                full_result,
                merge_additional_properties=include_additional_properties,
                merge_referenced_entities=include_referenced_entities,
            )

        return self._parse_response(
            response, as_type=as_type, return_full_result=include_result
        )

    def put(
        self,
        entity_name: str,
        entity_id: str,
        body: dict,
        ignore_missing_properties: bool = True,
        query: dict = None,
    ) -> dict:
        """Sends a PUT request to the weclapp API.
        Arguments:
            entity_name (str): The name of the entity to update.
            entity_id (str): The ID of the specific entity to update.
            body (dict): The data to update the entity with.
            ignore_missing_properties (bool): If True, the weclapp API will
                ignore missing properties in the body. Be careful when modifying
                list items, all other (unmodified) items need to be mentioned as
                well or they will be deleted!
            query (dict, optional): Additional query parameters for the request.
        Returns:
            result (dict): The parsed response from the API.
        """
        query = query or {}
        url = f"{self.base_url}/{entity_name}/id/{entity_id}"

        if not isinstance(query, dict):
            raise TypeError(f"query must be a dict, but got {type(query).__name__}")
        if not isinstance(body, dict):
            raise TypeError(f"body must be a dict, but got {type(body).__name__}")

        if ignore_missing_properties is True:
            query.update({"ignoreMissingProperties": True})

        response = self._request("PUT", url, params=query, data=json.dumps(body))
        return self._parse_response(response, as_type=dict)

    def post(
        self,
        entity_name: str,
        entity_id: str = None,
        body: dict = None,
        query: dict = None,
    ) -> dict:
        """Sends a POST request to the Weclapp API.
        Arguments:
            entity_name (str): The name of the entity to create or update.
            entity_id (str, optional): The ID of the specific entity to update.
                If None, a new entity will be created.
            body (dict, optional): The data to send in the request body.
            query (dict, optional): Additional query parameters for the request.
        Returns:
            result (dict): The parsed response from the API.
        """
        query = query or {}
        body = body or {}
        if not isinstance(query, dict):
            raise TypeError("query must be a dict")

        if isinstance(body, dict):
            body = json.dumps(body)
        elif isinstance(body, bytes) and entity_name in config.BYTE_TYPE_BODY_ENTITIES:
            logging.info("Sending bytes type body for post request.")
        else:
            raise TypeError("body must be a dict or bytes, when uploading document")

        url = f"{self.base_url}/{entity_name}"
        if entity_id is not None:
            url += f"/id/{entity_id}"

        response = self._request("POST", url, params=query, data=body)
        return self._parse_response(response=response, as_type=dict)

    def delete(
        self,
        entity_name: str,
        entity_id: str,
    ) -> None:
        """Sends a DELETE request to the Weclapp API to delete an entity.
        Arguments:
            entity_name (str): The name of the entity to delete.
            entity_id (str): The ID of the specific entity to delete.
        """

        logging.warning("Deleting entity %s with id %s", entity_name, entity_id)
        url = f"{self.base_url}/{entity_name}/id/{entity_id}"
        response = self._request("DELETE", url)

        if not response.ok:
            raise WeclappError(response)

    def _enrich_entities(
        self,
        response: dict,
        merge_additional_properties: bool = False,
        merge_referenced_entities: bool = False,
    ) -> list:
        """Enriches entities with additionalProperties and/or referencedEntities.

        Args:
            response (dict): The full API response containing 'result' and
                optionally 'additionalProperties' and/or 'referencedEntities'.
            merge_additional_properties (bool): If True, merges additionalProperties
                into each entity by index.
            merge_referenced_entities (bool): If True, adds referencedEntities
                to each entity under '_referencedEntities' key.

        Returns:
            list: List of entities with additional data merged in.
        """
        result = response.get(config.DEFAULT_RESPONSE_CONTAINER, [])

        if merge_additional_properties:
            additional_properties = response.get("additionalProperties", {})
            for index, entity in enumerate(result):
                for prop_name, prop_values in additional_properties.items():
                    if index < len(prop_values):
                        entity[prop_name] = prop_values[index]

        if merge_referenced_entities:
            referenced_entities = response.get("referencedEntities", {})
            if referenced_entities:
                for entity in result:
                    entity["_referencedEntities"] = referenced_entities

        return result

    def _check_iteration_parameters(
        self,
        query: dict,
        page_size: int,
        start_page: int,
        max_entities: int,
    ) -> dict:
        """Checks and prepares the parameters for iteration over entities. If any
        of the parameters are of the wrong type or out of range, it raises an error.
        Returns:
            query (dict): The updated query with pagination parameters.
        """
        query = query or {}
        if not isinstance(query, dict):
            raise TypeError(f"query must be a dict, but got {type(query).__name__}")

        if not isinstance(page_size, int) or not 0 < page_size <= 1000:
            raise ValueError(
                f"Page size must be an integer 0 < page_size <= 1000, but is "
                f"{page_size} of type {type(page_size).__name__}"
            )

        if not isinstance(start_page, int) or start_page < 1:
            raise ValueError(
                f"Start page must be an integer >= 1, but is {start_page} of "
                f"type {type(start_page).__name__}"
            )

        if max_entities and (not isinstance(max_entities, int) or max_entities < 1):
            raise ValueError(
                f"max_entities must be an integer >= 1, but is {max_entities} "
                f"of type {type(max_entities).__name__}"
            )

        if "pageSize" not in query:
            query["pageSize"] = page_size
        elif "pageSize" in query and page_size != query["pageSize"]:
            logging.warning(
                "pageSize in query (%s) does not match the page_size argument "
                "(%s). Using pageSize from query.",
                query["pageSize"],
                page_size,
            )
        return query

    def iterator(
        self,
        entity_name: str,
        query: dict = None,
        page_size: int = 100,
        start_page: int = 1,
        max_entities: int = None,
        enable_logging: bool = True,
        include_additional_properties: bool = False,
        include_referenced_entities: bool = False,
    ) -> Generator[dict, None, None]:
        """Yields all items (dict) of an entityName, that satisfy the query.
        Arguments:
            entity_name (str): The name of the entity to iterate over.
            query (dict, optional): Additional query parameters for the request.
            page_size (int, optional): The number of items to retrieve per page.
                Default is 100, maximum is 1000.
            start_page (int, optional): The page number to start from. Default is 1.
            max_entities (int, optional): Maximum number of entities to yield.
                If None, all entities will be yielded.
            enable_logging (bool, optional): If True, enables logging of the
                iteration process.
            include_additional_properties (bool, optional): If True, merges
                additionalProperties from the API response into each entity.
                Use this when the query includes additionalProperties parameter.
            include_referenced_entities (bool, optional): If True, adds
                referencedEntities to each entity under '_referencedEntities' key.
                Use this when the query includes includeReferencedEntities parameter.
        Yields:
            dict: The next entity in the iteration.
        """
        processed_items = 0
        page = start_page
        query = self._check_iteration_parameters(
            query, page_size, start_page, max_entities
        )

        if enable_logging:
            logging.warning("--- Iteration for %s started ---", entity_name)

        while True:
            query["page"] = page

            if include_additional_properties or include_referenced_entities:
                entity_list = self.get(
                    entity_name=entity_name,
                    query=query,
                    include_additional_properties=include_additional_properties,
                    include_referenced_entities=include_referenced_entities,
                )
            else:
                entity_list = self.get(
                    entity_name=entity_name,
                    query=query,
                    as_type=list,
                )

            if not isinstance(entity_list, list):
                raise ValueError(
                    f"Expected a list of entities, but got {type(entity_list).__name__}: "
                    f"{entity_list}"
                )

            entities_found = len(entity_list)
            if entities_found <= 0:
                break

            if enable_logging:
                logging.warning(
                    "--- Page %s: Found %s entities ---", page, entities_found
                )

            for obj in entity_list:
                processed_items += 1
                if max_entities and max_entities <= processed_items:
                    break
                yield obj

            page += 1
            if max_entities and max_entities <= processed_items:
                break
        if enable_logging:
            logging.warning("--- Iteration for %s finished ---", entity_name)
