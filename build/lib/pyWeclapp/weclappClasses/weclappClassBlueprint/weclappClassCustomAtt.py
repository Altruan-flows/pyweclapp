from typing import *
import logging
from pydantic import BaseModel
from datetime import datetime
from ... import weclapp, timeFunctions





class WeclappMetaData(BaseModel):
    attributeDefinitionId:str
    valueName:Literal["selectedValueId", "stringValue", "booleanValue", "dateValue", "selectedValues", "entityId", "entityReferences", "numberValue"] = None
    originalValue: Any = None
    value: Any = None
    reset:bool = False
    
    def __init__(self, **data):
        attributeDefinitionId = data["attributeDefinitionId"]
        valueName = None
        value = [] if any(x in data for x in ["selectedValues", "entityReferences"]) else None
        for key in ["selectedValueId", "stringValue", "booleanValue", "dateValue", "selectedValues", "entityId", "entityReferences", "numberValue"]:
            if key in data:
                valueName = key
                value = data.get(key)
                break

        super().__init__(attributeDefinitionId=attributeDefinitionId, valueName=valueName, value=value, originalValue=value)
    

        
    @property
    def updated(self) -> bool:
        if self.originalValue == self.value:
            return False
        elif self.originalValue is None:
            return True
        else:
            # special cases
            if self.value is not None:
                if self.valueName == "numberValue":
                    if float(self.originalValue) == float(self.value):
                        return False
                if self.valueName in ["selectedValueId", "entityId", "dateValue"]:
                    if int(self.originalValue) == int(self.value):
                        return False
                if self.valueName in ["selectedValues", "entityReferences"]:
                    if sorted(self.originalValue, key=lambda x: str(x)) == sorted(self.value, key=lambda x: str(x)):
                        return False
        return True
                
        
        
        
    @property
    def selectedValueId(self) -> str:
        return str(self.value) if self.valueName == "selectedValueId" else None
    
    @property
    def stringValue(self) -> str:
        return str(self.value) if self.valueName == "stringValue" else None
    
    @property
    def booleanValue(self) -> bool:
        return bool(self.value) if self.valueName == "booleanValue" else None
    
    @property
    def selectedValues(self) -> List[dict]:
        return list(self.value) if self.valueName == "selectedValues" else []
    
    @property
    def dateValue(self) -> int:
        return int(self.value) if self.valueName == "dateValue" else None
    
    @property
    def entityId(self) -> str:
        return str(self.value) if self.valueName == "entityId" else None
    
    @property
    def entityReferences(self) -> List[dict]:
        return list(self.value) if self.valueName == "entityReferences" else []
    
    @property
    def numberValue(self) -> float:
        return str(self.value) if self.valueName == "numberValue" else None
    
    
    
    
    def __setattr__(self, name, value):
        if name in ["selectedValueId", "stringValue", "booleanValue", "dateValue", "selectedValues", "entityId", "entityReferences", "numberValue"]:
            self.setValue(value, name)
        else:
            super().__setattr__(name, value)





    def checkValueName(self, valueName:Literal["selectedValueId", "stringValue", "booleanValue", "dateValue", "selectedValues", "entityId", "entityReferences", "numberValue"]):
        if self.valueName is None:
            self.valueName = valueName
        else:
            assert self.valueName == valueName, f"ValueName of cAtt {self.name} is {self.valueName} but should be {valueName}"
        
    # get the valueName of Class
    def getValueName(self):
        return self.valueName
                
    
    @property
    def name(self) -> str:
        return self.attributeDefinitionId
    

    def setValue(self, value, 
                 valueName:Literal["selectedValueId", "stringValue", "booleanValue", "dateValue", "selectedValues", "entityId", "entityReferences", "numberValue"],
                 unselect:bool=False):
        

        self.checkValueName(valueName)
        # If fields need to be resetted
        if unselect:
            self.reset = True
            self.value = None
        
        
        # Update Field
        else:
            self.value = self.validateValue(value)
            if not self.updated:
                logging.info(f"cAtt of {self.attributeDefinitionId} was already {self.value} - not updating")
                

    def addValue(self, value, 
                 valueName:Literal["selectedValues", "entityReferences"]):
        
        self.checkValueName(valueName)
        
        # Update Field
        if not isinstance(self.val, list):
            self.value = self.validateValue([])
        assert isinstance(self.val, list), f"self.value should be list but was {type(self.val).__name__}"
        assert all([isinstance(listEl, dict) for listEl in self.val]), f"All items in list cAtts should be dicts"
        if self.valueName == "selectedValues":
            currentState = set([listEl['id'] for listEl in self.val])
            currentState.add(value)
            newValue = [{'id': el} for el in currentState]
        else:
            assert "entityId" in value and "entityName" in value, f"entityReferences need to have entityId and entityName"
            if not value["entityId"] in [entity["entityId"] for entity in self.val]:
                newValue = self.val
                newValue.append(value)
            else:
                newValue = self.val
        
        self.value = self.validateValue(newValue)
        
        
        
    def removeValue(self, value, 
                 valueName:Literal["selectedValues", "entityReferences"]):
        
        self.checkValueName(valueName)
        
        # Update Field
        assert self.valueName in ["selectedValues", "entityReferences"], f"removing a value to cAtt is only possible for list Types"
        if not isinstance(self.val, list):
            self.value = self.validateValue([])
        assert isinstance(self.val, list), f"self.value should be list but was {type(self.val).__name__}"
        assert all([isinstance(listEl, dict) for listEl in self.val]), f"All items in list cAtts should be dicts"
        newValue = []
        key = "id" if self.valueName == "selectedValues" else "entityId"
        for el in self.val:
            if el[key] != value:
                newValue.append(el)
        
        self.value = self.validateValue(newValue)

    def hasValue(self, targetValue:Any=None) -> bool:
        try:
            if targetValue is None:
                return True if self.val is not None else False
            else:
                if self.valueName == "selectedValues":
                    return targetValue in [el['id'] for el in self.getValue(asType=list, default=[])]
                elif self.valueName == "entityReferences":
                    return targetValue in [el['entityId'] for el in self.getValue(asType=list, default=[])]
                else: 
                    return True if self.val == targetValue else False
        except Exception as e:
            logging.error(f"catched Error in cAtt.hasValue(): {e}")
            return False
        

    @property
    def val(self):
        return self.value
            
    
    
    def validateValue(self, value):
        
        # insert Numbers
        if self.valueName == "numberValue":
            if isinstance(value, float):
                return str(round(value, 2))
            assert str(value).replace('.', '').isnumeric(), f"Error in cAtt.setValue(): Given Value ({str(value)} in object {self.setValue}) is not nummeric"
            return str(value)

        # insert booleans
        elif self.valueName == "booleanValue":
            assert isinstance(value, bool), f"To Update Custom Attribute Value must be bool not {type(value).__name__} "
            return bool(value)

        # insert strings
        elif self.valueName == "stringValue" or self.valueName == "selectedValueId":
            return str(value)
        
        # if date is selected
        elif self.valueName == "dateValue":
            if isinstance(value, datetime):
                value = timeFunctions.localeDatetimeToStr(timestemp=value, to="weclapp")
            assert isinstance(value, int), 'date needs to be int'
            return int(value)

        # if entity is selected -> be carefull no validation
        elif self.valueName == "entityId" or self.valueName == "selectedValueId":
            return str(value)

        # Multiselect -> the whole list of dicts needs to be passed!!!
        elif self.valueName == "selectedValues" or self.valueName == "entityReferences":
            assert isinstance(value, list), f"Type needs to be list of dicts"
            for el in value:
                assert isinstance(el, dict), f"Type needs to be list of dicts - invalid dict -> perhaps overwrite"
            return value

        else:
            raise ValueError("Error in cAtt.setValue(): Something is seriously wrong")
        
        
    def getValue(self, asType:Union[str, dict, int, float, list, set, bool, datetime], 
                 default=None, 
                 raiseError:bool=True) -> Any:
        
        """Get the value of an attribute and convert it to a specified format. If not found used default if specified. If not Possibe: Error

        Args:
            asType (Union[str, dict, int, float, list, set, bool, datetime]): The data type to convert the attribute value to.
            default (Any, optional): The default value to return if the attribute is None. Defaults to None.
            raiseError (bool, optional): Whether to raise an error if there is an exception. Defaults to True.

        Raises:
            ValueError: If the specified data type is not supported.
            ValueError: If the attribute value is None.
            Exception: If there is an exception and `raiseError` is True.

        Returns:
            Any: The value of the attribute in the specified format.
        """
        
        try:
            val = self.val
            if val is None and default is not None: 
                val = default
                
            if val is not None:  
                if asType == str:
                    return str(val)
                
                elif asType == dict:
                    return dict(val)
                
                elif asType == int:
                    return int(float(val))
                
                elif asType == float:
                    return float(val)
                
                elif asType == bool:
                    return bool(val)
                
                elif asType == list:
                    return list(val)
                
                elif asType == set:
                    return set(val)
                
                elif asType == datetime:
                    return timeFunctions.parseLocalizedDatetimes(val)
                
                else:
                    raise ValueError(f"Given Type {asType} not found")
            else:
                raise ValueError(f"Value of {self.attributeDefinitionId} was None")
        except Exception as e:
            logging.error(e)
            if raiseError:
                raise e
            return default
        
        
    def getUpdateDict(self, updateType:Literal['full', 'used']='used'):
        if self.updated or updateType == 'full': 
            answer=  {"attributeDefinitionId": self.attributeDefinitionId}
            if not self.reset and self.valueName is not None:
                answer[self.valueName] = self.val
            return answer
        return None
    
    
    def updateWeclapp(self, entityName:str, 
                        entityId:str, 
                        value:Any, 
                        valueName:Literal["selectedValueId", "stringValue", "booleanValue", "dateValue", "selectedValues", "entityId", "entityReferences", "numberValue"]) -> dict:
        self.setValue(value=value,
                      valueName=valueName)
        body = {"customAttributes": [self.getUpdateDict()]}
        return weclapp.PUT(entityName=entityName, entityId=entityId, body=body)











































