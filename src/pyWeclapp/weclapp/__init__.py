from typing import Literal, Union, List
import requests
import json
import os

import logging
from .weclappResponseProcessing import AVAILABEL_APIKEYS, getWeclappHeaders, getWeclappQueries, weclappResponse, getWeclappDomain
from .weclappError import WeclappError




def GET(entityName:Literal["salesOrder", "shipment", "salesInvoice", "contract", "article", "quotation", "customer", "ticket"], 
        entityId:str= None, 
        query:dict={},
        asType:Union[dict, bytes, list]=dict,
        apiKey:AVAILABEL_APIKEYS="key0",
        includeResult:bool=False):
    # process URL
    URL = f'https://{getWeclappDomain()}/webapp/api/v1/{entityName}'
    if entityId is not None:
        URL += f'/id/{entityId}'
    
        
    response = requests.get(URL, headers=getWeclappHeaders(apiKey=apiKey), params=getWeclappQueries(query=query))
    
    return weclappResponse(response, asType=asType, includeResult=includeResult)



def PUT(entityName:Literal["salesOrder", "shipment", "salesInvoice", "contract", "article", "quotation", "customer", "ticket"], 
        entityId:str, 
        body:dict,
        ignore:bool=True,
        query:dict=None,
        apiKey:AVAILABEL_APIKEYS="key0"):
    # process URL
    URL = f'https://{getWeclappDomain()}/webapp/api/v1/{entityName}/id/{entityId}'
    # logging.info(body)
    
    if query is None:
        query = {}
    assert isinstance(query, dict), "query must be a dict"
    if ignore == True:
        query.update({"ignoreMissingProperties": True})
    

    response = requests.put(URL, headers=getWeclappHeaders(apiKey=apiKey), data=json.dumps(body),  params=query)

    return weclappResponse(response, asType=dict)



def POST(entityName:Literal["salesOrder", "shipment", "salesInvoice", "contract", "article", "quotation", "customer", "ticket"], 
         body:dict={},
         entityId:str= None, 
         apiKey:AVAILABEL_APIKEYS="key0",
         query:dict=None):
    if query is None:
        query = {}
    assert isinstance(query, dict), "query must be a dict"
    assert isinstance(body, dict) or (isinstance(body, bytes) and "document" in entityName), "body must be a dict or bytes, when uploading document"

    # process URL
    URL = f'https://{getWeclappDomain()}/webapp/api/v1/{entityName}'
    if entityId is not None:
        URL += f'/id/{entityId}'
    logging.warning(f"Post - {URL=}")
    headers = getWeclappHeaders(apiKey=apiKey)
    # requests.adapters.DEFAULT_RETRIES = 5
    # logging.info(body)
    if isinstance(body, dict):
        body = json.dumps(body)
    else:
        logging.warning(f"Bytes type Body for Post found!!!")
        
    response = requests.post(URL, headers=headers, data=body, params=query)
    
    return weclappResponse(response=response, asType=dict)




def DELETE(entityName:Literal["salesOrder", "shipment", "salesInvoice", "contract", "article", "quotation", "customer", "ticket"], 
        entityId:str, 
        apiKey:AVAILABEL_APIKEYS="key0"):
    
    logging.info('--def--- deleteWeclapp')
    # Request Parameters
    URL = f'https://{getWeclappDomain()}/webapp/api/v1/{entityName}/id/{entityId}'
    logging.warning(f"DELETE - {URL=}")
    headers = getWeclappHeaders(apiKey=apiKey)

    response = requests.delete(URL, headers=headers)

    logging.info(f'Item deleted {URL}')
    assert response.ok, f"item {entityId} could not be deleted {response.text}"





def iterator(entityName: Literal["salesOrder", "shipment", "article", "contract", "ticket", "party", "salesInvoice", "purchaseOrder", "customer"], 
             query: dict = None, 
             enableLogging:bool=True, 
             startPage:int=1, 
             pageSize:int=100,
             maxEntities:int=None) -> dict:
    '''Yields all items (dict) of an entityName, that satisfy the query.
        - entityName: the weclapp EntityName of the entity to iterate over
        - query: the query to filter the items. If None, all items will be returned
        - enableLogging: if True, the iterator will log the page number and the number of items on the page
        - pageSize: the number of items per page. Minimum is 1, maximum is 1000
        - maxEntities: if None, the iterator will run until the last available Entity. Minimum is 1'''
    
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
    query['pageSize'] = pageSize

    while True:
        # prepare Querys
        query['page'] = page
        weclappObjList = GET(entityName=entityName, query=query, asType=list)
        
        # check Result
        if not isinstance(weclappObjList, list):
            raise ValueError(f"List Item Expected from => {entityName}: got {type(weclappObjList).__name__}")
        
        entitiesFound = len(weclappObjList)
        if entitiesFound <= 0:
            break
        
        if enableLogging:
            logging.warning(f'--------PAGE {page}--------- {entitiesFound=}')
        
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
        