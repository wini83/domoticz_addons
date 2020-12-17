#!/usr/bin/python3

import config
import DomoticzAPI as dom

from lib import lcdbridge

LCD_ROW = 4
PM10_IDX = 5940
PM25_IDX = 5939


server = dom.Server(address=config.domoticz_ip, port=config.domoticz_port)

dev_pm10 = dom.Device(server, PM10_IDX)
dev_pm25 = dom.Device(server, PM25_IDX)

pm10_percentage = float(dev_pm10.data.strip('%')) / 100.0
pm25_percentage = float(dev_pm25.data.strip('%')) / 100.0



ergebnis = 'PM10:{:.0%} PM25:{:.0%}'.format(pm10_percentage, pm25_percentage).center(20)
print(ergebnis)

lcd = lcdbridge.LCDBridge()

lcd.send2LCD(4, 1, ergebnis)
