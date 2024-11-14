from typing import Union, List, Any, Literal
import logging
from pydantic import BaseModel
from datetime import datetime
from pyWeclapp import weclapp, timeFunctions
from . import config


class WeclappMetaData(BaseModel):
    attributeDefinitionId: str
    valueName: Union[config.CUSTOM_ATTRIBUTE_TYPES_LITERAL, None] = None
    originalValue: Any = None
    value: Any = None
    reset: bool = False

    def __init__(self, **data):
        attributeDefinitionId = data["attributeDefinitionId"]
        valueName = None
        value = (
            []
            if any(element in data for element in config.LIST_CUSTOM_ATTRIBUTE_TYPES)
            else None
        )
        for key in config.CUSTOM_ATTRIBUTE_TYPES:
            if key in data:
                valueName = key
                value = data.get(key)
                break
        try:
            super().__init__(
                attributeDefinitionId=attributeDefinitionId,
                valueName=valueName,
                value=value,
                originalValue=value,
            )
        except (AttributeError, TypeError) as error:
            logging.error(f"Error in WeclappMetaData {attributeDefinitionId}: {error}")
            raise error

    @property
    def updated(self) -> bool:
        """Checks if the value was updated and differs from the original value"""
        if self.originalValue == self.value:
            return False
        elif self.originalValue is None:
            return True
        else:
            # special cases
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

    @property
    def selectedValueId(self) -> str:
        return str(self.value) if self.valueName == "selectedValueId" else None

    @property
    def stringValue(self) -> str:
        return str(self.value) if self.valueName == "stringValue" else None

    @property
    def booleanValue(self) -> bool:
        return bool(self.value) if self.valueName == "booleanValue" else None

    @property
    def selectedValues(self) -> List[dict]:
        return list(self.value) if self.valueName == "selectedValues" else []

    @property
    def dateValue(self) -> int:
        return int(self.value) if self.valueName == "dateValue" else None

    @property
    def entityId(self) -> str:
        return str(self.value) if self.valueName == "entityId" else None

    @property
    def entityReferences(self) -> List[dict]:
        return list(self.value) if self.valueName == "entityReferences" else []

    @property
    def numberValue(self) -> float:
        return str(self.value) if self.valueName == "numberValue" else None

    def __setattr__(self, name, value):
        if name in config.CUSTOM_ATTRIBUTE_TYPES:
            self.setValue(value, name)
        else:
            super().__setattr__(name, value)

    def checkValueName(self, valueName: config.CUSTOM_ATTRIBUTE_TYPES_LITERAL):
        """Checks for consitstency of valueName"""
        if self.valueName is None:
            self.valueName = valueName
        elif self.valueName != valueName:
            raise ValueError(
                f"ValueName of cAtt {self.name} is {self.valueName} but should be {valueName}"
            )

    # get the valueName of Class
    def getValueName(self):
        """returns the type of custom attribute"""
        return self.valueName

    @property
    def name(self) -> str:
        """==attributeDefinitionId"""
        return self.attributeDefinitionId

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
                    f"cAtt of {self.attributeDefinitionId} was already {self.value} - not updating"
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
        if self.valueName == "selectedValues":
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
        if self.valueName not in config.LIST_CUSTOM_ATTRIBUTE_TYPES:
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
        key = "id" if self.valueName == "selectedValues" else "entityId"
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
                if self.valueName == "selectedValues":
                    return targetValue in [
                        el["id"] for el in self.getValue(asType=list, default=[])
                    ]
                elif self.valueName == "entityReferences":
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
        if self.valueName == "numberValue":
            if isinstance(value, float):
                return str(round(value, 2))
            if not str(value).replace(".", "").strip("-").isnumeric():
                raise ValueError(
                    f"Error in cAtt.setValue(): Given Value ({str(value)} in object {self.setValue}) is not nummeric"
                )
            return str(value)

        # insert booleans
        elif self.valueName == "booleanValue":
            if not isinstance(value, bool):
                raise ValueError(
                    f"To Update Custom Attribute Value must be bool not {type(value).__name__}"
                )
            return bool(value)

        # insert strings
        elif self.valueName == "stringValue" or self.valueName == "selectedValueId":
            return str(value)

        # if date is selected
        elif self.valueName == "dateValue":
            if isinstance(value, datetime):
                value = timeFunctions.toStr(time=value, to="weclapp")
            if not isinstance(value, int):
                raise ValueError("date needs to be int")
            return int(value)

        # if entity is selected -> be carefull no validation
        elif self.valueName == "entityId" or self.valueName == "selectedValueId":
            return str(value)

        # Multiselect -> the whole list of dicts needs to be passed!!!
        elif self.valueName in config.LIST_CUSTOM_ATTRIBUTE_TYPES:
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
                raise ValueError(f"Value of {self.attributeDefinitionId} was None")
        except Exception as e:
            logging.error(e)
            if raiseError:
                raise e
            return default

    def getUpdateDict(self, updateType: Literal["full", "used"] = "used") -> dict:
        """transform the Class back to a dict for updating Weclapp"""
        updateType = updateType if updateType != "used+" else "used"
        if self.updated or updateType == "full":
            answer = {"attributeDefinitionId": self.attributeDefinitionId}
            if not self.reset and self.valueName is not None:
                answer[self.valueName] = self.val
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
