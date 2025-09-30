"""Configuration for weclapp_classes.blueprint package. """

from typing import Literal

SALES_ORDER = "salesOrder"

CUSTOM_ATTRIBUTE_TYPES = [
    "selectedValueId",
    "stringValue",
    "booleanValue",
    "dateValue",
    "selectedValues",
    "entityId",
    "entityReferences",
    "numberValue",
]
CUSTOM_ATTRIBUTE_TYPES_LITERAL = Literal[
    "selectedValueId",
    "stringValue",
    "booleanValue",
    "dateValue",
    "selectedValues",
    "entityId",
    "entityReferences",
    "numberValue",
]
LIST_CUSTOM_ATTRIBUTE_TYPES = ["selectedValues", "entityReferences"]
LIST_CUSTOM_ATTRIBUTE_TYPES_LITERAL = Literal["selectedValues", "entityReferences"]
SINGLE_VALUE_CUSTOM_ATTRIBUTE_TYPES = [
    "selectedValueId",
    "stringValue",
    "booleanValue",
    "dateValue",
    "entityId",
    "numberValue",
]
SINGLE_VALUE_CUSTOM_ATTRIBUTE_TYPES_LITERAL = Literal[
    "selectedValueId",
    "stringValue",
    "booleanValue",
    "dateValue",
    "entityId",
    "numberValue",
]
INT_CUSTOM_ATTRIBUTE_TYPES = ["selectedValueId", "entityId", "dateValue"]
FLOAT_CUSTOM_ATTRIBUTE_TYPES = ["numberValue"]


# --------- Weclapp Class Creator ---------
CREATION_QUERY = {"serializeNulls": "", "sort": "-createdDate"}

STATIC_IMPORTS_MODEL_FILES = (
    '"""This code was dynamically created using WeclappClassCreator from pyweclapp"""'
    "\n\n"
    "from typing import Union, Optional, List\n"
    "from .blueprints import Blueprint, WeclappMetaData\n\n\n"
)
INIT_FILE_NAME = "__init__.py"
STATIC_IMPORTS_INIT = "from .blueprints.custom_attributes_model import WeclappMetaData"
INIT_FILE_DOC_STRING = (
    '"""Module for weclapp classes package imports. Add more classes if necessary."""\n'
)

EXCLUDED_KEYS = {
    "used_attributes",
    "used_keys",
    "excluded_keys",
    "createdDate",
    "lastModifiedDate",
    "statusHistory",
    "lastModifiedByUserId"
}
