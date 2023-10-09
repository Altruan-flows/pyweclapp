import requests, os, logging
from .weclappError import WeclappError
from typing import Union, Literal



AVAILABEL_APIKEYS = Literal["key0", "key1"]



def getWeclappHeaders(apiKey:AVAILABEL_APIKEYS = "key0"):
    assert "key" in apiKey, f"apiKey must be one of {AVAILABEL_APIKEYS}"
    apiKeyName = "Weclapp_AuthenticationToken" + apiKey.strip()[-1]
    authenticationToken = os.environ.get(apiKeyName, None)
    assert authenticationToken is not None, f"Authentication Token {apiKeyName} for weclapp not found in environment variables. Please add it."
    assert isinstance(authenticationToken, str), f"Authentication Token {apiKeyName} for weclapp is not a string. Please check it."
    assert len(authenticationToken) > 0, f"Authentication Token {apiKeyName} for weclapp is empty. Please check it."
    assert len(authenticationToken.split('-')) == 5, f"Authentication Token {apiKeyName} for weclapp is not valid. Please check it."
    return {
        "AuthenticationToken": authenticationToken,
        'Content-Type': 'application/json'
    }
        

def getWeclappDomain():
    url = os.environ.get("weclappDomain", None)
    assert url is not None, f"weclappApiUrl not found in environment variables. Please add it."
    return url
    
def getWeclappQueries(query:dict):
    exceptions = ["properties", "entityId", "entityName", "name", "description", "pageSize", "page", "additionalProperties", "includeReferencedEntities", "serializeNulls", "sort"]  
    for key in query:
        if key not in exceptions:
            assert "-" in str(key), f"Query _{key}_ in weclapp need to contain one of -eq, -ne, -le, -ge, -in, -ilike, -like, ..."
    return query
    # for key in query:
    #     if any([el not in str(key) for el in ["properties", "entityId", "entityName", "name", "description"]]):
    #         assert "-" in str(key), f"Query _{key}_ in weclapp need to contain one of -eq, -ne, -le, -ge, -in, -ilike, -like, ..."
    # return query



def weclappResponse(response:requests.Response, asType:Union[dict, bytes, list]=dict, includeResult:bool=False) -> Union[dict, list, bytes, int]:
    if response.ok:
        if "/count" in response.url:
            obj = response.json()
            logging.warning("A count request was sent to Weclapp returning int")
            if isinstance(obj['result'], int):
                return obj['result']
            return weclappResponse(response, dict)
        elif asType == dict:
            obj = response.json()
            if 'result' in obj and not includeResult:
                result = obj['result']
                if isinstance(result, list):
                    logging.warning("A list object was returned by Weclapp")
                return result
            else:
                return obj
        elif asType == list:
            obj = response.json()
            if 'result' in obj:
                result = obj['result']
                if not isinstance(result, list):
                    logging.info("Not a list object was returned by Weclapp -> turned it into List")
                    result = [result]
                return result
            else:
                logging.warning("A dict object was returned by Weclapp -> turned it into List")
                return [obj]
        elif asType == bytes:
            return response.content
        else:
            raise AssertionError("asType must be one of dict, list, bytes")
    else:
        # logging.error(f"{response.url=}")
        raise WeclappError(response)