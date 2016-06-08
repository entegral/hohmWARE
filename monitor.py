__author__ = "Brewski"

import RPi.GPIO as GPIO
import zone_controller
import resident_controller

GPIO.setmode(GPIO.BCM)

# Config:

#### assign zones to GPIO pins
zones = database.getAllZones()    				
for zone in zones:
	GPIO.setup(zone.channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)					
GPIO.output(2, GPIO.HIGH)

#### activate or config any other functions of the monitor






# create a loop that constantly checks the pin state of each zone
alarm = True
while alarm:
	GPIO.add_event_detect(zones, GPIO.BOTH, callback=my_callback)  





# if program ever needs to break this code will reset and safeguard all the pins
GPIO.cleanup()