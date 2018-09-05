# -*- coding: utf-8 -*-

import domobridge as dom
import socket
import os
import urllib.request

CAM_SWITCH_IDX = 1094
MOTION_SWITCH_IDX = 4252

DOMOTICZ_IP = "192.168.1.100"
DOMOTICZ_PORT = "8050"

def is_Open(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False
    
def is_switchOn(idx):    
    try:
        server = dom.Server(address=DOMOTICZ_IP, port=DOMOTICZ_PORT)
        dev_cam_switch = dom.Device(server,idx)
        print("{} Status = {}".format(dev_cam_switch.name,dev_cam_switch.data))
        if(dev_cam_switch.data == "On"):
            return True
        elif(dev_cam_switch.data == "Off"):
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
        print ("kto to spieprzyl?")
        
def motion_detection_ctl(command):
    if command == "start":
        with urllib.request.urlopen('http://python.org/') as response:
            html = response.read()
    elif command == "stop":
        os.system("sudo systemctl stop motioneye")
    else:
        print ("kto to spieprzyl?")
            
    
motioneye_alive = is_Open("127.0.0.1", 8765)
camswitch_status = is_switchOn(CAM_SWITCH_IDX)





if (camswitch_status):
    print ('Camera Switch in Domoticz is On')
    if(motioneye_alive):
        print("MotionEye is running")
    else:
        print("MotionEye is inactive, Starting motionEye...")
        service_ctl("start")
else:
    print ('Camera Switch in Domoticz is Off')
    if(motioneye_alive):
        print("MotionEye is running, Stopping motionEye...")
        service_ctl("stop")
    else:
        print("MotionEye is inactive")
    
