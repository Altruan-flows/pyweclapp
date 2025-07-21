"""Module to create Weclapp Class Blueprints."""

import logging
import os
from ...weclapp import Weclapp
from . import config


class WeclappClassCreator:
    """Class to create Weclapp Class Blueprints.
        Args:
            entity_name (str): Name of the entity to create a class for.
            target_directory (str): Directory where the class file should be created.
            entity_dict (dict, optional): Dictionary containing the entity data. If not provided,
                it will be fetched from the Weclapp API.

        After initialization call create_python_file() to generate the class file.
        """
    def __init__(
        self,
        entity_name: str,
        target_directory: str,
        entity_dict: dict = None,
    ):
        weclapp = Weclapp()
        if entity_dict is not None:
            self.entity = entity_dict
        else:
            entities = weclapp.get(entity_name, query={"serializeNulls": ""})
            if entities and isinstance(entities, list) and len(entities) > 0:
                self.entity = entities[0]
            else:
                raise ValueError(
                    f"Could not find entity {entity_name} in Weclapp API. "
                    "Please check the entity name or provide a valid entity dictionary."
                )
        self.entity_name = entity_name
        self.target_directory = target_directory
        self.class_templates = []

    def capitalize(self, string: str) -> str:
        """Capitalizes the first letter of a given string"""
        return string[:1].upper() + string[1:]

    def create_class_templates(self, entity_name: str, entity: dict) -> str:
        """Generates the python class code string for a given entity"""

        class_name = self.capitalize(entity_name)
        file_content = f"class {class_name}(Blueprint):\n"
        items_name = None

        for key, value in entity.items():
            if key == "customAttributes":
                file_content += f"\t{key}: List[WeclappMetaData] = []\n"

            elif isinstance(value, list):
                if len(value) > 0:
                    try:
                        child_name = self.create_class_templates(key, value[0])
                        file_content += f"\t{key}: List[{child_name}] = []\n"
                    except AttributeError as e:
                        logging.warning(
                            "Could not parse %s of %s -> %s => Type hinting not available ()",
                            key,
                            entity_name,
                            e,
                        )
                        file_content += (
                            f"\t{key}: list = []  # List could not be parsed\n"
                        )
                else:
                    file_content += f"\t{key}: list = []\n"

                if key == config.ITEMS_NAMES.get(entity_name, None):
                    items_name = f'"{key}"'

            elif isinstance(value, dict):
                child_name = self.create_class_templates(key, value)
                file_content += f"\t{key}: {child_name} = {child_name}.fromBlank()\n"

            else:
                attribute_type = type(value)
                if attribute_type.__name__ == "NoneType":
                    estimated_type = "int" if "date" in str(key).lower() else "str"
                    logging.warning(
                        "Attribute %s of %s is NoneType -> estimating type "
                        "as %s -> please check manually",
                        key,
                        entity_name,
                        estimated_type,
                    )
                    file_content += (
                        f"\t{key}:{estimated_type} = None  # Type estimated\n"
                    )
                else:
                    relevant_type = attribute_type.__name__
                    if key in config.MANDATORY_FIELDS:
                        file_content += f"\t{key}: Union[{relevant_type}, None]\n"
                    else:
                        file_content += (
                            f"\t{key}: Union[{relevant_type}, None] = None\n"
                        )

        file_content += "\t# AutomationData\n"
        file_content += f"\tITEMS_NAME: ClassVar[str] = {items_name}\n"
        self.class_templates.append(file_content)
        return class_name

    def create_python_file(self):
        """Main function to generate the python file."""
        if not os.path.exists(self.target_directory):
            os.makedirs(self.target_directory)

        self.create_class_templates(self.entity_name, self.entity)
        file_content = config.STATIC_IMPORTS_MODEL_FILES
        for class_template in self.class_templates:
            file_content += class_template
            file_content += "\n\n"

        file_name = f"{self.entity_name}_model"
        with open(f"{self.target_directory}/{file_name}.py", "w+", encoding="utf-8") as file:
            file.write(file_content)

        self.update_init_file(file_name)

    def update_init_file(self, file_name: str):
        """Imports the generated entity to the __init__.py file of the target
        directory."""
        init_path = os.path.join(self.target_directory, config.INIT_FILE_NAME)
        if not os.path.exists(init_path):
            with open(init_path, "w+", encoding="utf-8") as file:
                file.write("")

        current_imports = []
        with open(init_path, "r+", encoding="utf-8") as file:
            for line in file.readlines():
                if line.startswith("from ."):
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

        with open(init_path, "w+", encoding="utf-8") as file:
            current_imports.insert(0, config.STATIC_IMPORTS_INIT)
            current_imports.insert(
                0, '"""Dynamically created file. Please do not edit."""\n'
            )
            content = "\n".join(current_imports)
            file.write(content)
