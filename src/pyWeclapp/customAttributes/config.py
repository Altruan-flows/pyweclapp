FILE_TYPE = "py"
JSON_DATA_FOLDER_NAME = "catData"
FILENAME_CAT_SETTINGS = "cat_Settings"
FILENAME_ALL_CAT_DATA = "all"
STATIC_IDS_JSON_FILE = "StaticOrExcludedIDs"
STATIC_OR_EXCLUDED_IDS = {
    "2174360": "FORMER_SERVICE",
    "27993891": "ebay1StockTransfer",
    "27993890": "ebay2StockTransfer",
    "26423400": "ebay1Available",
    "26423399": "ebay2Available",
    "1527232": "amazonASIN",
    "1527231": "amazonSlSKU",
    "1527230": "amazonFbaSku",
    "1527229": "amazonSKU",
    "1527228": "amazonStockTransfer",
    "1527227": "amazonAvailable",
    "291457": "wooDescription",
    "8613": "wooStockTransfer",
    "8612": "wooActive",
    "8611": "wooAvailable",
    "45569272": "shopifyId",
    "45569274": "shopifyVariantId",
}
PREFIX_GROUPNAME_STATIC_IDS = "STATIC_"
PREFIX_GROUPNAME_ITEMS_ATTS = "ITEMS_"

# Citty Constants
DEFAULT_FIRST_CHAR = "v_"
BASE_ATTRIBUTES = ["id", "valueName"]
DEFAULT_GROUP_NAME = "other"
VALUE_NAME_MAPPING = {
    "MULTISELECT_LIST": "selectedValues",
    "INTEGER": "numberValue",
    "DECIMAL": "numberValue",
    "LIST": "selectedValueId",
    "BOOLEAN": "booleanValue",
    "STRING": "stringValue",
    "LARGE_TEXT": "stringValue",
    "DATE": "dateValue",
    "ENTITY": "entityId",
    "REFERENCE": "entityReferences",
    "URL": "stringValue",
}
DEFAULT_CAT_INDENT_SPACES = (
    25  # number of characters to indent after the catName before the
)
