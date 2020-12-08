import codecs
import json
import math
import pprint
import urllib.request

SYNGEOS_URL = "https://api.syngeos.pl/api/public/data/device/"





def pretty_print(payload):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(payload)


class NotInitiatedException(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class SyngeosPoller:
    UNIT_TEMP = "°C"
    UNIT_HUM = "%"
    UNIT_air_pressure = "hPa"
    UNIT_PM = "µg/m³"
    def __init__(self, deviceId):
        self.initiated = False
        self.temperature = 0
        self.humidity = 0
        self.air_pressure = 0
        self.pm2_5 = 0
        self.pm2_5_threshold = 0
        self.pm10 = 0
        self.pm10_threshold = 0
        self.device_id = deviceId
        self.response = None

    def syngeos_get(self, deviceId):
        url = SYNGEOS_URL + str(deviceId)
        response = urllib.request.urlopen(url)
        reader = codecs.getreader("utf-8")
        # Parse Json
        data = json.load(reader(response))
        return data

    def read_values(self, payload):
        self.temperature = payload["sensors"][0]["data"][0]["value"]
        self.humidity = payload["sensors"][1]["data"][0]["value"]
        self.air_pressure = payload["sensors"][2]["data"][0]["value"]
        self.pm2_5 = payload["sensors"][3]["data"][0]["value"]
        self.pm10 = payload["sensors"][4]["data"][0]["value"]
        self.pm2_5_threshold = payload["sensors"][3]["norm"]["threshold"]
        self.pm10_threshold = payload["sensors"][4]["norm"]["threshold"]

    def poll(self):
        self.response = self.syngeos_get(self.device_id)
        self.read_values(self.response)

    @property
    def pm10_percentage(self):
        if self.pm10_threshold != 0:
            return math.floor(100*(self.pm10/self.pm10_threshold))
        else:
            raise NotInitiatedException

    @property
    def pm2_5_percentage(self):
        if self.pm10_threshold != 0:
            return math.floor(100*(self.pm2_5/self.pm2_5_threshold))
        else:
            raise NotInitiatedException

