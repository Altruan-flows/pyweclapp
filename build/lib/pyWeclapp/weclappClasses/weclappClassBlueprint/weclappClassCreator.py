from typing import *
import logging
from . import weclapp




class WeclappClassCreator:
    def __init__(self, entityName:Literal["salesOrder", "shipment", "contract", "article", "etc."], expamleEntityId:str, targetDirectory:str, entity:dict=None):
        self.entity = weclapp.GET(entityName, expamleEntityId, query={"serializeNulls": ""}) if entity is None else entity
        self.entityName = entityName
        self.targetDirectory = targetDirectory
        self.itemsNames = {
            "salesOrder": "orderItems",
            "shipment": "shipmentItems",
            "contract": "contractItems",
            "article": "articlePrices",
            "salesInvoice": "salesInvoiceItems"
            } 
        self.classTemplates = []
        self.alwaysRequired = ["id", "version", "active", "createdDate", "lastModifiedDate", "articleType", "priceScaleType", "positionNumber"]
    
    def capitalize(self, string:str):
        return string[:1].upper() + string[1:]
        
    def createclassTemplates(self, entityName:str, entity:dict) -> str:
        className = self.capitalize(entityName)
        fileContent = f"class {className}(BaseModel, Blueprint):\n"   
        itemsName = None
        
        for key, value in entity.items():
            if key == "customAttributes":
                fileContent += f"\t{key}: List[WeclappMetaData] = []\n"
                
            elif isinstance(value, list):
                if len(value) > 0:
                    try:
                        childName = self.createclassTemplates(key, value[0])
                        fileContent += f"\t{key}: List[{childName}] = []\n"
                    except Exception as e:
                        logging.error(e)
                        fileContent += f"\t{key}: list = [] # could not be parsed\n"
                else:
                    fileContent += f"\t{key}: list = []\n"
                        
                if key == self.itemsNames.get(entityName, None):
                    itemsName = f'"{key}"'
                    
            elif isinstance(value, dict):
                childName = self.createclassTemplates(key, value)
                fileContent += f"\t{key}: {childName} = {childName}.fromBlank()\n"
                # fileContent += "{}\n"
                
            else:
                attributeType = type(value)
                if attributeType.__name__ == "NoneType":
                    estimatedType = "int" if "date" in str(key).lower() else "str"
                    logging.warning(f"Attribute {key} of {entityName} is NoneType -> estimating type as {estimatedType} -> please check manually")
                    fileContent += f"\t{key}:{estimatedType} = None # type Estimated as str\n"
                else:
                    if key in self.alwaysRequired or attributeType.__name__ == "bool": # or str(value) == str(value).upper(): -> doesnot work :(
                        fileContent += f"\t{key}: {attributeType.__name__}\n"
                    else:
                        fileContent += f"\t{key}: {attributeType.__name__} = None\n"
        # AutomationData
        fileContent += f"\n\n\n\t# AutomationData\n"
        fileContent += f'\tITEMS_NAME: str = {itemsName}\n'
        fileContent += f"\tUSED_ATTRIBUTES: dict = dict()\n"
        fileContent += f"\t__setattr__ = Blueprint.__setattr__\n\n\n"

        
        fileContent += f"\tdef __init__(self, **kwargs):\n"
        fileContent += f"\t\tBaseModel.__init__(self, **kwargs)\n"
        fileContent += f"\t\tBlueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)\n\n\n\n"
        self.classTemplates.append(fileContent)
        return className
        
        
        
        
        
    def createPythonFile(self):
        fileContent = f"from pyWeclapp.weclappClasses import Blueprint, WeclappMetaData\nfrom pydantic import BaseModel\nfrom typing import *\n\n\n\n"   
        _ = self.createclassTemplates(self.entityName, self.entity)
        
        
        for classTemplate in self.classTemplates:
            fileContent += classTemplate
        
        fileName = f"{self.entityName}_Model"
        with open(f"{self.targetDirectory}/{fileName}.py", "w+") as file:
            file.write(fileContent)
            
        self.updateInitFile(fileName)
    
    
    def updateInitFile(self, fileName:str):
        import os
        
        initPath = f"{self.targetDirectory}/__init__.py"
        currentImports = []
        if os.path.exists(initPath):
            with open(initPath, "r+") as file:
                for line in file.readlines():
                    if line.startswith(f"from ."):
                        currentImports.append(line.strip('\n'))
                        
        if not any(fileName in line for line in currentImports):
            currentImports.append(f"from .{fileName} import *")
            
        with open(f"{self.targetDirectory}/__init__.py", "w+") as file:
            currentImports.insert(0, "# dynamic File please do not edit\n")
            file.write("\n".join(currentImports))
            
                    