# from typing import *
# import logging
# from pydantic import BaseModel
# from datetime import datetime
# from util import weclapp, timeFunctions





# class WeclappMetaData(BaseModel):
#     attributeDefinitionId:str
#     selectedValueId: str = None
#     stringValue: str = None
#     booleanValue: bool = None
#     dateValue: int = None
#     selectedValues: List[dict] = []
#     entityId:str=None
#     entityReferences:List[dict]=None
#     numberValue:str = None
#     valueName:str = None
#     updated:bool = False
#     reset:bool = False
    
#     # get the valueName of Class
#     def getValueName(self):
#         if self.valueName is None:
#             for name in ["selectedValueId", "stringValue", "booleanValue", 
#                     "dateValue", "selectedValues", "entityId",
#                     "entityReferences", "numberValue"]:
#                 if getattr(self, name) or (name == "booleanValue" and getattr(self, name) != None):
#                     self.valueName = name
#                     break
#             else:
#                 self.valueName = None
                
    
#     @property
#     def name(self) -> str:
#         return self.attributeDefinitionId
    

#     def setValue(self, value, 
#                  valueName:Literal["selectedValueId", "stringValue", "booleanValue", "dateValue", "selectedValues", "entityId", "entityReferences", "numberValue"],
#                  unselect:bool=False,
#                  forceUpdate:bool=False):
        
