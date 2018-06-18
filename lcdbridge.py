# -*- coding: utf-8 -*-
import urllib2
import string
from unidecode import unidecode
import unicodedata
'''
Created on 17 cze 2018

@author: Mariusz Wincior
'''
#lcdUrl = "http://192.168.1.200/control?cmd=lcd,"
class LCDBridge:
    lcd_ip = "192.168.1.200"
    lcd_rows = 4
    lcd_cols = 20
    def send2LCD(self, row,col, payload):
        lcdUrl = "http://" + self.lcd_ip + "/control?cmd=lcd,"
        text2send = self.remove_accents(payload)
        urlOut = lcdUrl+str(row)+",1,"+urllib2.quote(text2send)
        print(urlOut)
        request2 = urllib2.Request(urlOut)
        response2 = urllib2.urlopen(request2)
    
    def remove_accents(self,input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str.decode("utf-8"))
        only_ascii = nfkd_form.encode('ASCII', 'ignore')
        return only_ascii
        
    