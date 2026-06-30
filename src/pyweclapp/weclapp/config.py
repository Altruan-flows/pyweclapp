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

The timeout passed to requests is a (connect, read) tuple. The connect value
caps how long we wait to establish the TCP connection; the read value caps the
gap allowed between bytes once the connection is open. Note that read is an
*inactivity* timeout (it resets on every received byte), not a total wall-clock
deadline -- a server that trickles data can still hold the connection longer
than the read value.

REQUEST_HARD_DEADLINE_S is an absolute wall-clock cap per attempt, enforced by
streaming the response body and aborting once the elapsed time exceeds it. This
is the backstop the (connect, read) tuple cannot provide.
"""

REQUEST_CONNECT_TIMEOUT_S = 10  # seconds - cap on establishing the connection
REQUEST_READ_TIMEOUT_S = 120  # seconds - cap on the gap between received bytes
REQUEST_HARD_DEADLINE_S = 150  # seconds - absolute wall-clock cap per attempt
REQUEST_TIMEOUT = (REQUEST_CONNECT_TIMEOUT_S, REQUEST_READ_TIMEOUT_S)  # (connect, read)
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

RETRY_MAX_ATTEMPTS = 2  # total attempts (1 initial + up to 1 retry)
RETRY_INITIAL_BACKOFF_S = 1.0  # seconds - first sleep after a retryable failure
RETRY_MAX_BACKOFF_S = 30.0  # ceiling per sleep
RETRY_STATUS_CODES = (429, 502, 503, 504)

# Contact info baked into User-Agent so weclapp support can reach us
# if our traffic shows unusual patterns.
USER_AGENT_CONTACT = "admin@altruan.de"

# ----------------- Rollbar Load Reporting -----------------
# When this env var is truthy ("1"/"true"/"yes") AND the `rollbar` package is
# installed AND the consuming app has called rollbar.init(), pyweclapp reports
# every response carrying X-Weclapp-Wait-* headers to Rollbar as a warning.
ROLLBAR_REPORTING_ENV_VAR = "weclappRollbarReporting"


# ----------------- Response Processing -----------------
DEFAULT_RESPONSE_CONTAINER = "result"
COUNT_REQUEST_IDENTIFIER = "/count"
OPTIMISTIC_LOCK_IDENTIFIER = "optimistic lock error"

# ----------------- Entity Specifics -----------------
BYTE_TYPE_BODY_ENTITIES = ["document"]