#         # ensure that valueNmae exists
#         self.getValueName()
#         if not self.valueName:
#             # logging.warning(f"Using provided default valueName")
#             self.valueName = valueName
            
#         # If fields need to be resetted
#         if unselect:
#             self.reset = True
#             self.updated = True
#             setattr(self, self.valueName, None)
        
#         # Update Field
#         else:
#             validatedValue = self.validateValue(value)
#             if self.val is not None and validatedValue != self.val or forceUpdate:
#                 setattr(self, self.valueName, validatedValue)
#                 # logging.warning(f"Value of {self.attributeDefinitionId} set to {validatedValue} - updating")
#             else:
#                 logging.info(f"cAtt of {self.attributeDefinitionId} was already {validatedValue} - not updating")
                

#     def addValue(self, value, 
#                  valueName:Literal["selectedValues", "entityReferences"]):
        
#         # ensure that valueNmae exists
#         self.getValueName()
#         if not self.valueName:
#             # logging.warning(f"Using provided default valueName")
#             self.valueName = valueName
        
#         # Update Field

#         assert self.valueName in ["selectedValues", "entityReferences"], f"Adding a value to cAtt is only possible for list Types"
#         if not isinstance(self.val, list):
#             setattr(self, self.valueName, self.validateValue([]))
#         assert isinstance(self.val, list), f"self.value should be list but was {type(self.val).__name__}"
#         assert all([isinstance(listEl, dict) for listEl in self.val]), f"All items in list cAtts should be dicts"
#         if self.valueName == "selectedValues":
#             currentState = set([listEl['id'] for listEl in self.val])
#             currentState.add(value)
#             newValue = [{'id': el} for el in currentState]
#         else:
#             assert "entityId" in value and "entityName" in value, f"entityReferences need to have entityId and entityName"
#             if not value["entityId"] in [entity["entityId"] for entity in self.val]:
#                 newValue = self.val
#                 newValue.append(value)
#             else:
#                 newValue = self.val
        
