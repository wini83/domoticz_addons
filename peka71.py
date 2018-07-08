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
import string

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

def get_1st_departure_json(bollard):
    json_data = peka_vm_get('getTimes','{"symbol":"'+bollard+'"}')
    try:
        departure = json_data["success"]["times"][0]
        return departure
    except:
        return "error"#.ljust(15," ")
    
def get_1st_departure_20char(bollard):
    departure = get_1st_departure_json(bollard)
    if(departure != "error"):
        line_len = len(departure["line"])
        minutes_len = len(str(departure["minutes"]))
        direction = departure["direction"].replace(" ", "").encode('UTF-8')[0:10].translate(None,string.punctuation)
        line = departure["line"]
        minutes = departure["minutes"]
        result = '{}>{}:{}'.format(line,direction,minutes).ljust(20," ")
        return result
    else:
        return "error".ljust(20," ")
    
def get_1st_departure_xchar(bollard,length):
    departure = get_1st_departure_json(bollard)
    if(departure != "error"):
        line_len = len(departure["line"])
        minutes_len = len(str(departure["minutes"]))
        length = length - line_len - minutes_len - 1
        direction = departure["direction"].replace(" ", "")
        direction = direction.encode('UTF-8').translate(None,string.punctuation)[0:length]
        line = departure["line"]
        minutes = departure["minutes"]
        result = '{}>{}:{}'.format(line,direction,minutes)#.ljust(length-," ")
        return result
    else:
        return "error".ljust(length," ")

part1 = get_1st_departure_xchar("IPNZ01",9)

part2 = get_1st_departure_xchar("IPNZ02",9)

text2send = '{} {}'.format(part1,part2)
print(text2send)
display = LCDBridge()
display.send2LCD(3, 1, text2send)








