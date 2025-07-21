from typing import Union, List, Any, Literal
import logging
from pydantic import BaseModel
from datetime import datetime
from pyWeclapp import weclapp, timeFunctions
from . import config


class WeclappMetaData(BaseModel):
    attribute_definition_id: str
    value_name: Union[config.CUSTOM_ATTRIBUTE_TYPES_LITERAL, None] = None
    original_value: Any = None
    value: Any = None
    reset: bool = False

    def __init__(self, **data):
        attribute_definition_id = data["attributeDefinitionId"]
        value_name = None
        value = (
            []
            if any(element in data for element in config.LIST_CUSTOM_ATTRIBUTE_TYPES)
            else None
        )
        for key in config.CUSTOM_ATTRIBUTE_TYPES:
            if key in data:
                value_name = key
                value = data.get(key)
                break
        try:
            super().__init__(
                attributeDefinitionId=attribute_definition_id,
                valueName=value_name,
                value=value,
                originalValue=value,
            )
        except (AttributeError, TypeError) as error:
            logging.error("Error in WeclappMetaData %s: %s", attribute_definition_id, error)
            raise error

    @property
    def updated(self) -> bool:
        """Checks if the value was updated and differs from the original value"""
        if self.original_value == self.value:
            return False
        elif self.original_value is None:
            return True
        else:
            # special cases
            if self.value is not None:
                if self.value_name in config.FLOAT_CUSTOM_ATTRIBUTE_TYPES:
                    if float(self.original_value) == float(self.value):
                        return False
                if self.value_name in config.INT_CUSTOM_ATTRIBUTE_TYPES:
                    if int(self.original_value) == int(self.value):
                        return False
                if self.value_name in config.LIST_CUSTOM_ATTRIBUTE_TYPES:
                    if sorted(self.original_value, key=lambda x: str(x)) == sorted(
                        self.value, key=lambda x: str(x)
                    ):
                        return False
        return True

    @property
    def selectedValueId(self) -> str:
        return str(self.value) if self.value_name == "selectedValueId" else None

    @property
    def stringValue(self) -> str:
        return str(self.value) if self.value_name == "stringValue" else None

    @property
    def booleanValue(self) -> bool:
        return bool(self.value) if self.value_name == "booleanValue" else None

    @property
    def selectedValues(self) -> List[dict]:
        return list(self.value) if self.value_name == "selectedValues" else []

    @property
    def dateValue(self) -> int:
        return int(self.value) if self.value_name == "dateValue" else None

    @property
    def entityId(self) -> str:
        return str(self.value) if self.value_name == "entityId" else None

    @property
    def entityReferences(self) -> List[dict]:
        return list(self.value) if self.value_name == "entityReferences" else []

    @property
    def numberValue(self) -> float:
        return str(self.value) if self.value_name == "numberValue" else None

    def __setattr__(self, name, value):
        if name in config.CUSTOM_ATTRIBUTE_TYPES:
            self.setValue(value, name)
        else:
            super().__setattr__(name, value)

    def checkValueName(self, valueName: config.CUSTOM_ATTRIBUTE_TYPES_LITERAL):
        """Checks for consitstency of valueName"""
        if self.value_name is None:
            self.value_name = valueName
        elif self.value_name != valueName:
            raise ValueError(
                f"ValueName of cAtt {self.name} is {self.value_name} but should be {valueName}"
            )

    # get the valueName of Class
    def getValueName(self):
        """returns the type of custom attribute"""
        return self.value_name

    @property
    def name(self) -> str:
        """==attributeDefinitionId"""
        return self.attribute_definition_id

    def setValue(
        self,
        value,
        valueName: config.CUSTOM_ATTRIBUTE_TYPES_LITERAL,
        unselect: bool = False,
    ):
        """Method to set a new value to a custom attribute. If unselect is True, the value will be set to None."""

        self.checkValueName(valueName)
        # If fields need to be resetted
        if unselect:
            self.reset = True
            self.value = None

        # Update Field
        else:
            self.value = self.validateValue(value)
            if not self.updated:
                logging.info(
                    f"cAtt of {self.attribute_definition_id} was already {self.value} - not updating"
                )

    def addValue(self, value, valueName: config.LIST_CUSTOM_ATTRIBUTE_TYPES_LITERAL):
        """Add a value to selectedValues and entityReferences list if it is not already present"""

        self.checkValueName(valueName)

        # Update Field
        if not isinstance(self.val, list):
            self.value = self.validateValue([])
        if not isinstance(self.val, list):
            raise AssertionError(
                f"self.value should be list but was {type(self.val).__name__}"
            )
        if not all([isinstance(listEl, dict) for listEl in self.val]):
            raise AssertionError("All items in list cAtts should be dicts")
        if self.value_name == "selectedValues":
            currentState = set([listEl["id"] for listEl in self.val])
            currentState.add(value)
            newValue = [{"id": el} for el in currentState]
        else:
            if not ("entityId" in value and "entityName" in value):
                raise AssertionError(
                    "entityReferences need to have entityId and entityName"
                )

            if not value["entityId"] in [entity["entityId"] for entity in self.val]:
                newValue = self.val
                newValue.append(value)
            else:
                newValue = self.val

        self.value = self.validateValue(newValue)

    def removeValue(self, value, valueName: config.LIST_CUSTOM_ATTRIBUTE_TYPES_LITERAL):
        """removes a value from selectedValues and entityReferences list if it is found"""
        self.checkValueName(valueName)

        # Update Field
        if self.value_name not in config.LIST_CUSTOM_ATTRIBUTE_TYPES:
            raise AssertionError(
                "removing a value to cAtt is only possible for list Types"
            )
        if not isinstance(self.val, list):
            self.value = self.validateValue([])
        if not isinstance(self.val, list):
            raise AssertionError(
                f"self.value should be list but was {type(self.val).__name__}"
            )
        if not all([isinstance(listEl, dict) for listEl in self.val]):
            raise AssertionError("All items in list cAtts should be dicts")
        newValue = []
        key = "id" if self.value_name == "selectedValues" else "entityId"
        for el in self.val:
            if el[key] != value:
                newValue.append(el)

        self.value = self.validateValue(newValue)

    def hasValue(self, targetValue: Any = None) -> bool:
        """Checks for selectedValues and entityReferences if a targetValue is present."""
        try:
            if targetValue is None:
                return True if self.val is not None else False
            else:
                if self.value_name == "selectedValues":
                    return targetValue in [
                        el["id"] for el in self.getValue(asType=list, default=[])
                    ]
                elif self.value_name == "entityReferences":
                    return targetValue in [
                        el["entityId"] for el in self.getValue(asType=list, default=[])
                    ]
                else:
                    return True if self.val == targetValue else False
        except Exception as e:
            logging.error(f"catched Error in cAtt.hasValue(): {e}")
            return False

    @property
    def val(self):
        return self.value

    def validateValue(self, value):
        """Validates the custom attriuute value and converts it to the correct
        format. Rasies an error if the value is invalid."""
        # insert Numbers
        if self.value_name == "numberValue":
            if isinstance(value, float):
                return str(round(value, 2))
            if not str(value).replace(".", "").strip("-").isnumeric():
                raise ValueError(
                    f"Error in cAtt.setValue(): Given Value ({str(value)} in object {self.setValue}) is not nummeric"
                )
            return str(value)

        # insert booleans
        elif self.value_name == "booleanValue":
            if not isinstance(value, bool):
                raise ValueError(
                    f"To Update Custom Attribute Value must be bool not {type(value).__name__}"
                )
            return bool(value)

        # insert strings
        elif self.value_name == "stringValue" or self.value_name == "selectedValueId":
            return str(value)

        # if date is selected
        elif self.value_name == "dateValue":
            if isinstance(value, datetime):
                value = timeFunctions.toStr(time=value, to="weclapp")
            if not isinstance(value, int):
                raise ValueError("date needs to be int")
            return int(value)

        # if entity is selected -> be carefull no validation
        elif self.value_name == "entityId" or self.value_name == "selectedValueId":
            return str(value)

        # Multiselect -> the whole list of dicts needs to be passed!!!
        elif self.value_name in config.LIST_CUSTOM_ATTRIBUTE_TYPES:
            if not isinstance(value, list):
                raise ValueError("Type needs to be list of dicts")
            for el in value:
                if not isinstance(el, dict):
                    raise ValueError(
                        "Type needs to be list of dicts - invalid dict -> perhaps overwrite"
                    )
            return value

        else:
            raise ValueError("Error in cAtt.setValue(): Something is seriously wrong")

    def getValue(
        self,
        asType: Union[str, dict, int, float, list, set, bool, datetime],
        default=None,
        raiseError: bool = True,
    ) -> Any:
        """Get the value of an attribute and convert it to a specified format.
        If not found used default if specified. If not Possibe: Error

        Args:
            asType (Union[str, dict, int, float, list, set, bool, datetime]):
            The data type to convert the attribute value to.
            default (Any, optional): The default value to return if the attribute
            is None. Defaults to None.
            raiseError (bool, optional): Whether to raise an error if there is
            an exception. Defaults to True.

        Raises:
            ValueError: If the specified data type is not supported.
            ValueError: If the attribute value is None.
            Exception: If there is an exception and `raiseError` is True.

        Returns:
            Any: The value of the attribute in the specified format.
        """

        try:
            val = self.val
            if val is None and default is not None:
                val = default

            if val is not None:
                if asType == str:
                    return str(val)

                elif asType == dict:
                    return dict(val)

                elif asType == int:
                    return int(float(val))

                elif asType == float:
                    return float(val)

                elif asType == bool:
                    return bool(val)

                elif asType == list:
                    return list(val)

                elif asType == set:
                    return set(val)

                elif asType == datetime:
                    return timeFunctions.parse(val)

                else:
                    raise ValueError(f"Given Type {asType} not found")
            else:
                raise ValueError(f"Value of {self.attribute_definition_id} was None")
        except Exception as e:
            logging.error(e)
            if raiseError:
                raise e
            return default

    def getUpdateDict(self, updateType: Literal["full", "used"] = "used") -> dict:
        """transform the Class back to a dict for updating Weclapp"""
        updateType = updateType if updateType != "used+" else "used"
        if self.updated or updateType == "full":
            answer = {"attributeDefinitionId": self.attribute_definition_id}
            if not self.reset and self.value_name is not None:
                answer[self.value_name] = self.val
            return answer
        return None

    def updateWeclapp(
        self,
        entityName: str,
        entityId: str,
        value: Any,
        valueName: config.CUSTOM_ATTRIBUTE_TYPES_LITERAL,
    ) -> dict:
        """Update a singe custom Attribute to Weclapp"""
        self.setValue(value=value, valueName=valueName)
        body = {"customAttributes": [self.getUpdateDict()]}
        return weclapp.PUT(entityName=entityName, entityId=entityId, body=body)
