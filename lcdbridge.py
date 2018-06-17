import urllib2
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
        urlOut = lcdUrl+str(row)+",1,"+urllib2.quote(payload)
        print(urlOut)
        request2 = urllib2.Request(urlOut)
        response2 = urllib2.urlopen(request2)
