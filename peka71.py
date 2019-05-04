# -*- coding: utf-8 -*-
'''
Created on 2 sty 2018


'''

from lcdbridge import LCDBridge

from pekaVMonitor import pekaVMonitor


LCD_ROW = 3
LCD_IP = "192.168.1.200"

monitor = pekaVMonitor()

odjazd1 = monitor.get_1st_departure("IPNZ01")

odjazd2 = monitor.get_1st_departure("IPNZ02")

print("Najbliższe odjazdy - kierunek {} linia {} odjazd za {} minut,".format(odjazd1[1].replace("Os.","osiedle"),odjazd1[0],odjazd1[2]))
print("kierunek {} linia {} odjazd za {} minut".format(odjazd2[1].replace("Os.","osiedle"),odjazd2[0],odjazd2[2]))
part1 = monitor.get_1st_departure_xchar("IPNZ01",9)
 
part2 = monitor.get_1st_departure_xchar("IPNZ02",9)


 
 
text2send = '{}  {}'.format(part1,part2)
print("{} + {} + 2 (space) = {}".format(len(part1),len(part2),len(text2send)))
display = LCDBridge()
print(display.remove_accents(text2send))
display.send2LCD(3, 1, text2send)








