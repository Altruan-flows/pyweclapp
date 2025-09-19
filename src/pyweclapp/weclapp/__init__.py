"""This module contains:
- the Weclapp class, which provides methods to interact
with the Weclapp API. It includes methods for sending GET, PUT, POST, and DELETE
requests, as well as an iterator for paginated results.
- the WeclappError class, which is a custom exception class for handling errors
from the Weclapp API.
"""

import json
import os
import logging
from typing import Union, Generator
import requests
from . import config


class WeclappError(Exception):
    """Custom exception class for Weclapp API errors."""

    def __init__(
        self, error_response: requests.Response, api_version: str = config.API_VERSION
    ):
        self.response = error_response
        self.url = str(self.response.url).split(f"/api/{api_version}", maxsplit=1)[-1]
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

    def __str__(self) -> str:
        """Returns a string representation of the WeclappError."""
        if not self.is_json:
            return (
                f"{self.response.status_code}: {self.detail} when sending "
                f"request to {self.url}"
            )

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
        return error_message


class Weclapp:
    """A class to interact with the Weclapp API.

    Attributes:
        api_token (str): The API token for authentication. If not provided, it will be
            fetched from the environment variable "WECLAPP_API_TOKEN".
        domain (str): The Weclapp domain to connect to. If not provided, it will be
            fetched from the environment variable "WECLAPP_DOMAIN".
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
        }

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
        Returns:
            result (Union[dict, list, bytes, int]): The parsed response in the
                specified format.
        """
        query = query or {}
        if not isinstance(query, dict):
            raise TypeError(f"query must be a dict, but got {type(query).__name__}")

        url = f"{self.base_url}/{entity_name}"

        if entity_id is not None:
            url += f"/id/{entity_id}"

        response = requests.get(
            url,
            headers=self.headers,
            params=query,
            timeout=config.REQUEST_TIMEOUT,
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

        response = requests.put(
            url,
            headers=self.headers,
            data=json.dumps(body),
            params=query,
            timeout=config.REQUEST_TIMEOUT,
        )

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

        response = requests.post(
            url,
            headers=self.headers,
            data=body,
            params=query,
            timeout=config.REQUEST_TIMEOUT,
        )

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
        response = requests.delete(
            url, headers=self.headers, timeout=config.REQUEST_TIMEOUT
        )

        if not response.ok:
            raise WeclappError(response)

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
