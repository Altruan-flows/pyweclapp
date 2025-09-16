"""This module defines the WeclappMetaData class, which represents custom attributes
in Weclapp entities. It includes methods for setting, adding, and removing values,
validating values, and checking if a value is present."""

import logging
from datetime import datetime
from typing import Union, Any, Literal
from pydantic import BaseModel
from ...time_functions import convert_to_time_format
from . import config


class WeclappMetaData(BaseModel):
    """Class representing custom attributes in Weclapp entities."""

    attributeDefinitionId: str
    valueName: Union[config.CUSTOM_ATTRIBUTE_TYPES_LITERAL, None] = None
    value: Any = None
    originalValue: Any = None
    empty: bool = False

    def __init__(self, **data):
        attribute_definition_id = data["attributeDefinitionId"]
        value_name = None
        value = (
            []
            if any(key in data for key in config.LIST_CUSTOM_ATTRIBUTE_TYPES)
            else None
        )
        for key in config.CUSTOM_ATTRIBUTE_TYPES:
            if key in data:
                value_name = key
                value = data.get(key)
                break

        super().__init__(
            attributeDefinitionId=attribute_definition_id,
            valueName=value_name,
            value=value,
            originalValue=value,
        )

    @property
    def updated(self) -> bool:
        """Checks if the value was updated and differs from the original value."""
        if self.originalValue == self.value:
            return False
        if self.originalValue is None:
            return True
        if self.value is not None:
            if self.valueName in config.FLOAT_CUSTOM_ATTRIBUTE_TYPES:
                if float(self.originalValue) == float(self.value):
                    return False
            if self.valueName in config.INT_CUSTOM_ATTRIBUTE_TYPES:
                if int(self.originalValue) == int(self.value):
                    return False
            if self.valueName in config.LIST_CUSTOM_ATTRIBUTE_TYPES:
                if sorted(self.originalValue, key=lambda x: str(x)) == sorted(
                    self.value, key=lambda x: str(x)
                ):
                    return False
        return True

    def set_value(
        self,
        value: Any,
        value_name: config.CUSTOM_ATTRIBUTE_TYPES_LITERAL,
        empty_field: bool = False,
    ) -> None:
        """Method to set a new value to a custom attribute. If empty_field is True,
        the update dictionary will not contain field value and the custom attribute
        field will be empty in Weclapp after update."""
        self.valueName = value_name

        if self.valueName not in config.SINGLE_VALUE_CUSTOM_ATTRIBUTE_TYPES:
            raise AssertionError(
                "Function set_value() is only for single value custom attributes, "
                f"not for {self.valueName}"
            )

        if empty_field:
            self.empty = True
            self.value = None

        else:
            self.value = self.validate_value(value)

    def add_value(self, value: Any, value_name: config.CUSTOM_ATTRIBUTE_TYPES_LITERAL) -> None:
        """Add a value to a list of values. This function is only for
        custom attributes that have multiselection capabilities, such as
        selectedValues and entityReferences."""
        self.valueName = value_name

        if self.valueName not in config.LIST_CUSTOM_ATTRIBUTE_TYPES:
            raise AssertionError(
                "Function add_value() is only for list custom attributes, "
                f"not for {self.valueName}"
            )

        if self.valueName == "selectedValues":
            selected_value_ids = {element["id"] for element in self.value}
            selected_value_ids.add(value)
            updated_values_list = [{"id": el} for el in selected_value_ids]
        else:
            if not ("entityId" in value and "entityName" in value):
                raise AssertionError(
                    "Value of entityReferences need to have entityId and entityName"
                )
            if not value["entityId"] in [entity["entityId"] for entity in self.value]:
                updated_values_list = self.value
                updated_values_list.append(value)
            else:
                updated_values_list = self.value

        self.value = self.validate_value(updated_values_list)

    def remove_value(self, value: Any, value_name: config.CUSTOM_ATTRIBUTE_TYPES_LITERAL) -> None:
        """Removes a value from a list of values. This function is only for
        custom attributes that have multiselection capabilities, such as
        selectedValues and entityReferences."""
        self.valueName = value_name

        if self.valueName not in config.LIST_CUSTOM_ATTRIBUTE_TYPES:
            raise AssertionError(
                "Function add_value() is only for list custom attributes, "
                f"not for {self.valueName}"
            )

        updated_values_list = []
        key = "id" if self.valueName == "selectedValues" else "entityId"
        for element in self.value:
            if element[key] != value:
                updated_values_list.append(element)

        self.value = self.validate_value(updated_values_list)

    def has_value(self, target_value: Any) -> bool:
        """Checks for selectedValues and entityReferences if a targetValue is
        present. Here valueName will always be provided, because Weclapp API
        always shows multiselection values as lists, even if it is empty. If not
        provided, it is then assumed that this is not a multiselection
        custom attribute."""
        if target_value is None:
            logging.error("target_value is None, cannot check for presence")
            return False
        if self.valueName is None:
            logging.error(
                "valueName is None, check if this is a custom attribute of "
                "multiselection type"
            )
            return False

        if self.valueName == "selectedValues":
            return target_value in [
                el["id"] for el in self.value
            ]
        if self.valueName == "entityReferences":
            return target_value in [
                el["entityId"] for el in self.value
            ]
        return self.value == target_value

    def validate_value(self, value: Any) -> Any:
        """Validates the custom attribute value and converts it to the correct
        format. Raises an error if the value format is invalid and cannot be converted.
        """

        if self.valueName == "numberValue":
            if type(value) in [int, float]:
                return str(round(value, 2))
            if not str(value).replace(".", "").strip("-").isnumeric():
                raise ValueError(
                    f"Given value ({value}) is not numeric. It needs to be "
                    "a float or int, or a string that can be converted to a float."
                )
            return str(value)

        if self.valueName == "booleanValue":
            if not isinstance(value, bool):
                raise ValueError(
                    f"Given value ({value}) is not boolean. It needs to be a boolean."
                )
            return bool(value)

        if self.valueName in ["stringValue", "entityId", "selectedValueId"]:
            return str(value)

        if self.valueName == "dateValue":
            if isinstance(value, datetime):
                value = convert_to_time_format(value, conversion_format="weclapp")
            if not isinstance(value, int):
                raise ValueError(
                    f"Date value ({value}) is not int. It needs to be an int "
                    " or a datetime object."
                )
            return int(value)

        if self.valueName in config.LIST_CUSTOM_ATTRIBUTE_TYPES:
            if not isinstance(value, list):
                raise ValueError(
                    f"Value ({value}) must be a list, but is {type(value).__name__}"
                )
            for element in value:
                if not isinstance(element, dict):
                    raise ValueError(
                        f"All elements in the list must be dicts, but "
                        f"found {type(element).__name__}"
                    )
            return value

        raise ValueError("Error in cAtt.setValue(): Something is seriously wrong")

    def build_update_dictionary(
        self,
        update_type: Literal["full", "used"] = "used",
    ) -> dict:
        """Builds a dictionary for updating or creating an entity in Weclapp.
        Args:
            update_type (Literal[full, used]): Type of update. Defaults to
                "used".
                - "full": Update dictionary will include all attributes of the
                    instance. This type of update should be used with caution as it
                    may lead to optimistic lock errors and could potentially overwrite
                    some values to empty if they are not set in the instance.
                - "used": Update dictionary will include only attributes that have been used.
        Returns:
            dict: Dictionary representing the entity to be updated or created.
        """
        data_to_send = {}
        if self.updated or update_type == "full":
            data_to_send["attributeDefinitionId"] = self.attributeDefinitionId
            if self.valueName is not None:
                data_to_send[self.valueName] = self.value
        return data_to_send
