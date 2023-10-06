import logging
from .legacyWeclappRequests import askWeclapp





def iterator(query_params: dict, endpoint: str = "salesOrder", demo:bool=False, stopAfterNPages:int=None, log:bool=True, startPage:int=1, pageSize:int=100) -> dict:
    if log:
        logging.info(f"---starting iterating over {endpoint}---")
    
    # init Cariables
    page = startPage
    items = 1
    assert all('-' in str(key) or str(key) in ['properties', "sort"] for key in query_params.keys()), f'Attention Weclapp iterators need to have a query containing a -eq, -in, ...'
    
    while items > 0:
        # prepare Querys
        query = {
            # "responsibleUserFixed": "true", -> wird über query params upgedatet
            "pageSize": pageSize,
            "page": page
            
        }
        query.update(query_params)
        
        # get Object
        weclappObjList = askWeclapp(method='GET', endpoint=endpoint, query_params=query, body = {}, demo=demo)['result']
        
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
        