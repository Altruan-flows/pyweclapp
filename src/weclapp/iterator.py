import logging
from .weclappRequests import GET
from typing import *




def iterator( endpoint: Literal["salesOrder", "shipment"], query_params: dict, 
             stopAfterNPages:int=None, log:bool=True, startPage:int=1, pageSize:int=100) -> dict:
    if log:
        logging.info(f"---starting iterating over {endpoint}---")
    assert 0 < pageSize <= 1000, f"pageSize must be <= 1000, but is {pageSize}"
    # init Cariables
    page = startPage
    items = 1
    
    while items > 0:
        # prepare Querys
        query = {
            # "responsibleUserFixed": "true", -> wird über query params upgedatet
            "pageSize": pageSize,
            "page": page
            
        }
        query.update(query_params)
        
        # get Object
        weclappObjList = GET(endpoint=endpoint, query_params=query, body = {})['result']
        
        # check Result
        assert isinstance(weclappObjList, list), f"The endpoint needs to be one that returns an List => {endpoint} is invalid"
        items= len(weclappObjList)
        if log:
            logging.warning(f'--------PAGE {page}--------- {items=}')
        
        # yield all purchases of customer
        for obj in weclappObjList:
            yield obj
        
        page += 1
        
        # check if stop is requested
        if stopAfterNPages:
            if stopAfterNPages < page:
                break
    if log:
        logging.warning(f"---finished iterating over {endpoint}---")
        