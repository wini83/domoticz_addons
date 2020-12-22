#!/usr/bin/python3

import config
import DomoticzAPI as dom

from lib import lcdbridge

PM10_IDX = 5940
PM25_IDX = 5939

def compose_row(pm10,pm25):
    pm10_percentage = float(pm10.data.strip('%')) / 100.0
    pm25_percentage = float(pm25.data.strip('%')) / 100.0
    ergebnis = 'PM10:{:.0%} PM25:{:.0%}'.format(pm10_percentage, pm25_percentage).center(20)
    print(ergebnis)
    return ergebnis


server = dom.Server(address=config.domoticz_ip, port=config.domoticz_port)

dev_airly_pm10 = dom.Device(server, PM10_IDX)
dev_airly_pm25 = dom.Device(server, PM25_IDX)

dev_syngeos_pm10 = dom.Device(server, config.syngeos_pm_10_norm)
dev_syngeos_pm25 = dom.Device(server, config.syngeos_pm_2_5_norm)


lcd = lcdbridge.LCDBridge()

lcd.send2LCD(3, 1, compose_row(dev_airly_pm10,dev_airly_pm25))
lcd.send2LCD(4, 1, compose_row(dev_syngeos_pm10,dev_syngeos_pm25))
