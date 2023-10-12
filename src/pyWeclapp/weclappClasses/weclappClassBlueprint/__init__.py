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
        """Returns the first item customAttribute where a given attributeDefinitionId equals value 

        Args:
            value (Any): any Value of the key (eg. 123)
            addToMetaData (bool): adds an empty customAttribute if not found
            raiseError (bool, optional): Returns None if nothing found. Defaults to True.

        Raises: KeyError if not found
        """
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
            if addToMetaData and hasattr(self, "customAttributes"):
                item = WeclappMetaData(attributeDefinitionId=value)
                self.customAttributes.append(item)
                return item
            elif raiseError:
                raise e
            else:
                return WeclappMetaData(attributeDefinitionId=value)
            
            
    
    def qmd(self, value, raiseError:bool = True, addToMetaData:bool=False) -> WeclappMetaData:
        """short Version for queryMetaData Function. Returns the first item customAttribute where a given attributeDefinitionId equals value 

        Args:
            value (Any): any Value of the key (eg. 123)
            addToMetaData (bool): adds an empty customAttribute if not found
            raiseError (bool, optional): Returns None if nothing found. Defaults to True.

        Raises: KeyError if not found
        """
        return self.queryMetaData(value=value, raiseError=raiseError, addToMetaData=addToMetaData)
    
    
    
    
    def query(self, key:str, value:Any, entity:str, raiseError:bool = True):
        """Returns the first item in the entity (eg. orderItem) where a given key equals value (e.g. key='id', value='123')

        Args:
            key (str): any attribute of the Child Attribute (eg. id)
            value (Any): any Value of the key (eg. 123)
            entity (str): list of items (eg. orderItems)
            raiseError (bool, optional): Returns None if nothing found. Defaults to True.

        Raises: KeyError if not found
        """
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
        """Returns the first item in the self.ITEMS_NAME (eg. orderItem) where a given key equals value (e.g. key='id', value='123')
            self.ITEMS_NAME is usually orderItems or a similar important list of items

        Args:
            key (str): any attribute of the Child Attribute (eg. id)
            value (Any): any Value of the key (eg. 123)
            raiseError (bool, optional): Returns None if nothing found. Defaults to True.

        Raises: KeyError if not found
        """
        try:
            assert hasattr(self, self.ITEMS_NAME), f"Attribute {self.ITEMS_NAME=} not found or invalid"
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
    
    
    def delUsedAttr(self, attName, suppressWarning:bool=False):
        if attName in self.USED_ATTRIBUTES:
            del self.USED_ATTRIBUTES[attName]
            if not suppressWarning:
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
    
            
            
    def getUpdateDict(self, updateType:Literal['full', 'used', 'used+']='used+', creationMode:bool=False):
        """Returns a drictionary with all attributes that should be updated, excludes all None Values

        Args:
            updateType (Literal[full, used, used+, optional): Mode of update. Defaults to 'used+'.
            creationMode (bool, optional): Used for creating post requests to handle differentces. Defaults to False.
        """
        if creationMode:
            updateType = 'full'
            
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
                            if issubclass(type(el), WeclappMetaData):
                                cat = el.getUpdateDict(updateType=updateType)
                                if updateType == 'full':
                                    helper.append(cat)
                                elif cat:
                                    helper.append(cat)
                            elif isinstance(el, dict) and hasattr(el, "attributeDefinitionId"):
                                helper.append(el)
                        if len(helper) > 0:
                            data[key] = helper
                            
                    # handle contract Items
                    elif isinstance(value, list) and self.__annotations__.get(key, list) != list:
                        helper = []
                        itemsUpdateNecessary = False
                        for el in value:
                            if issubclass(type(el), Blueprint):
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
                                    el.delUsedAttr("version", suppressWarning=True)
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
                            if creationMode:
                                assert key not in ["id", "version"], f"Can not post new Entity {type(self).__name__} -> id or version already set"
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
        """Updates recursively the first entity with the values of the second entity if they are not critical; else raises Error"""
        
        if hasattr(first, "USED_ATTRIBUTES") and hasattr(first, "version") and hasattr(other, "version") and issubclass(type(first), type(Blueprint)):
            assert type(first) == type(other), f"{type(first)} and {type(other)} types are not equal"
            
            for key, value in first.__dict__.items():
                if key not in ["USED_ATTRIBUTES", "ITEMS_NAME", "customAttributes", "version"]:
                    other_value = getattr(other, key)
                    if isinstance(value, list) :
                        for el in value:
                            try:
                                if hasattr(el, "id"):
                                    Blueprint.assesChanges(el, other.query(key='id', value=el.id, entity=key))
                                else:
                                    logging.warning(f"List Item {el} has no id -> can not be assesed")
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
                                
                     
                     
                            
    def refreshVersion(self):
        """Refreshes the version and updates Changes from weclapp and includes changes if they are not critical; else raises Error
        """
        if hasattr(self, "id"):
            logging.warning(f"Refreshing Version of {type(self).__name__}")
            currentEntity = type(self).fromWeclapp(entityId=self.id)
            self.assesChanges(self, currentEntity)
        else:
            logging.warning(f"Can not refresh Version of {type(self).__name__} -> no id found")
            
            
            
            
            
            
    ################################### Change Management Update ###################################
    
    
    
    
    
    
    def updateEntity(self, updateType:Literal['full', 'used', "used+"]='used+'):
        """Mirrors changes to weclapp with the specified updateType and includes any possible change from weclapp

        Args:
            updateType (Literal[full, used, used+, optional): Mode of update. Defaults to 'used+'.
        """

        logging.warning(f"Updating {self.__entityName__} in conjunction with webhooks can lead to loops!!! -> Please take precautions")
        body = self.getUpdateDict(updateType=updateType)
        if len(body) == 0:
            logging.warning(f"No fields to update for {self.__entityName__}")
        else:
            newEntity= weclapp.PUT(entityName=self.__entityName__, entityId=self.id, body=body)
            self.updateEntityFromNewEntity(newEntity=newEntity)
        
        
    def refershEntity(self):
        """Fetches changes that may have occured in weclapp
        """
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

    


    def updateWeclapp(self, updateType:Literal['full', 'used', "used+"]='full') -> dict:
        """Updates weclapp with the specified updateType, without updating self"""
        body = self.getUpdateDict(updateType=updateType)
        return weclapp.PUT(entityName=self.__entityName__, entityId=self.id, body=body)
    
    
    
    def postNewEntity(self) -> dict:
        """Posts a new Entity to weclapp, includes the changes additions from weclapp and returns the new Entity as dict
        """
        
        body = self.getUpdateDict(updateType="full", creationMode=True)
        logging.warning(f"Posting new Entity {type(self).__name__} {body=}")
        newEntityDict = weclapp.POST(entityName=self.__entityName__, body=body)
        
        # Update Entity with values from weclapp
        newEntity = self.updateEntityFromNewEntity(newEntity=newEntityDict)
        return newEntityDict
    
    
    
    ################################### Recreation ###################################
    
    
    
    
    @classmethod
    def fromWeclapp(cls, entityId:str):
        """initializes the class from a weclapp entity
        """
        entityName = cls.__name__
        entityName = entityName[:1].lower() + entityName[1:]
        response = weclapp.GET(entityName=entityName, entityId=entityId, asType=dict)
        return cls(**response)
    
    
 
    @classmethod
    def fromBlank(cls):
        """Creates a blank item with all attributes set to None or empty list or empty nested attributes
        -> used for creating new items and after setting the attributes in conjunction  with self.postNewEntity()
        """
        blankItem = {}
        NoneAtts = []

        for att, fieldInfo in cls.model_fields.items():

            # Normal Attributes
            if fieldInfo.annotation in [str, int, float, bool]:
                blankItem[att] = fieldInfo.annotation()
                NoneAtts.append(att)
                
            # List Attributes
            elif fieldInfo.annotation in [list, dict]:
                if str(fieldInfo.default) == "PydanticUndefined":
                    blankItem[att] = fieldInfo.annotation()

            # init bank lists
            elif getattr(fieldInfo.annotation, '__origin__', None) in [List, list]:
                pass
            
            # add other blank types
            elif isinstance(fieldInfo.annotation, type) and issubclass(fieldInfo.annotation, Blueprint):
                blankItem[att] = fieldInfo.annotation.fromBlank() # replace with .blank()
            else:
                print("other Att found !!!!!")
                save = fieldInfo
                raise Exception(f"Other Att found: {att} - {fieldInfo.annotation}")
            
        # init Att
        item = cls(**blankItem)
        
        # Set all values to None for creation
        for att in NoneAtts:
            setattr(item, att, None)
            
        item.USED_ATTRIBUTES = {}
        return item







