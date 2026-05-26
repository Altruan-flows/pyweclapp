"""Configuration settings for Weclapp API interactions."""

API_TOKEN_ENV_VAR = "weclappApiToken"
DOMAIN_ENV_VAR = "weclappDomain"

API_VERSION = "v2"
WECLAPP_DOMAIN_ENDING = ".weclapp.com"
AUTHENTICATION_TOKEN_NAME = "AuthenticationToken"
DEFAULT_CONTENT_TYPE = "application/json"

# ----------------- Request Timeout and Wait Timeout -----------------

"""
The current timeout and wait times are configured according to the Weclapp API\
documentation: https://www.weclapp.com/api/v2.html#overview--load-management


"The requests can currently wait in the queue for up to 30 seconds, after that
the application will respond with a HTTP 429 Too Many Requests response. We
recommend using request timeouts of at least one minute to avoid aborting
requests too early that would get a successful response."

Request timeout is twice the recommended request wait timeout: 120 seconds.
Wait timeout is the recommended request wait timeout: 30 seconds.
"""

REQUEST_TIMEOUT = 120  # seconds
REQUEST_TIMEOUT_MS = "120000"  # milliseconds
REQUEST_WAIT_TIMEOUT_MS = "30000"  # milliseconds

# ----------------- Response Headers -----------------

"""
When a request had to wait before being processed, the API includes the following
response headers:

- X-Weclapp-Wait-Ms: The total number of milliseconds the request had to wait
before processing started.

- X-Weclapp-Wait-Reason: The reason for the wait. Possible values: concurrency,
load, or concurrency, load (if both).
    - concurrency — the request was queued because too many parallel requests
    were active.
    - load — the request was delayed because the overall load was too high.

These headers are present on both successful responses and HTTP 429 error responses.
They are not present when the request did not have to wait.
"""


# ----------------- Retry / Load Management -----------------

"""
Retry on transient errors (429, 502, 503, 504) and on connection/timeout failures.
Backoff is exponential with jitter: initial * 2**attempt, capped, randomized +/-25%.
"""

RETRY_MAX_ATTEMPTS = 5  # total attempts (1 initial + up to 4 retries)
RETRY_INITIAL_BACKOFF_S = 1.0  # seconds - first sleep after a retryable failure
RETRY_MAX_BACKOFF_S = 30.0  # ceiling per sleep
RETRY_STATUS_CODES = (429, 502, 503, 504)

# Contact info baked into User-Agent so weclapp support can reach us
# if our traffic shows unusual patterns.
USER_AGENT_CONTACT = "admin@altruan.de"


# ----------------- Response Processing -----------------
DEFAULT_RESPONSE_CONTAINER = "result"
COUNT_REQUEST_IDENTIFIER = "/count"
OPTIMISTIC_LOCK_IDENTIFIER = "optimistic lock error"

# ----------------- Entity Specifics -----------------
BYTE_TYPE_BODY_ENTITIES = ["document"]
