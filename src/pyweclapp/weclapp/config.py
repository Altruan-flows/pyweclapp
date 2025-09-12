"""Configuration settings for Weclapp API interactions."""

API_TOKEN_ENV_VAR = "WECLAPP_API_TOKEN"
DOMAIN_ENV_VAR = "WECLAPP_DOMAIN"

API_VERSION = "v2"
WECLAPP_DOMAIN_ENDING = ".weclapp.com"
AUTHENTICATION_TOKEN_NAME = "AuthenticationToken"
DEFAULT_CONTENT_TYPE = "application/json"
REQUEST_TIMEOUT = 120  # seconds

# ----------------- Response Processing -----------------
DEFAULT_RESPONSE_CONTAINER = "result"
COUNT_REQUEST_IDENTIFIER = "/count"
OPTIMISTIC_LOCK_IDENTIFIER = "optimistic lock error"

# ----------------- Entity Specifics -----------------
BYTE_TYPE_BODY_ENTITIES = ["document"]
