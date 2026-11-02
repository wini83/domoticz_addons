from lib.syngeosPoller import SyngeosPoller
import DomoticzAPI as dom
import config

DEV_ID = 111

poller = SyngeosPoller(DEV_ID)

poller.poll()
print("Temperature :{} {}".format(poller.temperature, poller.UNIT_TEMP))
print("Humidity :{} {}".format(poller.humidity, poller.UNIT_HUM))

print("Air pressure :{} {}".format(poller.air_pressure, poller.UNIT_air_pressure))

print("PM 10 :{} {}".format(poller.pm10, poller.UNIT_PM))

print("PM 10 norm :{} {}".format(poller.pm10_threshold, poller.UNIT_PM))

print("PM 10 norm % :{} {}".format(poller.pm10_percentage, "%"))

print("PM 2,5 :{} {}".format(poller.pm2_5, poller.UNIT_PM))

print("PM 2,5 norm :{} {}".format(poller.pm2_5_threshold, poller.UNIT_PM))

print("PM 2,5 norm % :{} {}".format(poller.pm2_5_percentage, "%"))


server = dom.Server(address=config.domoticz_ip, port=config.domoticz_port)

dev_temperature = dom.Device(server, config.syngeos_temp_idx)
dev_temperature.update(0, poller.temperature, None, None)

dev_hum = dom.Device(server, config.syngeos_hum_idx)
dev_hum.update(poller.humidity, None, None, None)


dev_air_press = dom.Device(server, config.syngeos_air_pressure_idx)
dev_air_press.update(0, "{};{}".format(poller.air_pressure, 0), None, None)

dev_pm_2_5_norm = dom.Device(server, config.syngeos_pm_2_5_norm)
dev_pm_2_5_norm.update(0, poller.pm2_5_percentage, None, None)

dev_pm_10_norm = dom.Device(server, config.syngeos_pm_10_norm)
dev_pm_10_norm.update(0, poller.pm10_percentage, None, None)
