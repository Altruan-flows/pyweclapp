import json
import logging
import os, base64, io
import requests
import util
from typing import *




def askWeclapp(method:str="GET", endpoint:str="salesOrder", query_params:dict=None, body:dict=None, demo:bool=False, returnJson:bool=True) -> dict:
    # logging.info('---askWeclapp()---')
    # Request Parameters
    if demo:
        # demo System weclapp
        URL = f'https://altruan-demo.weclapp.com/webapp/api/v1/{endpoint}'
    else:
        # normales Weclapp
        URL = f'https://altruan.weclapp.com/webapp/api/v1/{endpoint}'
    headers = {
        "AuthenticationToken": os.environ["WeclappAuthenticationToken"],
        'Content-Type': 'application/json'
    }
    if not query_params:
        query_params = {}
    
    if not body:
        body = {}
        
    if method.lower() == "get":
        response = requests.get(URL, headers=headers, data=json.dumps(body), params=query_params)
    elif method.lower() == "post":
        response = requests.post(URL, headers=headers, data=json.dumps(body), params=query_params)
    elif method.lower() == "put":
        logging.warning('do not use put in ask weclapp: -> use updateWeclapp in stead')
        response = requests.put(URL, headers=headers, data=json.dumps(body), params=query_params)
    else:
        response = None
        raise ValueError('Invalid Method in ask weclapp')
    # logging.info('---askWeclapp()2---')
    assert response.status_code < 400, f"--askWeclapp-- got invalid response: {response.json()}"
    if returnJson:
        return response.json()
    else:
        return response



    

def updateWeclapp(entityName: str, entityId: str,  body: dict,  ignore: bool = True, useSecondaryAuth:Literal["Johannes", "Jakob"]= "Jakob") -> dict:
    logging.info('--def--- updateWeclapp')
    # Request Parameters
    URL = f'https://altruan.weclapp.com/webapp/api/v1/{entityName}/id/{entityId}'
    headers = {
        "AuthenticationToken": os.environ["WeclappAuthenticationToken"],
        'Content-Type': 'application/json'
    }
    if useSecondaryAuth != "Jakob":
        try:
            headers["AuthenticationToken"] = os.environ["WeclappAuthenticationTokenJohannes"]
            logging.info('With Johannes Api Key')
        except:
            pass
    # Query Parameters
    if ignore:
        query_params = {
                "ignoreMissingProperties": True
            }
    else:
        query_params = {}
    logging.info(json.dumps(body))
    # data needs to be encoded with urllib.parse.urlencode()
    response = requests.put(URL, headers=headers, data=json.dumps(body), params=query_params)

    logging.info(f'got {response.status_code} response response from {URL}')
    assert response.status_code < 400, f"got invalid response: {URL}{response.json()}"
    return response.json()






def deleteWeclapp(entityName: str, entityId: str) -> bool:
    logging.info('--def--- deleteWeclapp')
    # Request Parameters
    URL = f'https://altruan.weclapp.com/webapp/api/v1/{entityName}/id/{entityId}'
    headers = {
        "AuthenticationToken": os.environ["WeclappAuthenticationToken"],
        'Content-Type': 'application/json'
    }

    # data needs to be encoded with urllib.parse.urlencode()
    response = requests.delete(URL, headers=headers)

    logging.info(f'Item deleted {URL}')
    assert response.status_code == 204, f"got invalid response: {URL}"
    return True


def uploadFile(entityName:str, entityId:str, name:str, description:str, file:bytes, base64Content:str=None, demo:bool= False):
    logging.info('---weclapp.uploadFile()---')
    if base64Content:
        file = base64.b64decode(base64Content.encode())


    endpoint= 'document/upload'
    # Request Parameters
    if demo:
        # demo System weclapp
        URL = f'https://altruan-demo.weclapp.com/webapp/api/v1/{endpoint}'
    else:
        # normales Weclapp
        URL = f'https://altruan.weclapp.com/webapp/api/v1/{endpoint}'
    headers = {
        "AuthenticationToken": os.environ["WeclappAuthenticationToken"],
        'Content-Type': 'application/json'
    }


    response = requests.post(URL, 
                             headers=headers, 
                             data=file, 
                             params={"entityName": entityName, 
                                     "entityId": entityId, 
                                     "name": name, 
                                     "description":description})

    # logging.info('---askWeclapp()2---')
    assert response.status_code < 400, f"--askWeclapp-- got invalid response: {response.json()}"
    return response.json()


def getDocumentFiles(entityName: str, 
                   entityId: str, 
                   docUse: Literal['anlage2', 'anlage4', 'signature', 'pod'],
                   docType: Literal['pdf', 'png'],
                   by:Literal['all', 'latest']) -> Tuple[List[io.BytesIO], List[str]]:
    # ensure Nameing Convention
    _, description = util.documentNamingConvention(use=docUse, docType=docType, fullName='')
    
    # get All documents
    documnts = askWeclapp(method="GET", 
                          endpoint="document", 
                          query_params={
                              "entityId": str(entityId), 
                              "entityName": str(entityName), 
                              "description-eq": description
                              })['result']
    relevantIds = []
    names = []
    dateCreated = 0
    for document in documnts:
        if docType in document.get('name', ''):
            if by == 'all':
                relevantIds.append(document['id'])
                names.append(document.get('name', ''))

            elif by == 'latest' and dateCreated < document['createdDate']:
                dateCreated = document['createdDate']
                relevantIds = [document['id']]
                names = [document.get('name', '')]
        else:
            logging.warning(f"doument found with invalid docType {docType=} =! name={document.get('name', '')}")

    documents = []
    for i, doc in enumerate(relevantIds):
        content = askWeclapp(method="GET",
                             endpoint=f"document/id/{doc}/download", 
                             returnJson=False)
        file = io.BytesIO()
        file.write(content.content)
        file.seek(0)
        documents.append(file)
        
    return documents, names


        
    