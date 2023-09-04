import codecs
from dataclasses import dataclass
import json
import math
import pprint
import urllib.request
from typing import List, Tuple

import geopy.distance

TRESHOLD_DISTANCE = 5

SYNGEOS_URL_DEV = "https://api.syngeos.pl/api/public/data/device/"

SYNGEOS_URL_SENSOR_TYPES = "https://api.syngeos.pl/api/public/sensors"

SYNGEOS_URL_ALL_SENSORS = "https://api.syngeos.pl/api/v2/public/data/"


def pretty_print(payload):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(payload)


@dataclass
class SyngeosDeviceListItem:
    sensor_type: str
    id: int
    city: str
    address: str
    coordinates: Tuple[float, float]
    distance:float

class NotInitiatedException(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class SyngeosPoller:
    UNIT_TEMP = "°C"
    UNIT_HUM = "%"
    UNIT_air_pressure = "hPa"
    UNIT_PM = "µg/m³"

    def __init__(self, location: Tuple[float, float]):
        self.initiated = False
        self.temperature = 0
        self.humidity = 0
        self.air_pressure = 0
        self.pm2_5 = 0
        self.pm2_5_threshold = 0
        self.pm10 = 0
        self.pm10_threshold = 0
        self.location: Tuple[float, float] = location
        self.response = None

    def get_dev_data(self, deviceId):
        url = SYNGEOS_URL_DEV + str(deviceId)
        response = urllib.request.urlopen(url)
        reader = codecs.getreader("utf-8")
        data = json.load(reader(response))
        return data

    def get_sensor_types(self):
        url = SYNGEOS_URL_SENSOR_TYPES
        response = urllib.request.urlopen(url)
        reader = codecs.getreader("utf-8")
        data = json.load(reader(response))
        return data



    def get_all_sensor_of_type(self, slug: str):
        url = SYNGEOS_URL_ALL_SENSORS + slug
        response = urllib.request.urlopen(url)
        reader = codecs.getreader("utf-8")
        data_raw = json.load(reader(response))
        data: List[SyngeosDeviceListItem] = []
        for item in data_raw:
            point = (item["device"]["coordinates"][0], item["device"]["coordinates"][1])
            new_item = SyngeosDeviceListItem(
                slug,
                item["device"]["id"],
                item["device"]["city"],
                item["device"]["address"],
                point,
                geopy.distance.geodesic(point, self.location).km
            )
            data.append(new_item)

        data_filtered = filter(lambda x:x.distance <= TRESHOLD_DISTANCE, data)
        data_filtered = list(data_filtered)
        data_filtered.sort(key=lambda x:x.distance)
        return data_filtered

    def get_all_devices(self):
        slugs = self.get_sensor_types()
        data_global: List[SyngeosDeviceListItem] = []
        for slug in slugs:
            devices_of_slug = self.get_all_sensor_of_type(slug=slug["slug"])
            data_global.extend(devices_of_slug)
        return data_global

    def read_values_obs(self, payload):
        self.temperature = payload["sensors"][0]["data"][0]["value"]
        self.humidity = payload["sensors"][1]["data"][0]["value"]
        self.air_pressure = payload["sensors"][2]["data"][0]["value"]
        self.pm2_5 = payload["sensors"][3]["data"][0]["value"]
        self.pm10 = payload["sensors"][4]["data"][0]["value"]
        self.pm2_5_threshold = payload["sensors"][3]["norm"]["threshold"]
        self.pm10_threshold = payload["sensors"][4]["norm"]["threshold"]

    def poll(self):
        # self.response = self.get_dev_data(self.device_id)
        self.read_values_obs(self.response)

    @property
    def pm10_percentage(self):
        if self.pm10_threshold != 0:
            return math.floor(100 * (self.pm10 / self.pm10_threshold))
        else:
            raise NotInitiatedException

    @property
    def pm2_5_percentage(self):
        if self.pm10_threshold != 0:
            return math.floor(100 * (self.pm2_5 / self.pm2_5_threshold))
        else:
            raise NotInitiatedException
