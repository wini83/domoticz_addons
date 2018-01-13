import RPi.GPIO as GPIO
import time

import os
import signal
import sys


tab = [17,27]
text = sys.argv[1]
print "Announce: "+text+"..."
try:
	#GPIO.setmode(GPIO.BCM) #(GPIO.BOARD)
	GPIO.setup(17,GPIO.OUT)
	time.sleep(3)
	GPIO.setup(27,GPIO.OUT)
	time.sleep(1)
	os.system("aplay gong.wav")
	os.system("./speech.sh "+text)
	time.sleep(1)
	GPIO.cleanup(27)
	time.sleep(2)
	
	#GPIO.output(tab,True)
	
	#GPIO.output(17,True)
	
	#time.sleep(5)
	#GPIO.output(27,True)
	#time.sleep(10)
	#GPIO.output(27,False)
	#time.sleep(5)
	#GPIO.output(17,False)
	
	#GPIO.output(17,False)
	

	GPIO.cleanup(tab) #wyczysc/zresetuj oba wyjscia
	

	#os.kill(os.getppid(),signal.SIGHUP) #zamyka okno

	
except KeyboardInterrupt:
	GPIO.cleanup()
