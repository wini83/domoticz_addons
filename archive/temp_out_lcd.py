#!/usr/bin/python3

import config
from lib import lcdbridge
import DomoticzAPI as dom

LCD_ROW = 2
openweather = 6045



server = dom.Server(address=config.domoticz_ip, port=config.domoticz_port)

dev_openweather_ws = dom.Device(server, openweather)


print(dev_openweather_ws.temp)

print(dev_openweather_ws.barometer)


ergebnis = '{}C {}hPa'.format(dev_openweather_ws.temp, dev_openweather_ws.barometer)
print(ergebnis)

lcd = lcdbridge.LCDBridge()

lcd.send2LCD(LCD_ROW, 1, ergebnis)
