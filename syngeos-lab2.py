import config
from lib.syngeosPoller import SyngeosPoller

poller = SyngeosPoller(config.location)

dicto = poller.get_nearby_sensors()

print(len(dicto))

# pm10 = poller.get_all_devices()
#
# print(len(pm10))
#
# for item in pm10:
#     print(f'{item.sensor_type}  {item.distance:.1f} km ID:{item.id} {item.city} {item.address})')
