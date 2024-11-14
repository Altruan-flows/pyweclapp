from typing import Literal

ODATA_EXCEPTIONS = [
    "properties",
    "entityId",
    "entityName",
    "name",
    "description",
    "pageSize",
    "page",
    "additionalProperties",
    "includeReferencedEntities",
    "serializeNulls",
    "sort",
]


# Environment Variable NAMES
ENV_DOMAIN_NAME = "weclappDomain"
ENV_AUTHENTICATION_TOKEN_NAME_BASE = "Weclapp_AuthenticationToken"


# authentication
AVAILABLE_APIKEYS = Literal["key0", "key1"]
ENTITY_NAMES = Literal[
    "salesOrder",
    "shipment",
    "salesInvoice",
    "contract",
    "article",
    "quotation",
    "customer",
    "ticket",
]
DEFAULT_KEY = "key0"
AUTHENTICATION_TOKEN_NAME = "AuthenticationToken"
DEFAULT_CONTENT_TYPE = "application/json"

API_VERSION = "v1"


# response Handling
DEFAULT_RESPONSE_CONTAINER = "result"
COUNT_REQUEST_IDENTIFIER = "/count"
BYTE_TYPE_BODYS_ENTITIES = ["document"]


# weclapp Error
OPTIMISTIC_LOCK_IDENTIFIER = "optimistic lock error"
HAS_WRONG_STATUS_IDENTIFIER = "Sales order confirmation created"
