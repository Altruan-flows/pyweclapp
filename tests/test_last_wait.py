"""last_wait(): the X-Weclapp-Wait-Ms signal shared by every Weclapp instance."""

from unittest import mock

import pytest
import requests

from pyweclapp import Weclapp, WeclappWait, last_wait
from pyweclapp import weclapp as weclapp_module

URL = "https://example.weclapp.com/webapp/api/v1/salesOrder"


def _response(status_code: int, headers: dict) -> requests.Response:
    response = requests.Response()
    response.status_code = status_code
    response.headers.update(headers)
    response._content = b"{}"  # pylint: disable=protected-access
    return response


@pytest.fixture(autouse=True)
def no_previous_wait(monkeypatch):
    monkeypatch.setattr(weclapp_module, "_last_wait", None)
    monkeypatch.setattr(weclapp_module.time, "sleep", lambda _seconds: None)


def _send(*responses: requests.Response) -> requests.Response:
    client = Weclapp(api_token="token", domain="example.weclapp.com")
    with mock.patch.object(
        weclapp_module, "_request_with_deadline", side_effect=list(responses)
    ):
        return client._request("GET", URL)  # pylint: disable=protected-access


def test_no_wait_header_leaves_signal_empty():
    _send(_response(200, {}))

    assert last_wait() is None


def test_queued_success_is_recorded():
    with mock.patch.object(weclapp_module.time, "time", return_value=1700000000.0):
        _send(
            _response(
                200, {"X-Weclapp-Wait-Ms": "2500", "X-Weclapp-Wait-Reason": "load"}
            )
        )

    assert last_wait() == WeclappWait(wait_ms=2500, reason="load", at=1700000000.0)


def test_queued_429_is_recorded_before_the_retry():
    _send(
        _response(
            429, {"X-Weclapp-Wait-Ms": "30000", "X-Weclapp-Wait-Reason": "concurrency"}
        ),
        _response(200, {}),
    )

    wait = last_wait()
    assert wait is not None
    assert (wait.wait_ms, wait.reason) == (30000, "concurrency")


def test_signal_is_shared_across_instances():
    _send(_response(200, {"X-Weclapp-Wait-Ms": "10"}))
    _send(_response(200, {}))

    wait = last_wait()
    assert wait is not None
    assert (wait.wait_ms, wait.reason) == (10, None)


def test_latest_wait_wins():
    _send(_response(200, {"X-Weclapp-Wait-Ms": "10"}))
    _send(_response(200, {"X-Weclapp-Wait-Ms": "20", "X-Weclapp-Wait-Reason": "load"}))

    wait = last_wait()
    assert wait is not None
    assert (wait.wait_ms, wait.reason) == (20, "load")


def test_unparseable_header_is_ignored():
    _send(_response(200, {"X-Weclapp-Wait-Ms": "soon"}))

    assert last_wait() is None
