from syngeosPoller import SyngeosPoller
import DomoticzAPI as dom
import config
DEV_ID = 567

poller = SyngeosPoller(DEV_ID)

poller.poll()

print(poller.humidity)
print(poller.air_pressure)
print(poller.pm2_5)
print(poller.pm10)
print(poller.pm2_5_threshold)
print(poller.pm10_threshold)


print(poller.pm10_percentage)

server = dom.Server(address=config.domoticz_ip, port=config.domoticz_port)
dev_temperature = dom.Device(server, config.syngeos_temp_idx)

