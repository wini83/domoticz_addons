#!/usr/bin/python3
import json
import domobridge
import lcdbridge



LCD_ROW = 4
PM10_IDX = 5940
PM25_IDX = 5939


server = domobridge.Server(address="192.168.1.100", port="8050")

dev_pm10 = domobridge.Device(server, PM10_IDX)
dev_pm25 = domobridge.Device(server, PM25_IDX)

pm10_percentage = float(dev_pm10.data.strip('%')) / 100.0
pm25_percentage = float(dev_pm25.data.strip('%')) / 100.0



ergebnis = 'PM10:{:.0%} PM25:{:.0%}'.format(pm10_percentage, pm25_percentage).center(20)
print(ergebnis)

lcd = lcdbridge.LCDBridge()

lcd.send2LCD(4, 1, ergebnis)