#         setattr(self, self.valueName, self.validateValue(newValue))
        
        
        
#     def removeValue(self, value, 
#                  valueName:Literal["selectedValues", "entityReferences"]):
        
#         # ensure that valueNmae exists
#         self.getValueName()
#         if not self.valueName:
#             # logging.warning(f"Using provided default valueName")
#             self.valueName = valueName
        
#         # Update Field

#         assert self.valueName in ["selectedValues", "entityReferences"], f"removing a value to cAtt is only possible for list Types"
#         if not isinstance(self.val, list):
#             setattr(self, self.valueName, self.validateValue([]))
#         assert isinstance(self.val, list), f"self.value should be list but was {type(self.val).__name__}"
#         assert all([isinstance(listEl, dict) for listEl in self.val]), f"All items in list cAtts should be dicts"
#         newValue = []
#         key = "id" if self.valueName == "selectedValues" else "entityId"
#         for el in self.val:
#             if el[key] != value:
#                 newValue.append(el)
        
#         setattr(self, self.valueName, self.validateValue(newValue))

#     def hasValue(self, targetValue:Any=None) -> bool:
#         try:
#             if targetValue is None:
#                 return True if self.val is not None else False
#             else:
#                 self.getValueName()
#                 if self.valueName == "selectedValues":
#                     return targetValue in [el['id'] for el in self.getValue(asType=list, default=[])]
#                 elif self.valueName == "entityReferences":
#                     return targetValue in [el['entityId'] for el in self.getValue(asType=list, default=[])]
#                 else: 
#                     return True if self.val == targetValue else False
#         except Exception as e:
#             logging.error(f"catched Error in cAtt.hasValue(): {e}")
#             return False
        

#     @property
#     def val(self):
#         if not self.valueName:
#             self.getValueName()
#         if self.valueName:
#             return getattr(self, self.valueName)
#         return None
            
    
    
#     def validateValue(self, value, ignoreNone:bool=False):
        
#         if value is None and ignoreNone:
#             return None
#         # logging.info("---util.weclapp.CustomAtt->setValue()---")
#         # insert Numbers
#         if self.valueName == "numberValue":
#             if isinstance(value, float):
#                 return str(round(value, 2))
#             assert str(value).replace('.', '').isnumeric(), f"Error in cAtt.setValue(): Given Value ({str(value)} in object {self.setValue}) is not nummeric"
#             return str(value)

#         # insert booleans
#         elif self.valueName == "booleanValue":
#             assert isinstance(value, bool), f"To Update Custom Attribute Value must be bool not {type(value).__name__} "
#             return bool(value)

#         # insert strings
#         elif self.valueName == "stringValue" or self.valueName == "selectedValueId":
#             return str(value)
        
