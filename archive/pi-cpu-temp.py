from gpiozero import CPUTemperature
import DomoticzAPI as dom
import config

cpu = CPUTemperature()
print(cpu.temperature)

server = dom.Server(address=config.domoticz_ip, port=config.domoticz_port)

dev_temperature = dom.Device(server, config.camera_cpu_temp_idx)
dev_temperature.update(0, cpu.temperature, None, None)