from time import sleep

from datetime import datetime

import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


def set_sw(client, cmd, not_fake):
    if not_fake:
        if cmd:
            client.publish("zigbee2mqtt/ikea_outlet2/set", payload='{"state": "ON"}')
        else:
            client.publish("zigbee2mqtt/ikea_outlet2/set", payload='{"state": "OFF"}')
    print("{} Command: {}".format(datetime.now().strftime("%H:%M:%S"), cmd))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("wini", password="dupa")
client.connect("192.168.2.100", 1883, 60)

real = False

set_sw(client, False, real)

print("{} Ignition system start".format(datetime.now().strftime("%H:%M:%S")))
sleep(10)

for x in range(1, 6):
    print("Iteration: {}".format(x))
    set_sw(client, True, real)
    sleep(5)
    set_sw(client, False, real)
    sleep(5)

set_sw(client, True, real)

