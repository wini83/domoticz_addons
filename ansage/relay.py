import RPi.GPIO as GPIO
import time

import os
import signal
import sys
from playsound import playsound
import pyglet





tab = [17,27]
text = sys.argv[1]
print "Announce: "+text+"..."
try:
	#GPIO.setmode(GPIO.BCM) #(GPIO.BOARD)
	GPIO.setup(17,GPIO.OUT)
	time.sleep(3)
	GPIO.setup(27,GPIO.OUT)
	time.sleep(1)
	music = pyglet.resource.media('gong.wav')
	music.play()
	pyglet.app.run()

	time.sleep(1)
	GPIO.cleanup(27)
	time.sleep(2)

	

	GPIO.cleanup(tab)


	
except KeyboardInterrupt:
	GPIO.cleanup()
