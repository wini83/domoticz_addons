#!/usr/bin/python3
'''.
Created on 2 lip 2018

@author: Mariusz Wincior
'''
import domobridge
import urllib.request

WILDA_IDX = 5919
ESP_IP = "192.168.1.204"


def LEDPrint(value):
    url = "http://"+ESP_IP+"/control?cmd=7dt,"+str(value)
    print(url)
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req) 
    #reader = codecs.getreader("utf-8")
    #data = json.load(reader(response))
    #return data

server = domobridge.Server(address="192.168.1.100", port="8050")
dev1 = domobridge.Device(server, WILDA_IDX)

temperature = dev1.temp
print(temperature)

LEDPrint(temperature)

