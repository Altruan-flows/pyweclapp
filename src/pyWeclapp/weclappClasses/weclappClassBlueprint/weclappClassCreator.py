import logging
from pyWeclapp import weclapp
import os
from typing import Literal
from . import config


class Swagger:
    def __init__(self):
        self.swagger = weclapp.GET(entityName="meta/openapi.json")
        self.entities = [
            key for key in self.swagger["paths"].keys() if key.endswith("/id/{id}")
        ]
        self.schema = {}
        self.refKey = "$ref"

    def getEntity(self, entityName: str) -> dict:
        """returns the entity of a given entityName reconstructed from its opanApi doc
        - e.g. 'salesOrder'"""
        entityNameRef = self.getSchemaRef(entityName)
        return self.getProperties(entityNameRef)

    def getSchemaRef(self, entityName) -> str:
        """returns the reference to a schema of a given entity
        - e.g. '#/components/schemas/salesOrder'"""
        toSearch = f"/{entityName}/id/{'{id}'}"
        ref = self.swagger["paths"][toSearch]["get"]["responses"]["200"]["content"][
            "application/json"
        ]["schema"][self.refKey]
        return ref

    def getComponent(self, schemaRef: str):
        """returns the component of a given schemaRef
        - e.g. 'salesOrder'"""
        "#/components/schemas/salesOrder"
        if schemaRef.startswith("#/components/schemas/"):
            ref = schemaRef.split("/")[-1]
            intermediate = self.swagger["components"]["schemas"][ref]
            if "allOf" in intermediate:
                return intermediate["allOf"]
            else:
                return [intermediate]

        else:
            raise ValueError("schemaRef must start with '#/components/schemas/'")

    def getProperties(self, schemaRef: dict) -> dict:
        """returns a dict of all properties of a given entity"""
        customSchema = {}
        for subSchema in self.getComponent(schemaRef):
            if "properties" in subSchema:
                for key, val in subSchema["properties"].items():
                    if val.get("type") == "array":
                        # {
                        # 'orderItems': {
                        #     'items': {'$ref': '#/components/schemas/salesOrderItem'},
                        #     'type': 'array'
                        #     }
                        # }
                        if "items" in val:
                            if self.refKey in val["items"]:

                                customSchema[key] = [
                                    self.getProperties(val["items"][self.refKey])
                                ]
                            else:
                                customSchema[key] = []
                        else:
                            customSchema[key] = []
                    elif self.refKey in val:
                        customSchema[key] = self.getProperties(val[self.refKey])
                    else:
                        if val.get("type") == "string":
                            customSchema[key] = "string"
                        elif val.get("type") == "integer":
                            customSchema[key] = 999
                        elif val.get("type") == "boolean":
                            customSchema[key] = False
                        else:
                            raise ValueError(f"Unknown type {val.get('type')}")
            elif self.refKey in subSchema:
                customSchema.update(self.getProperties(subSchema[self.refKey]))

            elif "enum" in subSchema:
                allowedValues = subSchema["enum"]
                allowedValues = [f'"{el}"' for el in allowedValues]
                return f'Literal[{", ".join(allowedValues)}]'
        return customSchema


