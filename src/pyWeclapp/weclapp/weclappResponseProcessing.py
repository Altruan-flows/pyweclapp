import requests
import os
import logging
from .weclappError import WeclappError
from typing import Union
from . import config


def getWeclappHeaders(apiKey: config.AVAILABLE_APIKEYS = "key0") -> dict:
    # Check if apiKey is valid
    if "key" not in apiKey:
        raise ValueError(f"apiKey must be one of {config.AVAILABLE_APIKEYS}")

    apiKeyName = config.ENV_AUTHENTICATION_TOKEN_NAME_BASE + apiKey.strip()[-1]
    authenticationToken = os.environ.get(apiKeyName, None)

    # Check if the authentication token is found
    if authenticationToken is None:
        raise ValueError(
            f"Authentication Token {apiKeyName} for weclapp not found in environment variables. Please add it."
        )

    # Check if the authentication token is a string and not empty
    if not isinstance(authenticationToken, str) or len(authenticationToken) == 0:
        raise TypeError(
            f"Authentication Token {apiKeyName} for weclapp is not a valid string. Please check it."
        )

    # Check if the authentication token has a valid format
    if len(authenticationToken.split("-")) != 5:
        raise ValueError(
            f"Authentication Token {apiKeyName} for weclapp is not valid. Please check it."
        )

    return {
        config.AUTHENTICATION_TOKEN_NAME: authenticationToken,
        "Content-Type": config.DEFAULT_CONTENT_TYPE,
    }


def getWeclappDomain() -> str:
    url = os.environ.get(config.ENV_DOMAIN_NAME, None)
    if url is None:
        raise ValueError(
            f'weclappDomain not found in environment variables. Please set it '
            f'using os.environ["{config.ENV_DOMAIN_NAME}"] = "yourDomain.weclapp.com"'
        )
    url = str(url).strip()
    if not url.endswith(".weclapp.com"):
        raise ValueError(
            f'weclappDomain {url} is not valid. Please set it using os.environ'
            f'["{config.ENV_DOMAIN_NAME}"] = "yourDomain.weclapp.com"'
        )
    return url


def getWeclappQueries(query: dict):
    for key in query:
        if key not in config.ODATA_EXCEPTIONS and "-" not in str(key):
            raise ValueError(
                f"Query >> {key} << in weclapp need to contain one of -eq, -ne,-le, -ge, -in, -ilike, -like, ..."
            )
    return query


def weclappResponse(
    response: requests.Response,
    asType: Union[dict, bytes, list] = dict,
    includeResult: bool = False,
) -> Union[dict, list, bytes, int]:
    if response.ok:
        if config.COUNT_REQUEST_IDENTIFIER in response.url:
            obj = response.json()
            logging.warning("A count request was sent to Weclapp returning int")
            if isinstance(obj["result"], int):
                return obj["result"]
            return weclappResponse(response, dict)
        elif asType == dict:
            obj = response.json()
            if config.DEFAULT_RESPONSE_CONTAINER in obj and not includeResult:
                result = obj["result"]
                if isinstance(result, list):
                    logging.warning("A list object was returned by Weclapp")
                return result
            else:
                return obj
        elif asType == list:
            obj = response.json()
            if config.DEFAULT_RESPONSE_CONTAINER in obj:
                result = obj["result"]
                if not isinstance(result, list):
                    logging.info(
                        "Not a list object was returned by Weclapp -> turned it into List"
                    )
                    result = [result]
                return result
            else:
                logging.warning(
                    "A dict object was returned by Weclapp -> turned it into List"
                )
                return [obj]
        elif asType == bytes:
            return response.content
        else:
            raise TypeError("asType must be one of dict, list, bytes")
    else:
        raise WeclappError(response)
