#!/usr/bin/python3
import json
import urllib.request
import codecs
import domobridge

URL = "https://airapi.airly.eu/v1/mapPoint/measurements?latitude=52.39&longitude=16.89&historyHours=24"
APIKEY = "9658b2b3da0d45848fb1b312daccad29"
NORM_PM10 = 50
NORM_PM25 = 25
LCD_ROW = 4

PM10_IDX = 3724
PM25_IDX = 3725

lcdUrl = "http://192.168.1.200/control?cmd=lcd,"
request = urllib.request.Request(URL)
request.add_header("apikey", APIKEY)
response = urllib.request.urlopen(request)

reader = codecs.getreader("utf-8")

data = json.load(reader(response))


aki =  data["currentMeasurements"]["airQualityIndex"]
pm25 =  data["currentMeasurements"]["pm25"]
pm10 = data["currentMeasurements"]["pm10"]

pm10_percentage = pm10/NORM_PM10
pm25_percentage = pm25/NORM_PM25

domobridge.set_value(PM10_IDX, pm10_percentage*100)
domobridge.set_value(PM25_IDX, pm25_percentage*100)
ergebnis = 'PM10:{:.0%} PM25:{:.0%}'.format(pm10_percentage,pm25_percentage).center(20)
print (ergebnis)

from lcdbridge import LCDBridge

lcd = LCDBridge()

lcd.send2LCD(4, 1, ergebnis)


