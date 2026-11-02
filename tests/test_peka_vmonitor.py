import json
from io import BytesIO
from unittest.mock import patch

import pytest

from lib.pekaVmonitor import pekaVmonitor


class Response(BytesIO):
    pass


def test_request_uses_form_data_and_timeout():
    monitor = pekaVmonitor()
    with patch("lib.pekaVmonitor.urllib.request.urlopen", return_value=Response(b'{"success":{"times":[]}}')) as urlopen:
        assert monitor.peka_vm_get("getTimes", '{"symbol":"IPNZ02"}') == {"success": {"times": []}}
    request = urlopen.call_args.args[0]
    assert request.full_url.startswith("https://www.peka.poznan.pl/vm/method.vm?ts=")
    assert urlopen.call_args.kwargs["timeout"] == 10
    assert b"method=getTimes" in request.data
    assert b"IPNZ02" in request.data


def test_departure_and_short_format():
    monitor = pekaVmonitor()
    result = {"success": {"times": [{"line": "16", "direction": "Os. Sobieskiego", "minutes": 4}]}}
    with patch.object(monitor, "peka_vm_get", return_value=result) as get:
        assert monitor.get_1st_departure("IPNZ02") == ("16", "Os. Sobieskiego", 4)
        assert monitor.get_1st_departure_xchar("IPNZ02", 14) == "16>OsSobiesk:4"
    assert json.loads(get.call_args.args[1]) == {"symbol": "IPNZ02"}


@pytest.mark.parametrize("payload", [
    {"success": {"times": []}},
    {"success": {}},
    {"error": "unknown stop"},
])
def test_missing_departures_return_error(payload):
    monitor = pekaVmonitor()
    with patch.object(monitor, "peka_vm_get", return_value=payload):
        assert monitor.get_1st_departure_json("IPNZ02") == "error"
        assert monitor.get_1st_departure_xchar("IPNZ02", 8) == "error   "


def test_network_errors_are_not_hidden():
    monitor = pekaVmonitor()
    with patch.object(monitor, "peka_vm_get", side_effect=TimeoutError("offline")):
        with pytest.raises(TimeoutError):
            monitor.get_1st_departure_json("IPNZ02")
