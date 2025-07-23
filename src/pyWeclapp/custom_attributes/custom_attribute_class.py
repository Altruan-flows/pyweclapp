"""CustomAttributeClass for handling custom attributes in Weclapp."""

from . import config


class CustomAttributeClass:
    def __init__(self, group_name: str, attr_key: str, id: str, attr_type: str, selectable_values: dict):
        self.group_name = group_name
        self.attr_key = attr_key
        self.id = id
        self.attr_type = attr_type
        self.selectable_values: dict = selectable_values

    def generate_python_line(self) -> str:
        """Generates a Python line of code that creates a namedtuple for the custom attribute.
        The line will be formatted as follows:
        self.VAR = namedtuple("VAR", [key1, key2, ...])(**data["VAR"])
        """
        keys = config.BASE_ATTRIBUTES + list(self.selectable_values.keys())
        keystring = ", ".join([f'"{attribute_key}"' for attribute_key in keys])

        name_padding = self.attr_key + " " * (
            25 - len(self.attr_key)
        )
        name_schema_padding = " " * (
            25 - len(self.attr_key)
        )
        final_string = (
            f'\t\tself.{name_padding}= namedtuple("{self.attr_key}", {name_schema_padding}[{keystring}])'
        )
        final_string += f'(**data["{self.attr_key}"]) # {self.id}\n'
        return final_string

    def to_dict(self) -> dict:
        """Converts the custom attribute to a dictionary representation. This
        is used when creating named tuples or other data structures.
        """
        new = self.selectable_values.copy()
        new["id"] = self.id
        new["attr_key"] = self.attr_key
        return new