#         # if date is selected
#         elif self.valueName == "dateValue":
#             if isinstance(value, datetime):
#                 value = timeFunctions.localeDatetimeToStr(timestemp=value, to="weclapp")
#             assert isinstance(value, int), 'date needs to be int'
#             return int(value)

#         # select value -> ether by id or by value
#         # elif self.valueName == "selectedValueId":
#         #     if str(value) in self.selectableValues.keys():
#         #         return str(value)
#         #     elif str(value) in self.selectableValues.values():
#         #         return self.getSelectableID(str(value))
#         #     else:
#         #         raise ValueError(f"Error in cAtt.setValue(): Given Value ({str(value)} in object {self.setValue}) not found in Selectable Values")

#         # if entity is selected -> be carefull no validation
#         elif self.valueName == "entityId" or self.valueName == "selectedValueId":
#             return str(value)

#         # Multiselect -> the whole list of dicts needs to be passed!!!
#         elif self.valueName == "selectedValues" or self.valueName == "entityReferences":
#             assert isinstance(value, list), f"Type needs to be list of dicts"
#             for el in value:
#                 assert isinstance(el, dict), f"Type needs to be list of dicts - invalid dict -> perhaps overwrite"
#             return value

#         else:
#             raise ValueError("Error in cAtt.setValue(): Something is seriously wrong")
        
#     def getValue(self, asType:Union[str, dict, int, float, list, set, bool, datetime], 
#                  default=None, 
#                  raiseError:bool=True) -> Any:
        
#         """Get the value of an attribute and convert it to a specified format. If not found used default if specified. If not Possibe: Error

#         Args:
#             asType (Union[str, dict, int, float, list, set, bool, datetime]): The data type to convert the attribute value to.
#             default (Any, optional): The default value to return if the attribute is None. Defaults to None.
#             raiseError (bool, optional): Whether to raise an error if there is an exception. Defaults to True.

#         Raises:
#             ValueError: If the specified data type is not supported.
#             ValueError: If the attribute value is None.
#             Exception: If there is an exception and `raiseError` is True.

#         Returns:
#             Any: The value of the attribute in the specified format.
#         """
        
#         try:
#             val = self.val
#             if val is None and default is not None: 
#                 val = default
                
#             if val is not None:  
#                 if asType == str:
#                     return str(val)
                
#                 elif asType == dict:
#                     return dict(val)
                
#                 elif asType == int:
#                     return int(float(val))
                
#                 elif asType == float:
#                     return float(val)
                
#                 elif asType == bool:
#                     return bool(val)
                
#                 elif asType == list:
#                     return list(val)
                
#                 elif asType == set:
#                     return set(val)
                
#                 elif asType == datetime:
#                     return timeFunctions.parseLocalizedDatetimes(val)
                
#                 else:
#                     raise ValueError(f"Given Type {asType} not found")
#             else:
#                 raise ValueError(f"Value of {self.attributeDefinitionId} was None")
#         except Exception as e:
#             logging.error(e)
#             if raiseError:
#                 raise e
#             return default
        
#     def __setattr__(self, name, value):
#         # print(self.valueName, getattr(self, str(self.valueName)), name)
#         if self.valueName and name == self.valueName:
#             self.updated = True
#         return super().__setattr__(name, value)
        
#     def getUpdateDict(self, updateType:Literal['full', 'used']='used'):
#         self.getValueName()
#         if self.updated or updateType == 'full': 
#             answer=  {"attributeDefinitionId": self.attributeDefinitionId}
#             if not self.reset and self.valueName:
#                 answer[self.valueName] = self.val
#             return answer
#         return None
    
#     def updateWeclapp(self, entityName:str, 
#                         entityId:str, 
#                         value:Any, 
#                         valueName:Literal["selectedValueId", "stringValue", "booleanValue", "dateValue", "selectedValues", "entityId", "entityReferences", "numberValue"]) -> dict:
#         self.setValue(value=value,
#                       valueName=valueName)
#         body = {"customAttributes": [self.getUpdateDict()]}
#         return weclapp.updateWeclapp(entityName=entityName, entityId=entityId, body=body)