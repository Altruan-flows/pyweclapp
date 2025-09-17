"""Module for generating and managing custom attributes (CAT) for Weclapp entities."""

import logging
import re
import unicodedata
import json
import os
from typing import Tuple, List
from .custom_attribute_class import CustomAttributeClass
from ..weclapp import Weclapp
from . import config


class CustomAttributeGenerator:
    """Generator for custom attributes classes of Weclapp entities.
    Args:
        entity_name (str): The name of the Weclapp entity for which to generate
            custom attributes.
        target_directory (str): The directory where the generated files will
            be saved.
    Usage:
        1. Create an instance of CustomAttributeGenerator with the entity
        name and target directory.
        2. Call the main method to generate the custom attributes.
        3. If necessary, create json file named "special_attributes.json"
        in the target directory to assign names to system attributes
        (attributes that are not created by the user). Do this before
        running the generator.
        4. Import CustomAttributes class from __init__.py to access custom
        attributes of all Weclapp entities. Or import the specific
        custom attribute class for the entity you are interested in.
    """

    def __init__(self, target_directory: str):
        self.target_directory = target_directory
        self.weclapp = Weclapp()
        self.collected_custom_attributes: List[CustomAttributeClass] = []
        self.special_attributes = self.load_special_attributes()

    def load_special_attributes(self) -> dict:
        """Loads the special attributes from a JSON file.
        This file contains mappings of custom attribute IDs to their names.
        If the file does not exist, it returns an empty dictionary.
        """
        os.makedirs(self.target_directory, exist_ok=True)

        if not os.path.exists(f"{self.target_directory}/{config.STATIC_IDS_JSON_FILE}"):
            logging.warning(
                "File %s not found in %s. Provide the file to assign names to "
                "system attributes.",
                config.STATIC_IDS_JSON_FILE,
                self.target_directory,
            )
            return {}

        with open(
            f"{self.target_directory}/{config.STATIC_IDS_JSON_FILE}",
            "r",
            encoding="utf-8",
        ) as f:
            return dict(json.load(f))

    def main(self) -> None:
        """Main method to run the custom attribute generator."""
        self.collect_custom_attributes()
        custom_attributes_json, file_content = self.construct_file_content()
        self.save_files(custom_attributes_json, file_content)

    def collect_custom_attributes(self):
        """Finds the default custom attributes for the given entity and adds them to the set"""
        custom_attributes_definitions = self.retrieve_custom_attributes()
        for attribute_dict in custom_attributes_definitions:
            cat = self.setup_custom_attribute_definition(attribute_dict)
            self.collected_custom_attributes.append(cat)

    def retrieve_custom_attributes(self) -> Weclapp:
        """Returns a list of all active custom attribute definitions from Weclapp."""
        attributes = []
        for custom_attribute in self.weclapp.iterator(
            entity_name="customAttributeDefinition",
            query=config.ATTRIBUTE_QUERY,
            page_size=1000,
        ):
            attributes.append(custom_attribute)

        return attributes

    def setup_custom_attribute_definition(
        self, attribute_dict: dict
    ) -> CustomAttributeClass:
        """Fetches the custom attribute definition from Weclapp, transforms the
        data to Python friendly format and returns a CustomAttributeClass instance."""
        attr_key = (
            attribute_dict["attributeKey"]
            if attribute_dict["id"] not in self.special_attributes
            else self.special_attributes[attribute_dict["id"]]
        )
        attr_key = self.to_python_variable(attr_key)
        attr_type = attribute_dict["attributeType"]
        group_name = attribute_dict.get("groupName", config.DEFAULT_GROUP_NAME).strip()

        selectable_values = {}
        if "selectableValues" in attribute_dict and attribute_dict["selectableValues"]:
            for value in attribute_dict["selectableValues"]:
                name = value["value"].replace("___", "_").strip()
                match = re.search(r"\((.*?)\)", name)
                if match:
                    name = match.group(1)
                name = self.to_python_variable(name)
                selectable_values[name] = value["id"]

        return CustomAttributeClass(
            group_name=group_name,
            attr_key=attr_key,
            attr_id=attribute_dict["id"],
            attr_type=attr_type,
            selectable_values=selectable_values,
        )

    def to_python_variable(self, raw_string: str) -> str:
        """Converts a raw string to a Python variable name."""
        # Normalize unicode (e.g., ä -> a)
        s = (
            unicodedata.normalize("NFKD", raw_string)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
        # Replace spaces and slashes with underscores
        s = re.sub(r"[ /]", "_", s)
        # Remove any character that is not a letter, number, or underscore
        s = re.sub(r"\W", "", s)
        # Ensure it doesn't start with a number
        if s and s[0].isdigit():
            s = "_" + s
        return s.lower()

    def construct_file_content(self) -> Tuple[str, dict]:
        """Constructs the python file content and the JSON data for the custom attributes."""
        custom_attributes_json = {}
        file_content = (
            '"""Automatically generated file for Weclapp custom attributes."""\n\n'
            "import json\n"
            "from types import SimpleNamespace\n\n\n"
            "class CustomAttributes:\n"
        )
        file_content += '    """Class to handle Weclapp custom attributes."""\n'
        file_content += (
            "    def __init__(self, data: dict = None):\n"
            "        if data is None:\n"
            "            with open(\n"
            f'                "{self.target_directory}/{config.JSON_DATA_FILE_NAME}'
            '.json", "r", encoding="utf-8"\n'
            f"            ) as file:\n"
            f"                data = json.load(file)\n\n"
            f"        for key, value in data.items():\n"
            f"            setattr(self, key, SimpleNamespace(**value))\n"
        )

        previous_group_name = None
        for custom_attribute in sorted(
            self.collected_custom_attributes, key=lambda x: x.group_name
        ):
            if previous_group_name != custom_attribute.group_name:
                previous_group_name = custom_attribute.group_name
                file_content += "\n"
                file_content += f"        # {custom_attribute.group_name}\n"

            custom_attributes_json[custom_attribute.attr_key] = (
                custom_attribute.to_dict()
            )
            file_content += custom_attribute.generate_python_line()

        return custom_attributes_json, file_content

    def save_files(self, custom_attributes_json: dict, file_content: str) -> None:
        """Saves the generated custom attributes JSON and Python file to the
        target directory."""
        os.makedirs(
            f"{self.target_directory}/{config.JSON_DATA_FILE_NAME}", exist_ok=True
        )

        with open(
            f"{self.target_directory}/{config.JSON_DATA_FILE_NAME}.json",
            "w+",
            encoding="utf-8",
        ) as f:
            json.dump(custom_attributes_json, f, indent=4)

        with open(
            f"{self.target_directory}/__init__.py",
            "w+",
            encoding="utf-8",
        ) as f:
            f.write(file_content)
