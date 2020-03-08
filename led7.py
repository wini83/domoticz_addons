#!/usr/bin/python3
'''.
Created on 2 lip 2018

@author: Mariusz Wincior
'''
import DomoticzAPI as dom
import urllib.request
import datetime

WILDA_IDX = 5919
ESP_IP = "192.168.2.204"


def led_print(value):
    url = "http://" + ESP_IP + "/control?cmd=7dt," + str(value)
    print(url)
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    # reader = codecs.getreader("utf-8")
    # data = json.load(reader(response))
    # return data


server = dom.Server(address="192.168.2.100", port="8050")
dev1 = dom.Device(server, WILDA_IDX)

temperature = dev1.temp
lastupd = datetime.datetime.strptime(dev1.lastupdate, '%Y-%m-%d %H:%M:%S')
print("Last Update: {}".format(lastupd))
now = datetime.datetime.now()
delta = now - lastupd
delta = divmod(delta.seconds, 60)[0]
print("Minutes ago: {}".format(delta))

print("Temperature: {}".format(temperature))

if delta > 180:
    temperature = 99

#led_print(temperature)
