from ... import weclapp
from .weclappClassCustomAtt import WeclappMetaData
import logging
from typing import *
import json




class Blueprint:
    USED_ATTRIBUTES:dict = dict()
    
    
    def __init__(self, itemsName:str, usedAtts:dict=dict()):
        self.ITEMS_NAME = itemsName
        self.USED_ATTRIBUTES = usedAtts

        
        
    def incrementVersion(self):
        if hasattr(self, 'version'):
            version = int(float(getattr(self, 'version')))
            setattr(self, 'version', str(version + 1))
            logging.info(f"Incremented Version to {version + 1}")
        else:
            logging.info(f"No Version Attribute found")
    
            
    '''Dies Ist eine Klase, die nicht eigenständig vverwendet werden sollte'''
    def queryMetaData(self, value, raiseError:bool = True, addToMetaData:bool=False) -> WeclappMetaData:
        
        try:
            try:
                # Intrgrate CAT more easily by directly inserting the named tuple
                valueId = value
                if isinstance(value, tuple) and hasattr(value, "_fields") and hasattr(value, "id"):
                    valueId = value.id
            except:
                valueId = value
            for el in self.customAttributes:
                if el.name == valueId:
                    return el
            raise KeyError(f"Custom Attribute {value} not found")

        except KeyError as e:
            if raiseError:
                raise e
            else:
                # create Custom Attribute
                item = WeclappMetaData(attributeDefinitionId=value)
                if addToMetaData:
                    self.customAttributes.append(item)
                return item
        # try:
            

        #     for el in self.customAttributes:
        #         if el.name == value:
        #             return el
        #     raise KeyError(f"Custom Attribute {value} not found")

        # except KeyError as e:
        #     if raiseError:
        #         raise e
        #     else:
        #         # create Custom Attribute
        #         item = WeclappMetaData(attributeDefinitionId=value)
        #         if addToMetaData:
        #             self.customAttributes.append(item)
        #         return item
            
            
            
    def query(self, key:str, value:Any, entity:str, raiseError:bool = True):
        try:
            if hasattr(self, entity):
                for el in getattr(self, entity):
                    if getattr(el, key) == value:
                        return el
                raise KeyError(f"Item >{value}< not found in >{entity}<")
            else:
                raise KeyError(f"Attribute >{entity}< not found")

        except KeyError as e:
            if raiseError:
                raise e
            else:
                return None
           
           
            
    def queryItems(self, key:str, value:Any, justParentItems:bool=True, raiseError:bool = True):
        try:
            for el in getattr(self,self.ITEMS_NAME):
                if getattr(el, key) == value:
                    if justParentItems:
                        if not hasattr(self, 'parentItemId'):
                            return el
                        else:
                            raise KeyError(f"Attribute is not ParentArticle -> it is not recomendet to edit this articles; else set justParentItems=False")
                    else:
                        return el
            raise KeyError(f"Item {value} not found")

        except KeyError as e:
            if raiseError:
                raise e
            else:
                return None
    
    
    
    def qmd(self, value, raiseError:bool = True, addToMetaData:bool=False) -> WeclappMetaData:
        """short Version for queryMetaData Function"""
        return self.queryMetaData(value=value, raiseError=raiseError, addToMetaData=addToMetaData)
    
    
    
    
    
    ################################### Used Attribute Handling ###################################
    
    
    
    
    
    
    def resetUsedAtts(self):
        self.USED_ATTRIBUTES = {}
        
        
    def resetAllUsedAtt(self):
        self.resetUsedAtts()
        for key, value in self.__dict__.items():
            if isinstance(value, list):
                for el in value:
                    if hasattr(el, "resetUsedAtts"):
                        el.resetUsedAtts()
                    elif hasattr(el, "updated") and getattr(el, "updated") is True:
                        el.updated = False
            elif hasattr(value, "resetUsedAtts"):
                value.resetUsedAtts()
    
    
    def addUsedAtt(self, attName):
        if hasattr(self, attName):
            self.USED_ATTRIBUTES[attName] = getattr(self, attName)
    
    
    def delUsedAttr(self, attName):
        if attName in self.USED_ATTRIBUTES:
            del self.USED_ATTRIBUTES[attName]
            logging.warning(f"Deleted Attribute {attName} from Used Attributes")
    
            
    def setValue(self, key, value):
        assert hasattr(self, key), f"{type(self).__name__} has no attribute {key} -> check spelling, make sure it is included"
        setattr(self, key, value)
        # self.USED_ATTRIBUTES[key] = value # -> not necessary because of __setattr__
        

    def restoreValue(self, key):
        assert hasattr(self, key), f"{type(self).__name__} has no attribute {key} -> check spelling, make sure it is included"
        value = self.USED_ATTRIBUTES.get(key)
        logging.warning(f"Restoring {key} to {value}")
        setattr(self, key, value)
        
        
        
        
        
        
        
    ################################### Core Functions ###################################
    
    
    
    
    
    
    
    def __setattr__(self, __name: str, __value: Any) -> None:
            
        # Ensure type consistancy
        if type(__value) in  [int, str, float, bool]:
            if type(__value) != self.__annotations__.get(__name, type(__value)):
                targetType = self.__annotations__.get(__name, type(__value))
                logging.warning(f"You tried to assign {__value} ({type(__value).__name__}) to the {targetType.__name__} attribute {__name} -> try to converted it")
                if targetType == int:
                    __value = int(float(__value))
                elif targetType == str:
                    __value = str(__value)
                elif targetType == bool:
                    __value = bool(__value)
                elif targetType == float:
                    __value = float(__value)
                else:
                    logging.error(f"failed to correct it...")
                    raise TypeError(f"You tried to assign an {type(__value).__name__} to the {targetType.__name__} attribute {__name} -> could not correct it")
        
        # Check if somthing would change
        if __value != getattr(self, __name):
            if isinstance(__value, tuple):
                if len(__value) == 2:
                    __value, justUsedKeys = __value
                    if justUsedKeys:
                        if __name not in ["USED_ATTRIBUTES", "ITEMS_NAME"]:
                            self.USED_ATTRIBUTES[__name] = getattr(self, __name)
                    else:
                        logging.warning(f"Not Adding >{__name}< in >{type(self).__name__}< to used keys")
            elif __name not in ["USED_ATTRIBUTES", "ITEMS_NAME"]:
                self.USED_ATTRIBUTES[__name] = getattr(self, __name)
                
            object.__setattr__(self, __name, __value)
        elif __name not in ["USED_ATTRIBUTES", "ITEMS_NAME"]:
            logging.info(f"Attribute {__name} is already set to {__value} -> nothing changed")
    
            
            
    def getUpdateDict(self, updateType:Literal['full', 'used', 'used+']='full'):
        alwaysToExclude = ['USED_ATTRIBUTES', 'ITEMS_NAME', "USED_KEYS", "statusHistory"] # statusHistory

        data = {}
        for key, value in self.__dict__.items():
            # excludes Empty Values and uninitialized classes
            if (value or value is False) and not isinstance(value, type) and key not in alwaysToExclude:
                # try:
                    # handl custom Attributes
                    if key == "customAttributes":
                        helper = []
                        for el in value:
                            updateTypeCAtts = updateType if updateType != "used+" else 'used'
                            cat = el.getUpdateDict(updateType=updateTypeCAtts)
                            if updateType == 'full':
                                helper.append(cat)
                            elif cat:
                                helper.append(cat)
                        if len(helper) > 0:
                            data[key] = helper
                            
                    # handle contract Items
                    elif isinstance(value, list) and self.__annotations__.get(key, list) != list:
                        helper = []
                        itemsUpdateNecessary = False
                        for el in value:
                            if hasattr(el, 'getUpdateDict'):
                                if updateType == 'full':
                                    helper.append(el.getUpdateDict(updateType=updateType))
                                elif updateType == "used+":
                                    oldUsedItems = el.USED_ATTRIBUTES
                                    el.addUsedAtt("id")
                                    el.addUsedAtt("version")
                                    item = el.getUpdateDict(updateType="used+")
                                    if len(item) > 2:
                                        itemsUpdateNecessary = True
                                    helper.append(item)
                                    el.USED_ATTRIBUTES = oldUsedItems
                                elif updateType == "used":   
                                    oldUsedItems = el.USED_ATTRIBUTES
                                    el.addUsedAtt("id")
                                    item = el.getUpdateDict(updateType="used")
                                    # item = el.getUsedAttributes(add=['id'])
                                    if len(item) > 1:
                                        itemsUpdateNecessary = True
                                    helper.append(item)
                                    el.USED_ATTRIBUTES = oldUsedItems
                            elif isinstance(el, dict):
                                helper.append(el)
                                itemsUpdateNecessary = True
                        if len(helper) > 0:
                            if updateType in ['used', 'used+'] and not itemsUpdateNecessary:
                                # logging.warning(f"Excluded items, because nothing updated")
                                pass
                            else:
                                # Update Type "full" or items changed
                                data[key] = helper
                    
                    # handle list of dict
                    elif isinstance(value, list) and (updateType in ['full'] or key in self.USED_ATTRIBUTES):
                        helper = []
                        for el in value:
                            if isinstance(el, dict):
                                helper.append(el)
                            else:
                                logging.error(f"handled Error: {el} is not a dict")
                        if len(helper) > 0:
                            data[key] = helper

                            
                    # handl Other classes
                    elif hasattr(value, 'getUpdateDict'):
                        ocls = value.getUpdateDict(updateType=updateType)
                        if ocls:
                            data[key] = ocls
                    
                    # Normal attributes
                    elif key in self.USED_ATTRIBUTES or updateType == 'full' or (key in ["version"] and updateType== "used+"):
                        if value is not None:
                            data[key] = value  
                # except Exception as e:
                #     logging.error(f'Error at key {key=}')
                #     raise e
        if 'ITEMS_NAME' in data:
            del data["ITEMS_NAME"]
            
        if "USED_KEYS" in data:
            del data["USED_KEYS"]
            
        if 'USED_ATTRIBUTES' in data:
            del data["USED_ATTRIBUTES"]
        return data
    





    ################################### Change Management version ###################################
    
    
    
    @property
    def __entityName__(self) -> str:
        classType = type(self)
        entityName = str(classType.__name__)
        entityName = entityName[:1].lower() + entityName[1:]
        return entityName
    

    @staticmethod
    def assesChanges(first, other):
        if hasattr(first, "USED_ATTRIBUTES") and hasattr(first, "version") and hasattr(other, "version") and issubclass(type(first), type(Blueprint)):
            assert type(first) == type(other), f"{type(first)} and {type(other)} types are not equal"
            
            for key, value in first.__dict__.items():
                if key not in ["USED_ATTRIBUTES", "ITEMS_NAME", "customAttributes", "version"]:
                    other_value = getattr(other, key)
                    if isinstance(value, list) :
                        for el in value:
                            try:
                                Blueprint.assesChanges(el, other.query(key='id', value=el.id, entity=key))
                            except AttributeError: 
                                pass
                            except AssertionError as ae:
                                logging.error(f"Error while assesing {key} {el.id}: {ae}")
                    elif issubclass(type(value), type(Blueprint)):
                        Blueprint.assesChanges(value, other_value)
                        
                    elif not isinstance(value, dict):
                        if value != other_value:
                            if first.USED_ATTRIBUTES.get(key) == None:
                                logging.warning(f"Uncrittical ChangeFound {key} changed from {value} to {getattr(other, key)}")
                                setattr(first, key, getattr(other, key))
                            elif first.USED_ATTRIBUTES.get(key) != other_value:
                                raise AssertionError(f"Valid Optimistic-Loc Error found: {key} changed from {value} to {getattr(other, key)}")


            first.version = other.version
                                
                     
                     
                            
    def refreshVersion2(self):
        """Refreshes the version and updates Changes from weclapp and includes changes if they are not critical; else raises Error
        """
        logging.warning(f"Refreshing Version of {type(self).__name__}")
        currentEntity = type(self).fromWeclapp2(entityId=self.id)
        self.assesChanges(self, currentEntity)
            
    def refreshVersion(self):
        currentEntity:dict = weclapp.GET(entityName=self.__entityName__, query={"properties":f"id,version,{self.ITEMS_NAME}.version,{self.ITEMS_NAME}.id", "id-eq":self.id})[0]
        realVersion = currentEntity['version']
        self.version = realVersion
        # update Versions of items...
        
        newItemsVersion = {str(item.get('id')): str(int(item.get('version'))) for item in currentEntity.get(self.ITEMS_NAME, [])}
        for item in getattr(self, self.ITEMS_NAME):
            if hasattr(item, "version"):
                item.version = newItemsVersion.get(item.id), False
            elif isinstance(item, dict) and "version" in item and "id" in item:
                relalItemsVersion = newItemsVersion.get(item.get('id'))
                item["version"] = relalItemsVersion
            
            
            
            
            
            
    ################################### Change Management Update ###################################
    
    
    
    
    
    
    def updateEntity(self, updateType:Literal['full', 'used', "used+"]='full', log:bool=False):


        self.queryMetaData("14568660", raiseError=False).setValue(value=str(int(float(self.version))+1), valueName='stringValue')
        if log:
            logging.info(f"updating {self.__entityName__} with {json.dumps(self.getUpdateDict(updateType='used'))}")
        
        body = self.getUpdateDict(updateType=updateType)
        if len(body) == 0:
            logging.warning(f"No fields to update for {self.__entityName__}")
        else:
            newEntity= weclapp.PUT(entityName=self.__entityName__, entityId=self.id, body=body)
            self.updateEntityFromNewEntity(newEntity=newEntity)
        
        
    def refershEntity(self):
        response = weclapp.GET(entityName=self.__entityName__, entityId=self.id, asType=dict)
        self.updateEntityFromNewEntity(newEntity=response)
        logging.warning(f"{self.__entityName__} refreshed")
            
            
            
    def updateEntityFromNewEntity(self, newEntity:Union[dict, object]):
        logging.warning(f"Updateing entity {type(self).__name__}")
        if isinstance(newEntity, dict):
            newEntity = type(self)(**newEntity)
        if type(newEntity) == type(self):
            self.__dict__.update(newEntity.__dict__)
            # reset Used Keys
            self.resetAllUsedAtt()
            logging.warning(f"Entity {type(self).__name__} updated; all fields resetet")
            
        else:
            raise AssertionError('No Matching entity Provided to update the self')

    
    
    def updateWeclapp(self, updateType:Literal['full', 'used', "used+"]='full', setLoopVersion:bool=False, entityName:str=None) -> dict:
        # if entityName is None:
        #     entityName = self.__entityName__
        # try:
        #     if setLoopVersion:
        #         self.queryMetaData("14568660", raiseError=False).setValue(value=str(int(float(self.version))+1), valueName='stringValue')
        # except:
        #     logging.warning('loop Verion could not be set')
        # return weclapp.updateWeclapp(entityName=entityName, entityId=self.id, body=self.getUpdateDict(updateType=updateType))
        logging.warning(f"updateWeclapp is deprecated; use updateWeclapp2 instead")
        return self.updateWeclapp2(updateType=updateType, setLoopVersion=setLoopVersion, entityName=entityName)


    def updateWeclapp2(self, updateType:Literal['full', 'used', "used+"]='full', setLoopVersion:bool=False, entityName:str=None) -> dict:
        if entityName is None:
            entityName = self.__entityName__
        try:
            if setLoopVersion:
                self.queryMetaData("14568660", raiseError=False).setValue(value=str(int(float(self.version))+1), valueName='stringValue')
        except:
            logging.warning('loop Verion could not be set')
        body = self.getUpdateDict(updateType=updateType)
        return weclapp.PUT(entityName=entityName, entityId=self.id, body=body)
    
    
    
    
    
    
    ################################### Recreation ###################################
    
    
    
    
    
    @classmethod
    def fromWeclapp(cls, entityName:str, entityId:str):
        # response = weclapp.askWeclapp(method="GET", endpoint=f"{entityName}/id/{entityId}")
        # return cls(**response)
        logging.warning(f"fromWeclapp is deprecated; use fromWeclapp2 instead")
        return cls.fromWeclapp2(entityId=entityId)
    
    @classmethod
    def fromWeclapp2(cls, entityId:str):
        entityName = cls.__name__
        entityName = entityName[:1].lower() + entityName[1:]
        response = weclapp.GET(entityName=entityName, entityId=entityId, asType=dict)
        return cls(**response)
    
    
 
    @classmethod
    def blank(cls):
        fields = {field: None for field in cls.__fields__}
        return cls(**fields)







