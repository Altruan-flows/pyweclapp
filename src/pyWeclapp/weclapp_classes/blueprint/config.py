"""Configuration for weclapp_classes.blueprint package. """

from typing import Literal

# CustomAttributes
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
# LIST_CUSTOM_ATTRIBUTE_TYPES_LITERAL = Literal["selectedValues", "entityReferences"]
INT_CUSTOM_ATTRIBUTE_TYPES = ["selectedValueId", "entityId", "dateValue"]
FLOAT_CUSTOM_ATTRIBUTE_TYPES = ["numberValue"]


# --------- Weclapp Class Creator ---------
ITEMS_NAMES = {
    "salesOrder": "orderItems",
    "shipment": "shipmentItems",
    "contract": "contractItems",
    "article": "articlePrices",
    "salesInvoice": "salesInvoiceItems",
    "ticket": "entityReferences",
    "party": "addresses",
    "customer": "addresses",
}
MANDATORY_FIELDS = [
    "id",
    "version",
    "active",
    "createdDate",
    "lastModifiedDate",
    "articleType",
    "priceScaleType",
    "positionNumber",
]
# COMMON_ENTITIES = []

STATIC_IMPORTS_MODEL_FILES = (
    "This code was dynamically created using WeclappClassCreator from pyweclapp\n\n"
    "from pyweclapp.weclappClasses.weclappClassBlueprint import Blueprint, "
    "WeclappMetaData\nfrom typing import *\n\n\n\n"
)
INIT_FILE_NAME = "__init__.py"
STATIC_IMPORTS_INIT = (
    "from .blueprint.custom_attributes_model import WeclappMetaData"
)
