from typing import Union, Generator
import requests
import json

import logging
from .weclappResponseProcessing import (
    getWeclappHeaders,
    getWeclappQueries,
    weclappResponse,
    getWeclappDomain,
)
from . import config


def GET(
    entity_name: config.ENTITY_NAMES,
    entity_id: str = None,
    query: dict = {},
    as_type: Union[dict, bytes, list] = dict,
    api_key: config.AVAILABLE_APIKEYS = config.DEFAULT_KEY,
    include_result: bool = False,
):
    # process URL
    URL = f"https://{getWeclappDomain()}/webapp/api/{config.API_VERSION}/{entity_name}"
    if entity_id is not None:
        URL += f"/id/{entity_id}"

    response = requests.get(
        URL,
        headers=getWeclappHeaders(apiKey=api_key),
        params=getWeclappQueries(query=query),
    )
    return weclappResponse(response, asType=as_type, includeResult=include_result)


def PUT(
    entityName: config.ENTITY_NAMES,
    entityId: str,
    body: dict,
    ignoreMissingProperties: bool = True,
    query: dict = None,
    apiKey: config.AVAILABLE_APIKEYS = config.DEFAULT_KEY,
):
    """Sends a PUT request to the weclapp API
    - ignoreMissingProperties: if True, the API will ignore missing properties
    in the body - be careful when modifying list items, all other (unmodifiesd)
    items need to be mentioned as well or they will be deleted
    - apiKey: Selects the API Key to use for the request"""
    # process URL
    URL = f"https://{getWeclappDomain()}/webapp/api/{config.API_VERSION}/{entityName}/id/{entityId}"

    query = query or {}
    if not isinstance(query, dict):
        raise TypeError("query must be a dict")

    if ignoreMissingProperties is True:
        query.update({"ignoreMissingProperties": True})

    response = requests.put(
        URL,
        headers=getWeclappHeaders(apiKey=apiKey),
        data=json.dumps(body),
        params=query,
    )

    return weclappResponse(response, asType=dict)


def POST(
    entityName: config.ENTITY_NAMES,
    body: dict = None,
    entityId: str = None,
    apiKey: config.AVAILABLE_APIKEYS = config.DEFAULT_KEY,
    query: dict = {},
):

    query = query or {}
    body = body or {}
    if not isinstance(query, dict):
        raise TypeError("query must be a dict")

    if not (
        isinstance(body, dict)
        or (isinstance(body, bytes) and entityName in config.BYTE_TYPE_BODYS_ENTITIES)
    ):
        raise TypeError("body must be a dict or bytes, when uploading document")

    # process URL
    URL = f"https://{getWeclappDomain()}/webapp/api/{config.API_VERSION}/{entityName}"
    if entityId is not None:
        URL += f"/id/{entityId}"

    logging.warning(f"Post - {URL=}")
    headers = getWeclappHeaders(apiKey=apiKey)

    if isinstance(body, dict):
        body = json.dumps(body)
    else:
        logging.info("Bytes type Body for Post found!!!")

    response = requests.post(URL, headers=headers, data=body, params=query)

    return weclappResponse(response=response, asType=dict)


def DELETE(
    entityName: config.ENTITY_NAMES,
    entityId: str,
    apiKey: config.AVAILABLE_APIKEYS = config.DEFAULT_KEY,
):

    logging.warning(f"TRYING TO DELETE ITEM {entityId} form {entityName}")
    # Request Parameters
    URL = f"https://{getWeclappDomain()}/webapp/api/{config.API_VERSION}/{entityName}/id/{entityId}"

    headers = getWeclappHeaders(apiKey=apiKey)

    response = requests.delete(URL, headers=headers)

    assert response.ok, f"item {entityId} could not be deleted {response.text}"


def iterator(
    entityName: config.ENTITY_NAMES,
    query: dict = {},
    enableLogging: bool = True,
    startPage: int = 1,
    pageSize: int = 100,
    apiKey: config.AVAILABLE_APIKEYS = config.DEFAULT_KEY,
    maxEntities: int = None,
) -> Generator[dict, None, None]:
    """Yields all items (dict) of an entityName, that satisfy the query.
    - entityName: the weclapp EntityName of the entity to iterate over
    - query: the query to filter the items. If None, all items will be returned
    - enableLogging: if True, the iterator will log the page number and the number of items on the page
    - pageSize: the number of items per page. Minimum is 1, maximum is 1000
    - maxEntities: if None, the iterator will run until the last available Entity. Minimum is 1
    """

    # check input
    if not 0 < pageSize <= 1000:
        raise ValueError(f"pageSize must be 0 < pageSize <= 1000, but is {pageSize}")

    if maxEntities is not None and int(maxEntities) < 1:
        maxEntities = 1

    if enableLogging:
        logging.info(f"---starting iterating over {entityName}---")

    proccessedItems = 0
    page = startPage
    query = query.copy() or {}
    query["pageSize"] = pageSize

    while True:
        # prepare Querys
        query["page"] = page
        weclappObjList = GET(
            entity_name=entityName,
            query=query,
            as_type=list,
            api_key=apiKey,
            include_result=False,
        )

        # check Result
        if not isinstance(weclappObjList, list):
            raise ValueError(
                f"List Item Expected from => {entityName}: got {type(weclappObjList).__name__}"
            )

        entitiesFound = len(weclappObjList)
        if entitiesFound <= 0:
            break

        if enableLogging:
            logging.warning(f"--------PAGE {page}--------- {entitiesFound=}")

        # yield all purchases of customer
        for obj in weclappObjList:
            proccessedItems += 1
            if maxEntities is not None:
                if maxEntities < proccessedItems:
                    break
            yield obj

        page += 1
        if maxEntities is not None:
            if maxEntities < proccessedItems:
                break
    if enableLogging:
        logging.info(f"---finished iterating over {entityName}---")
