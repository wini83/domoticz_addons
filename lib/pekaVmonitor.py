"""Small client for Poznań PEKA virtual departure monitor.

The PEKA endpoint is unofficial and may change without notice.
"""
import json
import string
import time
import urllib.parse
import urllib.request

PEKA_URL = "https://www.peka.poznan.pl/vm/method.vm?ts="


def now_milliseconds():
    return int(time.time() * 1000)


class pekaVmonitor:
    """Keep the historical API for existing Domoticz integrations."""

    def peka_vm_get(self, met, p0):
        url = PEKA_URL + str(now_milliseconds())
        headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        payload = urllib.parse.urlencode({"method": met, "p0": p0}).encode("utf-8")
        request = urllib.request.Request(url, payload, headers=headers)

        with urllib.request.urlopen(request, timeout=10) as response:
            return json.load(response)

    def get_1st_departure_json(self, bollard):
        data = self.peka_vm_get("getTimes", json.dumps({"symbol": bollard}))
        try:
            return data["success"]["times"][0]
        except (KeyError, IndexError, TypeError):
            return "error"

    def get_1st_departure(self, bollard):
        departure = self.get_1st_departure_json(bollard)
        if departure == "error":
            return "error"
        return (departure["line"], departure["direction"], departure["minutes"])

    def get_1st_departure_xchar(self, bollard, length):
        departure = self.get_1st_departure(bollard)
        if departure == "error":
            return "error".ljust(length, " ")

        line, direction, minutes = departure
        available = max(0, length - len(str(line)) - len(str(minutes)) - 2)
        translator = str.maketrans("", "", string.punctuation)
        short_direction = direction.replace(" ", "").translate(translator)[:available]
        return f"{line}>{short_direction}:{minutes}"
