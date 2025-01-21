import logging
import re
from .. import weclapp
from . import config


class KITTY_Generator:
    def __init__(self, groupName, catName, catId, catType, selectableValues):
        self.groupName = groupName
        self.catName = catName
        self.catId = catId
        self.catType = catType
        self.selectableValues: dict = selectableValues

    @staticmethod
    def getValueName(attributeType) -> str:
        """Takes a weclapp attributeType and returns the corresponding Python value name"""
        return config.VALUE_NAME_MAPPING[attributeType]

    @staticmethod
    def getFieldName(input_string: str) -> str:
        """Takes a string and returns a valid Python variable name
        - Text in barckets will be extracted and used as the variable name"""
        # Ensure the input string is not empty
        if not isinstance(input_string, str) or not len(input_string) > 0:
            raise AssertionError("Input String is empty")

        # Use a regular expression to extract the value inside parentheses
        match = re.search(r"\((.*?)\)", input_string)
        if match:
            # If there's a match, take the value inside the parentheses
            extracted_string = match.group(1)
        else:
            # Otherwise, use the entire input string
            extracted_string = input_string

        # Use a regular expression to keep only valid Python variable characters
        valid_string = re.sub(r"[^a-zA-Z0-9_]", "", extracted_string)

        # Ensure the resulting string starts with a valid character
        if not valid_string or not (
            valid_string[0].isalpha() or valid_string[0] == "_"
        ):
            return config.DEFAULT_FIRST_CHAR + valid_string
        return valid_string

    @classmethod
    def fromWeclapp(cls, catId: str, catName: str = None, groupNamePrefix: str = None):
        """Returns a KITTY_Generator object from a weclapp customAttributeDefinition"""
        groupNamePrefix = groupNamePrefix or ""
        attribute = weclapp.GET(entity_name="customAttributeDefinition", entity_id=catId)

        # parse selectableValues
        selectableValues = {}
        for el in attribute.get("selectableValues", []):
            try:
                name = cls.getFieldName(el["value"]).replace("___", "_")
                selectableValues[name] = el["id"]
            except AssertionError as e:
                logging.warning(
                    f"Could not parse selectableValues of {catId}: AssertionError: {e}"
                )

        groupName = groupNamePrefix + attribute.get(
            "groupName", config.DEFAULT_GROUP_NAME
        )
        # init Attribute
        return cls(
            groupName=groupName,
            catName=(
                cls.getFieldName(attribute["attributeKey"])
                if catName is None
                else catName
            ),
            catId=catId,
            catType=cls.getValueName(attribute["attributeType"]),
            selectableValues=selectableValues,
        )

    def to_dict(self) -> dict:
        """returns a copy of the namedTuple attributes as a dict"""
        new = self.selectableValues.copy()
        new["id"] = self.catId
        new["valueName"] = self.catType
        return new

    def getPythonCode(self) -> str:
        """returns the variable setup for a single kitty as a string
        - Format: self.VAR = namedtuple("VAR", [key1, key2, ...])(**data["VAR"])"""
        keys = config.BASE_ATTRIBUTES + list(self.selectableValues.keys())
        keystring = ", ".join([f'"{key2}"' for key2 in keys])

        catNameWithSpacing = self.catName + " " * (
            config.DEFAULT_CAT_INDENT_SPACES - len(self.catName)
        )
        spacesBetweenNameAndSchema = " " * (
            config.DEFAULT_CAT_INDENT_SPACES - len(self.catName)
        )
        finalString = (
            f'\t\tself.{catNameWithSpacing}= namedtuple("{self.catName}", {spacesBetweenNameAndSchema}[{keystring}])'
        )
        finalString += f'(**data["{self.catName}"]) # {self.catId}\n'
        return finalString
