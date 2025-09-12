"""CustomAttributeClass for handling custom attributes in Weclapp."""


class CustomAttributeClass:
    """Class representing a custom attribute in Weclapp."""
    def __init__(
        self,
        group_name: str,
        attr_key: str,
        attr_id: str,
        attr_type: str,
        selectable_values: dict,
    ):
        self.group_name = group_name
        self.attr_key = attr_key
        self.attr_id = attr_id
        self.attr_type = attr_type
        self.selectable_values: dict = selectable_values

    def generate_python_line(self) -> str:
        """Generates a Python line for the custom attribute. This is used when
        creating the custom attributes class in Python.
        """
        return f"        self.{self.attr_key}: SimpleNamespace  # {self.attr_id}\n"

    def to_dict(self) -> dict:
        """Converts the custom attribute to a dictionary representation. This
        is used when creating named tuples or other data structures.
        """
        new = self.selectable_values.copy()
        new["id"] = self.attr_id
        new["attr_key"] = self.attr_key
        return new
