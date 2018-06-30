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

def truncateUTF8length(unicodeStr, maxsize):
    ur""" This method can be used to truncate the length of a given unicode
        string such that the corresponding utf-8 string won't exceed
        maxsize bytes. It will take care of multi-byte utf-8 chars intersecting
        with the maxsize limit: either the whole char fits or it will be
        truncated completely. Make sure that unicodeStr is in Unicode
        Normalization Form C (NFC), else strange things can happen as
        mentioned in the examples below.
        Returns a unicode string, so if you need it encoded as utf-8, call
        .decode("utf-8") after calling this method.
        >>> truncateUTF8lengthIfNecessary(u"ö", 2) == (u"ö", False)
        True
        >>> truncateUTF8length(u"ö", 1) == u""
        True
        >>> u'u1ebf'.encode('utf-8') == 'xe1xbaxbf'
        True
        >>> truncateUTF8length(u'hiu1ebf', 2) == u"hi"
        True
        >>> truncateUTF8lengthIfNecessary(u'hiu1ebf', 3) == (u"hi", True)
        True
        >>> truncateUTF8length(u'hiu1ebf', 4) == u"hi"
        True
        >>> truncateUTF8length(u'hiu1ebf', 5) == u"hiu1ebf"
        True

        Make sure the unicodeStr is in NFC (see unicodedata.normalize("NFC", ...) ).
        The following would not be true, as e and u'u0301' would be seperate
        unicode chars. This could be handled with unicodedata.combining
        and a loop deleting chars from the end until after the first non
        combining char, but this is _not_ done here!
        #>>> u'eu0301'.encode('utf-8') == 'exccx81'
        #True
        #>>> truncateUTF8length(u'eu0301', 0) == u"" # not in NFC (u'xe9'), but in NFD
        #True
        #>>> truncateUTF8length(u'eu0301', 1) == u"" #decodes to utf-8: 
        #True
        #>>> truncateUTF8length(u'eu0301', 2) == u""
        #True
        #>>> truncateUTF8length(u'eu0301', 3) == u"eu0301"
        #True
        """
    return unicode(unicodeStr.encode("utf-8")[:maxsize], "utf-8", errors="ignore")

def get_1st_departure(bollard):
    json_data = peka_vm_get('getTimes','{"symbol":"'+bollard+'"}')
    try:
        departure = json_data["success"]["times"][0]
        
        result = '{}>{}:{}m'.format(departure["line"],departure["direction"].replace(" ", "").encode('UTF-8')[0:7],departure["minutes"]).ljust(15," ")
        return result
    except:
        return "error".ljust(15," ")

text2send = get_1st_departure("IPNZ01")
print(text2send)
display = LCDBridge()
display.send2LCD(3, 1, text2send)








