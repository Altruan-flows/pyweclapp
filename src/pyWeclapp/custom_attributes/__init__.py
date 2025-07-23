"""Module for generating and managing custom attributes (CAT) for Weclapp entities."""

import logging
import re
import json
import os
from typing import Tuple, List, Union
from .custom_attribute_class import CustomAttributeClass
from ..weclapp import Weclapp
from . import config


class CustomAttributeGenerator:
    def __init__(self, entity_name: str, target_directory: str):
        """Creates or updated a CAT Class for a givern weclapp entity in a predefined directory
        it will use the
            - entityName:       as the name of the weclapp entity
            - entityId:         as the id of the weclapp entity
            - targetDirectory   desired directory to save the file in
            - StaticOrExcludedIDs.json File - Schema: {catId: catName}; Method
            to manually rename or exclude (catName=null) a cat
            - cat_Settings.py File: File to manually save other constants related to cats.
        """
        self.entity_name = entity_name
        self.target_directory = target_directory
        # self.custom_attributes = set()
        # self.default_custom_attributes = set()
        self.collected_custom_attributes: List[CustomAttributeClass] = []
        self.special_attributes = self.load_special_attributes()

        self.main()

    def load_special_attributes(self) -> dict:
        """Loads the special attributes from a JSON file.
        This file contains mappings of custom attribute IDs to their names.
        If the file does not exist, it returns an empty dictionary.
        """
        if not os.path.exists(self.target_directory):
            os.mkdir(self.target_directory)

        if not os.path.exists(
            f"{self.target_directory}/{config.STATIC_IDS_JSON_FILE}"
        ):
            logging.warning(
                f"File {config.STATIC_IDS_JSON_FILE} not found in {self.target_directory}."
                f" Provide the file to assign names to system attributes"
            )
            return {}

        with open(
            f"{self.target_directory}/{config.STATIC_IDS_JSON_FILE}", "r"
        ) as f:
            return dict(json.load(f))
    
    def save(self, custom_attributes_json: dict, file_content: str) -> None:
        if not os.path.exists(self.target_directory):
            os.mkdir(self.target_directory)

        if not os.path.exists(f"{self.target_directory}/{config.JSON_DATA_FOLDER_NAME}"):
            os.mkdir(f"{self.target_directory}/{config.JSON_DATA_FOLDER_NAME}")

        with open(
            f"{self.target_directory}/{config.JSON_DATA_FOLDER_NAME}/{self.entity_name}.json",
            "w+",
        ) as f:
            json.dump(custom_attributes_json, f, indent=4)

        # pathToAllCatData = f"{self.target_directory}/{config.JSON_DATA_FOLDER_NAME}/{config.FILENAME_ALL_CAT_DATA}.json"
        # if os.path.exists(pathToAllCatData):
        #     # read all other cat data
        #     with open(pathToAllCatData, "r") as f:
        #         data = dict(json.load(f))
        #         data.update(custom_attributes_json)
        #         totalJson = data
        # else:
        #     totalJson = custom_attributes_json

        # with open(pathToAllCatData, "w+") as f:
        #     json.dump(totalJson, f, indent=4)

        with open(f"{self.target_directory}/cat_{self.name}.py", "w+") as f:
            f.write(file_content)
    
    def construct_file_content(self) -> Tuple[str, dict]:
        """Constructs the python file content and the JSON data for the custom attributes."""
        custom_attributes_json = {}
        file_content = "import json\n"
        file_content += "from collections import namedtuple\n\n\n"
        # self.file += f"from . import {config.FILENAME_CAT_SETTINGS}\n"

        file_content += (
            f"class {self.name}CustomAttributes:\n\n"
        )
        file_content += (
            '    @staticmethod\n    def is_namedtuple(obj):\n        try:\n            '
            'return isinstance(obj, tuple) and hasattr(obj, "_fields")\n        '
            'except:\n            return False\n\n'
        )
        file_content += (
            f'    def __init__(self, data:dict=None):\n        super().__init__()\n        '
            f'if data is None:\n            with open("{self.target_directory}/'
            f'{config.JSON_DATA_FOLDER_NAME}/{self.entity_name}.json", "r") as '
            'f:\n                data = json.load(f)\n\n'
        )

        previous_group_name = None
        for custom_attribute in sorted(self.collected_custom_attributes, key=lambda x: x.group_name):
            if not isinstance(custom_attribute, CustomAttributeClass):
                raise AssertionError(f"Expected CustomAttributeClass, got {type(custom_attribute)}")

            if previous_group_name != custom_attribute.group_name:
                previous_group_name = custom_attribute.group_name
                file_content += "\n"
                file_content += f"        # {custom_attribute.group_name}\n"

            custom_attributes_json[custom_attribute.attr_key] = custom_attribute.to_dict()
            file_content += custom_attribute.generate_python_line()
        
        return custom_attributes_json, file_content
    
    def setup_custom_attribute_definition(self, attribute_id: str) -> CustomAttributeClass:
        """Fetches the custom attribute definition from Weclapp, transforms the
        data to Python friendly format and returns a CustomAttributeClass instance."""
        attribute_dict = Weclapp().get(entity_name="customAttributeDefinition", entity_id=attribute_id)

        attr_key = attribute_dict["attributeKey"] if attribute_id not in self.special_attributes else self.special_attributes[attribute_id]
        attr_type = attribute_dict["attributeType"]

        selectable_values = {}
        if "selectableValues" in attribute_dict and attribute_dict["selectableValues"]:
            for value in attribute_dict["selectableValues"]:
                name = value["value"].replace("___", "_").strip()
                match = re.search(r"\((.*?)\)", name)
                if match:
                    name = match.group(1)
                selectable_values[name] = value["id"]
        
        return CustomAttributeClass(
            group_name=attribute_dict.get("groupName", config.DEFAULT_GROUP_NAME),
            attr_key=attr_key,
            id=attribute_dict["id"],
            attr_type=attr_type,
            selectable_values=selectable_values
        )

    def get_weclapp_entity(self) -> Weclapp:
        """Returns custom attributes of the given entity from Weclapp."""
        entities = Weclapp().get(entity_name=self.entity_name, query=config.ENTITY_QUERY, as_type=list)
        if not entities:
            raise ValueError(f"No entities found for {self.entity_name}")
        entity = entities[0]
        if "customAttributes" not in entity:
            raise ValueError(f"No custom attributes found for {self.entity_name}")
        return entity["customAttributes"]

    def collect_entity_custom_attributes(self):
        """Finds the default custom attributes for the given entity and adds them to the set"""
        list_of_default_attributes = self.get_weclapp_entity()
        custom_attributes_ids = [attr["attributeDefinitionId"] for attr in list_of_default_attributes]
        for attribute_id in custom_attributes_ids:
            cat = self.setup_custom_attribute_definition(attribute_id)
            self.collected_custom_attributes.append(cat)
    
    def main(self) -> None:
        """Main method to run the custom attribute generator."""
        self.collect_entity_custom_attributes()
        custom_attributes_json, file_content = self.construct_file_content()
        self.save(custom_attributes_json, file_content)
        # self.updateSuperClass()

    @property
    def name(self):
        """Returns the name of the class based on the entity name."""
        return self.entity_name[0].upper() + self.entity_name[1:]



    

    

    # def createCatSettings(self):
    #     """creates a cat_Settings.py file if none exists"""
    #     fileContent = "from collections import namedtuple\n\n"
    #     fileContent += "class CAT_Settings:\n"
    #     fileContent += "    def __init__(self, data:dict=None):\n"
    #     fileContent += (
    #         "        # You can place global cat settings here. they will not be modified\n"
    #     )
    #     fileContent += "        pass\n"

    #     if not os.path.exists(
    #         f"{self.target_directory}/{config.FILENAME_CAT_SETTINGS}.py"
    #     ):
    #         with open(
    #             f"{self.target_directory}/{config.FILENAME_CAT_SETTINGS}.py", "w+"
    #         ) as file:
    #             file.write(fileContent)

    # def estimateClassName(self, fileName: str):
    #     return fileName.replace("cat", "CAT")

    # def updateSuperClass(self):

    #     # List all files in the directory
    #     all_files = os.listdir(self.target_directory)

    #     # Filter out files that are not Python files or are the __init__.py file
    #     python_files = [
    #         f
    #         for f in all_files
    #         if f.endswith(".py") and f not in ["__init__.py", "cat.py"]
    #     ]

    #     # Extract names without the .py extension
    #     module_names = [os.path.splitext(f)[0] for f in python_files]

    #     # Generate import statements
    #     import_statements = [f"from . import {module}" for module in module_names]
    #     import_statements.append("import json")
    #     # import_statements.append("import os")

    #     model = ", ".join(
    #         [f"{module}.{self.estimateClassName(module)}" for module in module_names]
    #     )

    #     fileContent = "\n".join(import_statements)
    #     fileContent += "\n# dynamic File please do not edit\n"
    #     fileContent += f"\n\nclass CAT({model}):\n"
    #     fileContent += "    def __init__(self):\n"
    #     fileContent += (
    #         f'        with open("{self.target_directory}/{config.JSON_DATA_FOLDER_NAME}/'
    #         f'{config.FILENAME_ALL_CAT_DATA}.json", "r") as f:\n'
    #     )
    #     fileContent += "            self.data = json.load(f)\n"
    #     fileContent += "        super().__init__(self.data)\n"
    #     fileContent += "\n\n"

    #     with open(f"{self.target_directory}/cat.py", "w+") as file:
    #         file.write(fileContent)

    #     # update Init.py dile
    #     module_names.append("cat")

    #     currentImports = [f"from .{fileName} import *" for fileName in module_names]

    #     with open(f"{self.target_directory}/__init__.py", "w+") as file:
    #         currentImports.insert(0, "# dynamic File please do not edit\n")
    #         file.write("\n".join(currentImports))
