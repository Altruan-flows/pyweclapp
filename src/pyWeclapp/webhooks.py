from . import weclapp
import logging
from jsonschema import validate


class HookRequest:
    
    def __init__(self, webhook:dict, loopPervAttDefId:str="14568660"):
        """{
            "entityId": "2792591",
            "entityName": "article",
            "type": "UPDATE"
        }"""
        try:
            logging.info(webhook)
            webhook = self.cleanAndValidateDictWithJsonSchema(retrievedObject=webhook)
            self.entityId = webhook.get('entityId')
            self.entityName = webhook.get('entityName')
            self.action = webhook.get('type')
            self.loopPervAttDefId = str(loopPervAttDefId)
            self.toUpdate = {}

        except Exception as e:
            logging.error(channel='error', message=f"Webhook was not parsed properly", facts={'error': e}, send=True)
            
    @staticmethod
    def cleanAndValidateDictWithJsonSchema(retrievedObject: dict,  log:bool=True) -> dict:
        if log:
            logging.info("---util.cleanAndValidateDictWithJsonSchema()---")
        try:
            jsonSchema = {
                "$schema": "http://json-schema.org/schema#",
                "type": "object",
                "properties": {
                    "entityId": {
                        "type": "string"
                    },
                    "entityName": {
                        "type": "string"
                    },
                    "type": {
                        "type": "string"
                    }
                },
                "required": [
                    "entityId",
                    "entityName",
                    "type"
                ]
            }

            validate(instance=retrievedObject, schema=jsonSchema)
            toReturn = {}
            
            for line in jsonSchema["required"]:
                toReturn[line] = retrievedObject[line]
                
            return toReturn
        except Exception as e:
            logging.error(f'---shema Validation failed--- >>>{e}<<<')
            raise ValueError(f'---shema Validation failed--- >>>{e}<<<')
        
        
        
        
    # ask weclapp to return the full object
    def getObject(self, query:dict=None, timeLimitS:int=30, turnOffLoopPrevention:bool=False):
        # minAge = round((time.time() - int(timeLimitS)) * 1000)
        queryParams = {
            # f"customAttribute{self.loopPervAttDefId}-le": minAge,
            "id-eq": str(self.entityId)
        }    
        if query:
            for key, value in query.items():
                if key != "properties":
                    assert "-" in key, f"query must contain -eq, -ne, -le, ..."
                else:
                    assert "version" in value, f"Version must be included when using properties for Loop prevention"
                    assert "customAttributes" in value, f"customAttributes must be included when using properties for Loop prevention"
            queryParams.update(query)
        logging.info(f"{queryParams}")
        answer = weclapp.GET(entity_name=self.entityName, query_params=queryParams)
        logging.info(f"{answer=}")
        result = answer['result']
        logging.info(f"{len(result)=}")
        assert len(result) <= 1, f"Got a response with a length of more than 1 -> Should get max 1!!!"
        if len(result) == 1:
            self.result = self.loopPerventor(result[0], turnOffLoopPrevention=turnOffLoopPrevention)
            return self.result
        else:
            return None
    
    # checks if version allignes with saved one
    def loopPerventor(self, result:dict, turnOffLoopPrevention:bool=False):
        if turnOffLoopPrevention:
            logging.warning('loop pervention turned off!!!')
            return result
        self.version = result.get('version')
        logging.info(self.version)
        customAttributes = result.get('customAttributes')
        for customAttribute in customAttributes:
            if customAttribute.get('attributeDefinitionId') == self.loopPervAttDefId:
                if str(customAttribute.get('stringValue')) != str(self.version):
                    logging.info(customAttribute)
                    logging.warning('No Loop')
                    return result
        logging.warning('Loop found !!!!!! -> No execution')
        return None
    
    # ads an element to self.toUpdate
    def addUpdateElement(self, body:dict):

        if body:
            self.toUpdate = self.update(body, self.toUpdate)

    
    
    def update(self, d, u):
        for k, v in u.items():
            if isinstance(v, list):
                if isinstance(d[k], list):
                    result = []
                    d[k].extend(v)
                    for myDict in d[k]:
                        if myDict not in result:
                            result.append(myDict)
                    d[k] = result
                else:
                    raise ValueError("content could not be updated: not tow list")
            elif isinstance(v, dict):
                d[k] = self.update(d.get(k, {}), v)
            else:
                d[k] = v
        return d
    
    
    def recursiveCheck(self, base:dict, subset, enforceTypeEquality:bool=False) -> bool:

        for subsetkey, subsetValue in subset.items():
            baseValue = base.get(subsetkey, None)
            if type(baseValue) != type(subsetValue):
                if enforceTypeEquality:
                    # will trigger if a field is not delivered by the weclapp api
                    logging.error(f"{base} {subsetValue}")
                    logging.error(f"{type(baseValue).__name__} {type(subsetValue).__name__}")
                    raise ValueError(f"DataTypes of objects are not identicale")
                else:
                    logging.warning(f"unequal types")
                    return False
            elif isinstance(subsetValue, list):
                # checks if all elements exist in the list, ignotes extensions
                if not all(subsetEl in baseValue for subsetEl in subsetValue):
                    logging.warning(f"unequal list")
                    return False
                
            elif isinstance(subsetValue, dict):
                # Recursive call of checking dicts
                if not self.recursiveCheck(baseValue, subsetValue):
                    return False
                
            else:
                if subsetValue != baseValue:
                    logging.warning(f"unequal Values")
                    return False
                
        return True
    
    
    def updateIsIdenticale(self) -> bool:
        if self.result:
            return self.recursiveCheck(self.result, self.toUpdate)
        else:
            logging.warning(f"No self.result")
            return True
    
    
    # Update weclapp
    def updateObject(self) -> dict:
        # include optimistic locs Error by adding version -> it may be necessary to repeat the whole process
        if self.toUpdate:
            if not self.updateIsIdenticale():
                self.addUpdateElement(body={"customAttributes": [
                    {
                        "attributeDefinitionId": str(self.loopPervAttDefId),
                        "stringValue": str(int(self.version) + 1)
                    }
                ]})
                logging.info(f"{self.toUpdate=}")
                return weclapp.PUT(entityName=self.entityName,
                                        entityId=self.entityId, 
                                        body=self.toUpdate)
            else:
                logging.warning(f"Nothing has been changed -> update not necessary")
