# -*- coding: utf-8 -*-

import domobridge as dom
import socket
import os

CAM_SWITCH_IDX = 1094
MOTION_SWITCH_IDX = 9999

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
        os.system("sudo systemctl stop motioneye")
    elif command == "stop":
        os.system("sudo systemctl stop motioneye")
    else:
        print ("kto to spieprzyl")
            
    
motion_alive = is_Open("127.0.0.1", 8765)
switch_status = is_switchOn(CAM_SWITCH_IDX)



if switch_status == True and motion_alive == True:
    print ('Switch is On and Service is running, no Action required.')
elif switch_status == True and motion_alive == False:
    print ('Switch is On and Service is inactive, Starting service...')
    service_ctl("start")
elif switch_status == False and motion_alive == False:
    print ('Switch is Off and Service is inactive, no Action required.')
else:
    print ('Switch is On and Service is running, Stopping service...')
    service_ctl("stop")