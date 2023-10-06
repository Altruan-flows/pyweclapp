from typing import *


class CreationBluePrint:
    
    def addCAtt(self, attId:str, attValue, attValueName:Literal["booleanValue", "selectedValueId", "stringValue", "numberValue"]):
        assert hasattr(self, "customAttributes"), f"Custom Attributes must be initialized"
        if attValue != None:
            self.customAttributes.append(
                {
                    "attributeDefinitionId": str(attId),
                    str(attValueName): attValue
                }
            )
        
    def to_dict(self):
        data_dict = {}
        for key, value in self.__dict__.items():
            if value is not None and not callable(value):
                data_dict[key] = value

        return data_dict