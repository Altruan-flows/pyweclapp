from typing import Literal, Union, List
import requests
import json

import logging
from .weclappResponseProcessing import AVAILABEL_APIKEYS, getWeclappHeaders, getWeclappQueries, weclappResponse
# from .weclappError import WeclappError

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from urllib3.exceptions import MaxRetryError






def GET(entityName:Literal["salesOrder", "shipment", "salesInvoice", "contract", "article", "quotation", "customer", "ticket"], 
        entityId:str= None, 
        query:dict={},
        asType:Union[dict, bytes, list]=dict,
        apiKey:AVAILABEL_APIKEYS="Jakob",
        includeResult:bool=False):
    # process URL
    URL = f'https://altruan.weclapp.com/webapp/api/v1/{entityName}'
    if entityId is not None:
        URL += f'/id/{entityId}'
    
        
    response = requests.get(URL, headers=getWeclappHeaders(apiKey=apiKey), params=getWeclappQueries(query=query))
    
    return weclappResponse(response, asType=asType, includeResult=includeResult)


def PUT(entityName:Literal["salesOrder", "shipment", "salesInvoice", "contract", "article", "quotation", "customer", "ticket"], 
        entityId:str, 
        body:dict,
        ignore:bool=True,
        query:dict=None,
        apiKey:AVAILABEL_APIKEYS="Jakob",
        maxRetries:int=0,
        retriesStatus:List[int]=[500, 502, 503, 504, 409]):
    # process URL
    URL = f'https://altruan.weclapp.com/webapp/api/v1/{entityName}/id/{entityId}'
    # logging.info(body)
    
    if query is None:
        query = {}
    assert isinstance(query, dict), "query must be a dict"
    if ignore == True:
        query.update({"ignoreMissingProperties": True})
    

    response = requests.put(URL, headers=getWeclappHeaders(apiKey=apiKey), data=json.dumps(body),  params=query)
    # if not response.ok and maxRetries > 0 :
    #     assert isinstance(maxRetries, int), f"maxRetries is not int, but {maxRetries}"
    #     assert isinstance(retriesStatus, list), f"retriesStatus is not a list"
    #     assert all([isinstance(el, int) for el in retriesStatus]), f"retriesStatus needs to be list of int"
    #     response2 = None
    #     try:
    #         # Create a retry strategy
    #         retries = Retry(total=maxRetries, backoff_factor=0.1, status_forcelist=retriesStatus)

    #         # Create a session with the retry strategy
    #         session = requests.Session()
    #         adapter = HTTPAdapter(max_retries=retries)
    #         session.mount("http://", adapter)
    #         session.mount("https://", adapter)
                
    #         response2 = session.put(URL, headers=getWeclappHeaders(apiKey=apiKey), data=json.dumps(body),  params=query)
    #     except Exception as e:
    #         logging.error(f"MaxRetryError: {e}")
    #     if response2 is not None:
    #         response = response2
    return weclappResponse(response, asType=dict)


def POST(entityName:Literal["salesOrder", "shipment", "salesInvoice", "contract", "article", "quotation", "customer", "ticket"], 
         body:dict={},
         entityId:str= None, 
         apiKey:AVAILABEL_APIKEYS="Jakob",
         query:dict=None,
         maxRetries:int=0,
         retriesStatus:List[int]=[500, 502, 503, 504, 409]):
    if query is None:
        query = {}
    assert isinstance(query, dict), "query must be a dict"
    assert isinstance(body, dict) or (isinstance(body, bytes) and "document" in entityName), "body must be a dict or bytes, when uploading document"

    # process URL
    URL = f'https://altruan.weclapp.com/webapp/api/v1/{entityName}'
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
    
    # if not response.ok and maxRetries > 0 :
    #     assert isinstance(maxRetries, int), f"maxRetries is not int, but {maxRetries}"
    #     assert isinstance(retriesStatus, list), f"retriesStatus is not a list"
    #     assert all([isinstance(el, int) for el in retriesStatus]), f"retriesStatus needs to be list of int"
    #     response2 = None
    #     try:
    #         logging.warning(f"requests error -> Retrying...")
    #         # Create a retry strategy
    #         retries = Retry(total=maxRetries, backoff_factor=0.1, status_forcelist=retriesStatus)

    #         # Create a session with the retry strategy
    #         session = requests.Session()
    #         adapter = HTTPAdapter(max_retries=retries)
    #         session.mount("http://", adapter)
    #         session.mount("https://", adapter)
                
    #         response2 = session.post(URL, headers=headers, data=json.dumps(body))
    #     except Exception as e:
    #         logging.error(f"MaxRetryError: {e}")
    #     if response2 is not None:
    #         response = response2
    
    return weclappResponse(response=response, asType=dict)




def DELETE(entityName:Literal["salesOrder", "shipment", "salesInvoice", "contract", "article", "quotation", "customer", "ticket"], 
        entityId:str, 
        apiKey:AVAILABEL_APIKEYS="Jakob"):
    
    logging.info('--def--- deleteWeclapp')
    # Request Parameters
    URL = f'https://altruan.weclapp.com/webapp/api/v1/{entityName}/id/{entityId}'
    logging.warning(f"DELETE - {URL=}")
    headers = getWeclappHeaders(apiKey=apiKey)

    response = requests.delete(URL, headers=headers)

    logging.info(f'Item deleted {URL}')
    assert response.ok, f"item {entityId} could not be deleted {response.text}"

