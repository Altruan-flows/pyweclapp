"""Response handling for Weclapp API interactions."""

import logging
from typing import Union
import requests
from . import WeclappError
from . import config


def get_headers(api_token: str) -> dict:
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


def check_domain(url: str) -> str:
    """Checks if the provided URL is a valid Weclapp domain."""
    if not url:
        raise ValueError("Weclapp domain must be provided as a non-empty string.")
    url = str(url).strip()
    if not url.endswith(config.WECLAPP_DOMAIN_ENDING):
        raise ValueError(
            f"Weclapp domain {url} must end with {config.WECLAPP_DOMAIN_ENDING}."
        )
    return url


def parse_response(
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

    if config.DEFAULT_RESPONSE_CONTAINER not in json_response:
        raise WeclappError(response)

    if return_full_result is True:
        if as_type != dict:
            logging.warning(
                "If return_full_result is True, function will always return a dict."
            )
        return json_response

    result = json_response[config.DEFAULT_RESPONSE_CONTAINER]

    if config.COUNT_REQUEST_IDENTIFIER in response.url:
        if isinstance(result, int):
            return result
    elif as_type == dict:
        if not isinstance(result, dict):
            logging.warning(
                "Not a dict object was returned by Weclapp -> turned it into dict"
            )
            result = {config.DEFAULT_RESPONSE_CONTAINER: result}
        return result
    elif as_type == list:
        if not isinstance(result, list):
            logging.warning(
                "Not a list object was returned by Weclapp -> turned it into list"
            )
            result = [result]
        return result
    else:
        raise TypeError("as_type must be one of dict, list, bytes")

    return result
