from typing import Literal, Union, List
import requests
import json
import os

import logging
from .weclappResponseProcessing import AVAILABEL_APIKEYS, getWeclappHeaders, getWeclappQueries, weclappResponse, getWeclappDomain






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

