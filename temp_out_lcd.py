#!/usr/bin/python3

import config
import lcdbridge
import DomoticzAPI as dom

LCD_ROW = 2
openweather = 6045



server = dom.Server(address=config.domoticz_ip, port=config.domoticz_port)

dev_openweather_ws = dom.Device(server, openweather)


print(dev_openweather_ws.data)

print(dev_openweather_ws.temp)

print(dev_openweather_ws.barometer)

#pm10_percentage = float(dev_pm10.data.strip('%')) / 100.0




#ergebnis = 'PM10:{:.0%} PM25:{:.0%}'.format(pm10_percentage, pm25_percentage).center(20)
#print(ergebnis)

#lcd = lcdbridge.LCDBridge()

#lcd.send2LCD(4, 1, ergebnis)