class WeclappClassCreator:
    def __init__(
        self,
        entityName: Literal["salesOrder", "shipment", "contract", "article", "etc."],
        targetDirectory: str,
        entity: dict = None,
        exampleEntityId: str = None,
    ):
        """Sets up the WeclappClassCreator
            - enityName: the name of the entity to be generated
            - targetDirectory: the directory where the file should be saved
            - entity: Optional a dictionaly of the entity to be generated (first
            priority) -> Not Recomended
            - exampleEntityId: Optional an exampleEntityId to be used to get the
            entity from weclapp (second priority) -> Recomended for inoffical
            API entities
            - else: if neither entity nor exampleEntityId is given the entity
            will be generated from the openApi swagger (third priority) ->
            Recomended for official API entities

        After initialization call createPythonFile() to generate the file
        """
        if entity is not None:
            self.entity = entity
        elif exampleEntityId is None:
            self.entity = Swagger().getEntity(entityName) if entity is None else entity
        else:
            self.entity = (
                weclapp.GET(entityName, exampleEntityId, query={"serializeNulls": ""})
                if entity is None
                else entity
            )
        self.entityName = entityName
        self.targetDirectory = targetDirectory
        self.classTemplates = []

    def capitalize(self, string: str):
        """Capitalizes the first letter of a given string"""
        return string[:1].upper() + string[1:]

    def createclassTemplates(self, entityName: str, entity: dict) -> str:
        """Generates the python class code string for a given entity"""

        # create ClassName
        className = self.capitalize(entityName)
        fileContent = f"class {className}(Blueprint):\n"
        itemsName = None

        # create Class Attributes
        for key, value in entity.items():
            # handle Custom Attributes
            if key == "customAttributes":
                fileContent += f"\t{key}: List[WeclappMetaData] = []\n"

            # Handle List Items
            elif isinstance(value, list):
                if len(value) > 0:
                    try:
                        childName = self.createclassTemplates(key, value[0])
                        fileContent += f"\t{key}: List[{childName}] = []\n"
                    except AttributeError as e:
                        logging.warning(
                            f"Could not parse {key} of {entityName} -> {e} => Type hinting not available ()"
                        )
                        fileContent += f"\t{key}: list = [] # could not be parsed\n"
                else:
                    fileContent += f"\t{key}: list = []\n"

                if key == config.ITEMS_NAMES.get(entityName, None):
                    itemsName = f'"{key}"'

            # handle nested entities
            elif isinstance(value, dict):
                childName = self.createclassTemplates(key, value)
                fileContent += f"\t{key}: {childName} = {childName}.fromBlank()\n"

            # handle simple attributes
            else:
                attributeType = type(value)
                if attributeType.__name__ == "NoneType":
                    estimatedType = "int" if "date" in str(key).lower() else "str"
                    logging.warning(
                        f"Attribute {key} of {entityName} is NoneType -> "
                        f"estimating type as {estimatedType} -> please check manually"
                    )
                    fileContent += (
                        f"\t{key}:{estimatedType} = None # type Estimated as str\n"
                    )
                else:
                    relevantType = (
                        value
                        if str(value).startswith("Literal")
                        else attributeType.__name__
                    )  # for items generated from openApi swagger this can be a preprocessed Literal
                    if (
                        key in config.ALWAYS_REQUIRED
                    ):  # or str(value) == str(value).upper(): -> doesnot work :(
                        fileContent += f"\t{key}: Union[{relevantType}, None]\n"
                    else:
                        fileContent += f"\t{key}: Union[{relevantType}, None] = None\n"

        # create AutomationData
        fileContent += "\t# AutomationData\n"
        fileContent += f"\tITEMS_NAME: ClassVar[str] = {itemsName}\n"
        self.classTemplates.append(fileContent)
        return className

    def createPythonFile(self):
        """Main function to generate the python file"""
        if not os.path.exists(self.targetDirectory):
            os.makedirs(self.targetDirectory)

        # create and join all classTemplates
        _ = self.createclassTemplates(self.entityName, self.entity)
        fileContent = config.STATIC_IMPORTS_MODEL_FILES
        for classTemplate in self.classTemplates:
            fileContent += classTemplate
            fileContent += "\n\n"

        # Save the file
        fileName = f"{self.entityName}_Model"
        with open(f"{self.targetDirectory}/{fileName}.py", "w+") as file:
            file.write(fileContent)

        # update init file
        self.updateInitFile(fileName)

    def updateInitFile(self, fileName: str):
        """Imports the generated entity to the __init__.py file of the targetDirectory"""
        initPath = os.path.join(self.targetDirectory, config.INIT_FILE_NAME)
        if not os.path.exists(initPath):
            with open(initPath, "w+") as file:
                file.write("")

        # read current state
        currentImports = []
        with open(initPath, "r+") as file:
            for line in file.readlines():
                if line.startswith("from ."):
                    currentImports.append(line.strip("\n"))

            if not any(fileName in line for line in currentImports):
                other = (
                    ", " + self.capitalize(config.ITEMS_NAMES[self.entityName])
                    if config.ITEMS_NAMES.get(self.entityName, None) is not None
                    else ""
                )
                currentImports.append(
                    f"from .{fileName} import {self.capitalize(self.entityName)}{other}"
                )

        # save files
        with open(initPath, "w+") as file:
            currentImports.insert(0, config.STATIC_IMPORTS_INIT)
            currentImports.insert(0, "# dynamic File please do not edit\n")
            content = "\n".join(currentImports)
            file.write(content)
