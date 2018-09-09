#!/usr/bin/python3
import json
import urllib.request
import codecs
import domobridge
import lcdbridge

URL = "https://airapi.airly.eu/v1/mapPoint/measurements?latitude=52.39&longitude=16.89&historyHours=24"
API_KEY: str = "9658b2b3da0d45848fb1b312daccad29"
NORM_PM10 = 50
NORM_PM25 = 25
LCD_ROW = 4
PM10_IDX = 3724
PM25_IDX = 3725
TEMP_IDX = 4062


def print_raw_json(status_idx):
    print(json.dumps(status_idx, indent=4, sort_keys=True))


lcdUrl = "http://192.168.1.200/control?cmd=lcd,"
request = urllib.request.Request(URL)
request.add_header("apikey", API_KEY)
response = urllib.request.urlopen(request)

reader = codecs.getreader("utf-8")

data = json.load(reader(response))

# print_raw_json(data)

aki = data["currentMeasurements"]["airQualityIndex"]
pm25 = data["currentMeasurements"]["pm25"]
pm10 = data["currentMeasurements"]["pm10"]
temp = data["currentMeasurements"]["temperature"]

pm10_percentage = pm10 / NORM_PM10
pm25_percentage = pm25 / NORM_PM25

server = domobridge.Server(address="192.168.1.100", port="8050")

dev_pm10 = domobridge.Device(server, PM10_IDX)
dev_pm25 = domobridge.Device(server, PM25_IDX)
dev_temp = domobridge.Device(server, TEMP_IDX)

dev_pm10.update(0, str(pm10_percentage * 100))
dev_pm25.update(0, str(pm25_percentage * 100))
dev_temp.update(0, str(temp))

ergebnis = 'PM10:{:.0%} PM25:{:.0%}'.format(pm10_percentage, pm25_percentage).center(20)
print(ergebnis)

lcd = lcdbridge.LCDBridge()

lcd.send2LCD(4, 1, ergebnis)
