from .. import weclapp
import logging
import re


class CITTY_Generator:
    def __init__(self, groupName, catName, catId, catType, selectableValues):
        self.groupName = groupName
        self.catName = catName
        self.catId = catId
        self.catType = catType
        self.selectableValues:dict = selectableValues
    
    @staticmethod
    def getValueName(attributeType) -> str:
        a = {"MULTISELECT_LIST": "selectedValues",
            "INTEGER": "numberValue",
            "DECIMAL": "numberValue",
            "LIST": "selectedValueId",
            "BOOLEAN": "booleanValue",
            "STRING": "stringValue",
            "LARGE_TEXT": "stringValue",
            "DATE": "dateValue",
            "ENTITY": "entityId",
            "REFERENCE": "entityReferences",
            "URL": "stringValue"
        }
        return a[attributeType]
    
    # @staticmethod
    # def getFieldName(input_string) -> str:
    #     # Use a regular expression to match non-alphanumeric characters (except underscore)
    #     # and replace them with an underscore '_'
    #     assert len(input_string) > 0, "Input String is empty"
    #     modified_string = re.sub(r'[^a-zA-Z0-9_]', '', input_string)
        
    #     # Use another regular expression to extract the value inside parentheses
    #     match = re.search(r'\((.*?)\)', input_string)
    #     returnString = match.group(1) if match else modified_string
    #     if not returnString or not returnString[0].isalpha():
    #         return "X" + returnString
    #     return returnString
    
    @staticmethod
    def getFieldName(input_string) -> str:
        # Ensure the input string is not empty
        assert len(input_string) > 0, "Input String is empty"
        
        # Use a regular expression to extract the value inside parentheses
        match = re.search(r'\((.*?)\)', input_string)
        if match:
            # If there's a match, take the value inside the parentheses
            extracted_string = match.group(1)
        else:
            # Otherwise, use the entire input string
            extracted_string = input_string
        
        # Use a regular expression to keep only valid Python variable characters
        valid_string = re.sub(r'[^a-zA-Z0-9_]', '', extracted_string)
        
        # Ensure the resulting string starts with a valid character
        if not valid_string or not (valid_string[0].isalpha() or valid_string[0] == '_'):
            return "X" + valid_string
        return valid_string







        
    @classmethod
    def fromWeclapp(cls, catId:str, catName:str=None):
        attribute = weclapp.GET(entityName=f"customAttributeDefinition", entityId=catId)
        
        # parse selectableValues
        selectableValues = {}
        for el in attribute.get("selectableValues", []):
            try:
                name = cls.getFieldName(el['value']).replace('___', '_')
                selectableValues[name] = el['id']
            except:
                logging.warning(f"Could not parse selectableValues of {catId}")
            
        # init Attribute
        return cls(groupName=   attribute.get('groupName', 'other'),
                    catName=    cls.getFieldName(attribute['attributeKey']) if catName is None else catName,
                    catId=      catId,
                    catType=    cls.getValueName(attribute['attributeType']),
                    selectableValues = selectableValues)
        
        
    def getDict(self) -> dict:
        new = self.selectableValues.copy()
        new["id"] = self.catId
        new["valueName"] = self.catType
        return new
        
    def getPythonCode(self) -> str:
        keys = ["id", "valueName"] + list(self.selectableValues.keys())
        keystring = ", ".join([f'"{key2}"' for key2 in keys])
        return f'\t\tself.{self.catName + " " * (25 - len(self.catName))}= namedtuple("{self.catName}", {" " * (25 - len(self.catName))}[{keystring}])(**data["{self.catName}"]) # {self.catId}\n'

