#!/usr/bin/python3
'''.
Created on 2 lip 2018

@author: Mariusz Wincior
'''
import domobridge
import urllib.request
import codecs
import json

WILDA_IDX = 8
ESP_IP = "192.168.1.240"

print(domobridge.read_temp(WILDA_IDX))

def LEDPrint(value):
    url = "http://"+ESP_IP+"/control?cmd=7dt,"+str(domobridge.read_temp_float(WILDA_IDX))
    print(url)
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)

    #reader = codecs.getreader("utf-8")
    #data = json.load(reader(response))
    #return data

print(domobridge.print_raw_json(LEDPrint(WILDA_IDX)))

