"""Module to create Weclapp Class Blueprints."""
import logging
import os
from typing import List, Union, ClassVar
from pyweclapp.weclapp import Weclapp
from . import config


class Swagger:
    def __init__(self):
        self.swagger = weclapp.GET("meta/openapi.json")
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
        entity_name: str,
        target_directory: str,
        entity_dict: dict = None,
    ):
        """Sets up the WeclappClassCreator
            - enityName: the name of the entity to be generated
            - targetDirectory: the directory where the file should be saved
            - entity: Optional a dictionaly of the entity to be generated (first priority) -> Not Recomended
            - exampleEntityId: Optional an exampleEntityId to be used to get the entity from weclapp (second priority) -> Recomended for inoffical API entities
            - else: if neither entity nor exampleEntityId is given the entity will be generated from the openApi swagger (third priority) -> Recomended for official API entities

        After initialization call createPythonFile() to generate the file
        """
        if entity_dict is not None:
            self.entity = entity_dict
        elif example_entity_id is None:
            self.entity = Swagger().getEntity(entity_name) if entity_dict is None else entity_dict
        else:
            self.entity = (
                weclapp.GET(
                    entity_name, query={"serializeNulls": ""}
                )
                if entity_dict is None
                else entity_dict
            )
        self.entity_name = entity_name
        self.target_directory = target_directory
        self.class_templates = []

    def capitalize(self, string: str) -> str:
        """Capitalizes the first letter of a given string"""
        return string[:1].upper() + string[1:]

    def create_class_templates(self, entity_name: str, entity: dict) -> str:
        """Generates the python class code string for a given entity"""

        # create ClassName
        class_name = self.capitalize(entity_name)
        file_content = f"class {class_name}(Blueprint):\n"
        items_name = None

        # create Class Attributes
        for key, value in entity.items():
            # handle Custom Attributes
            if key == "customAttributes":
                fileContent += f"\t{key}: List[WeclappMetaData] = []\n"

            # Handle List Items
            elif isinstance(value, list):
                if len(value) > 0:
                    try:
                        child_name = self.create_class_templates(key, value[0])
                        file_content += f"\t{key}: List[{child_name}] = []\n"
                    except AttributeError as e:
                        logging.warning(
                            f"Could not parse {key} of {entity_name} -> {e} => Type hinting not available ()"
                        )
                        file_content += f"\t{key}: list = [] # could not be parsed\n"
                else:
                    file_content += f"\t{key}: list = []\n"

                if key == config.ITEMS_NAMES.get(entity_name, None):
                    items_name = f'"{key}"'

            # handle nested entities
            elif isinstance(value, dict):
                child_name = self.create_class_templates(key, value)
                file_content += f"\t{key}: {child_name} = {child_name}.fromBlank()\n"

            # handle simple attributes
            else:
                attribute_type = type(value)
                if attribute_type.__name__ == "NoneType":
                    estimated_type = "int" if "date" in str(key).lower() else "str"
                    logging.warning(
                        f"Attribute {key} of {entity_name} is NoneType -> estimating type as {estimated_type} -> please check manually"
                    )
                    file_content += (
                        f"\t{key}:{estimated_type} = None # type Estimated as str\n"
                    )
                else:
                    relevant_type = (
                        value
                        if str(value).startswith("Literal")
                        else attribute_type.__name__
                    )  # for items generated from openApi swagger this can be a preprocessed Literal
                    if (
                        key in config.ALWAYS_REQUIRED
                    ):  # or str(value) == str(value).upper(): -> doesnot work :(
                        file_content += f"\t{key}: Union[{relevant_type}, None]\n"
                    else:
                        file_content += f"\t{key}: Union[{relevant_type}, None] = None\n"

        # create AutomationData
        file_content += f"\t# AutomationData\n"
        file_content += f"\tITEMS_NAME: ClassVar[str] = {items_name}\n"
        self.class_templates.append(file_content)
        return class_name

    def createPythonFile(self):
        """Main function to generate the python file"""
        if not os.path.exists(self.target_directory):
            os.makedirs(self.target_directory)

        # create and join all classTemplates
        _ = self.create_class_templates(self.entity_name, self.entity)
        file_content = config.STATIC_IMPORTS_MODEL_FILES
        for class_template in self.class_templates:
            file_content += class_template
            file_content += "\n\n"

        # Save the file
        file_name = f"{self.entity_name}_Model"
        with open(f"{self.target_directory}/{file_name}.py", "w+") as file:
            file.write(file_content)

        # update init file
        self.updateInitFile(file_name)

    def updateInitFile(self, file_name: str):
        """Imports the generated entity to the __init__.py file of the targetDirectory"""
        init_path = os.path.join(self.target_directory, config.INIT_FILE_NAME)
        if not os.path.exists(init_path):
            with open(init_path, "w+") as file:
                file.write("")

        # read current state
        current_imports = []
        with open(init_path, "r+") as file:
            for line in file.readlines():
                if line.startswith(f"from ."):
                    current_imports.append(line.strip("\n"))

            if not any(file_name in line for line in current_imports):
                other = (
                    ", " + self.capitalize(config.ITEMS_NAMES[self.entity_name])
                    if config.ITEMS_NAMES.get(self.entity_name, None) is not None
                    else ""
                )
                current_imports.append(
                    f"from .{file_name} import {self.capitalize(self.entity_name)}{other}"
                )

        # save files
        with open(init_path, "w+") as file:
            current_imports.insert(0, config.STATIC_IMPORTS_INIT)
            current_imports.insert(0, "# dynamic File please do not edit\n")
            content = "\n".join(current_imports)
            file.write(content)
