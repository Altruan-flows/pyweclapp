"""Module to create Weclapp Class Blueprints."""

import os
import re
from typing import Any
from ...weclapp import Weclapp
from . import config


class WeclappClassCreator:
    """Class to create Weclapp Class Blueprints.
    Args:
        entity_name (str): Name of the entity to create a class for.
        target_directory (str): Directory where the class file should be created.
        entity_dict (dict, optional): Dictionary containing the entity data. If
            not provided, it will be fetched from the Weclapp API.

    After initialization call create_python_file() to generate the class file.
    """

    def __init__(
        self, entity_name: str, target_directory: str, entity_dict: dict = None
    ):
        if entity_dict is not None:
            self.entity = entity_dict
        else:
            self.entity = self.get_example_entity(entity_name)
        self.entity_name = entity_name
        self.target_directory = target_directory
        self.class_templates = []

    def get_example_entity(self, entity_name: str) -> dict:
        """Fetches an example entity from the Weclapp API to create a class
        blueprint."""
        weclapp = Weclapp()
        entities = weclapp.get(entity_name, query=config.CREATION_QUERY, as_type=list)
        if entities and isinstance(entities, list) and len(entities) > 0:
            return entities[0]

        raise ValueError(
            f"Could not find entity {entity_name} in Weclapp API. "
            "Please check the entity name or provide a valid entity dictionary."
            f"Response: {entities}"
        )

    def create_python_file(self) -> None:
        """Main function to generate the python file."""
        if not os.path.exists(self.target_directory):
            os.makedirs(self.target_directory)

        self.create_class_templates(self.entity_name, self.entity)
        file_content = config.STATIC_IMPORTS_MODEL_FILES

        file_content += "\n\n".join(self.class_templates)

        splitted_entity_name = re.split(r"(?=[A-Z])", self.entity_name)
        file_name = f"{'_'.join(splitted_entity_name).lower()}_model"
        with open(
            f"{self.target_directory}/{file_name}.py", "w+", encoding="utf-8"
        ) as file:
            file.write(file_content)

        self.update_init_file(file_name)

    def create_class_templates(self, entity_name: str, entity: dict) -> str:
        """Generates the python class code string for a given entity"""
        class_name = self.capitalize(entity_name)
        file_content = f"class {class_name}(Blueprint):\n"

        for key, value in entity.items():
            if key == "customAttributes":
                file_content += f"    {key}: List[WeclappMetaData] = []\n"

            elif isinstance(value, list):
                if len(value) > 0 and isinstance(value[0], dict):
                    child_name = self.create_class_templates(key, value[0])
                    file_content += f"    {key}: List[{child_name}] = []\n"
                else:
                    file_content += f"    {key}: list = []\n"

            elif isinstance(value, dict):
                child_name = self.create_class_templates(key, value)
                file_content += f"    {key}: {child_name} = {child_name}()\n"

            else:
                file_content += self.generate_type_hint(value, key)

        self.class_templates.append(file_content)
        return class_name

    def capitalize(self, string: str) -> str:
        """Capitalizes the first letter of a given string"""
        return string[:1].upper() + string[1:]

    def generate_type_hint(self, value: Any, key: str) -> str:
        """Generate type hint for a given value."""
        attribute_type = type(value)
        if attribute_type.__name__ == "NoneType":
            estimated_type = "int" if "date" in str(key).lower() else "str"
            return f"    {key}: Optional[{estimated_type}] = None  # Type estimated\n"
        else:
            relevant_type = attribute_type.__name__
            return f"    {key}: Union[{relevant_type}, None] = None\n"

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

            new_import = f"from .{file_name} import {self.capitalize(self.entity_name)}"
            if not any(new_import in import_line for import_line in current_imports):
                current_imports.append(new_import)

        with open(init_path, "w+", encoding="utf-8") as file:
            current_imports.insert(0, config.INIT_FILE_DOC_STRING)
            content = "\n".join(current_imports) + "\n"
            file.write(content)
