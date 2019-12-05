# -*- coding: utf-8 -*-
import urllib.request
import unicodedata
'''
Created on 17 cze 2018

@author: Mariusz Wincior
'''
#lcdUrl = "http://192.168.2.200/control?cmd=lcd,"
class LCDBridge:
    lcd_ip = "192.168.2.200"
    lcd_rows = 4
    lcd_cols = 20
    def send2LCD(self, row,col, payload):
        lcdUrl = "http://" + self.lcd_ip + "/control?cmd=lcd,"
        text2send = self.remove_accents(payload)
        urlOut = lcdUrl+str(row)+",1,"+urllib.request.quote(text2send)
        print(urlOut)
        request2 = urllib.request.Request(urlOut)
        response2 = urllib.request.urlopen(request2)
    
    def remove_accents(self,input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        only_ascii = nfkd_form.encode('ASCII', 'ignore')
        return only_ascii
        
    