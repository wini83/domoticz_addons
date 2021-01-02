# -*- coding: utf-8 -*-

import DomoticzAPI as dom
import socket
import os
import urllib.request

CAM_SWITCH_IDX = 1094
MOTION_SWITCH_IDX = 4252

DOMOTICZ_IP = "192.168.2.100"
DOMOTICZ_PORT = "8050"


def is_open(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except socket.error as msg:
        print(msg)
        return False


def is_switch_on(idx):
    try:
        server = dom.Server(address=DOMOTICZ_IP, port=DOMOTICZ_PORT)
        dev_cam_switch = dom.Device(server, idx)
        print("{} Status = {}".format(dev_cam_switch.name, dev_cam_switch.data))
        if dev_cam_switch.data == "On":
            return True
        elif dev_cam_switch.data == "Off":
            return False
        else:
            return True
    except:
        return True


def service_ctl(command):
    if command == "start":
        os.system("sudo systemctl start motioneye")
    elif command == "stop":
        os.system("sudo systemctl stop motioneye")
    else:
        print("Wrong parameter")


def motion_detection_ctl(command):
    if command == "start":
        with urllib.request.urlopen('http://127.0.0.1:7999/1/detection/pause') as response:
            html = response.read()
    elif command == "stop":
        with urllib.request.urlopen('http://127.0.0.1:7999/1/detection/pause') as response:
            html = response.read()
    else:
        print("Wrong parameter")


motioneye_alive = is_open("127.0.0.1", 8765)
cam_switch_status = is_switch_on(CAM_SWITCH_IDX)

if cam_switch_status:
    if motioneye_alive:
        print("MotionEye is running")
    else:
        print("MotionEye is inactive, Starting motionEye...")
        service_ctl("start")
    if is_switch_on(MOTION_SWITCH_IDX):
        print("Starting Motion Detection")
        motion_detection_ctl("start")
    else:
        print("Pausing Motion Detection")
        motion_detection_ctl("stop")
else:
    if motioneye_alive:
        print("MotionEye is running, Stopping motionEye...")
        service_ctl("stop")
    else:
        print("MotionEye is inactive")
