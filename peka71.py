#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2 sty 2018


'''

import json
import urllib2
import time
import urllib
from lcdbridge import LCDBridge

LCD_ROW = 3
LCD_IP = "192.168.1.200"
PEKA_URL = "http://www.peka.poznan.pl/vm/method.vm?ts="


def now_milliseconds():
    return int(time.time() * 1000)

lcdUrl = "http://192.168.1.200/control?cmd=lcd,"

def peka_vm_get(met,p0):
    url = PEKA_URL+str(now_milliseconds())
    headers = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8"}
    payload = urllib.urlencode({'method' : met,
                                'p0'  : p0})
    req = urllib2.Request(url, payload, headers)
    response = urllib2.urlopen(req)

    # Parse Json
    data = json.load(response)
    return data

# Preety print the result
#print json.dumps(peka_vm_get('getStopPoints','{"pattern":"IPN"}'), indent=4, sort_keys=True)

#print json.dumps(peka_vm_get('getBollardsByStopPoint','{"name":"IPN"}'), indent=4, sort_keys=True)

def get_1st_departure(bollard):
    json_data = peka_vm_get('getTimes','{"symbol":"'+bollard+'"}')
    try:
        departure = json_data["success"]["times"][0]
        
        result = '{}>{}:{}m'.format(departure["line"],departure["direction"].encode('UTF-8')[0:14],departure["minutes"])
        return result
    except:
        return "error"

text2send = get_1st_departure("IPNZ01")
print(text2send)
display = LCDBridge()
display.send2LCD(3, 1, text2send)





