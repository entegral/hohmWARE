__author__ = "Brewski"

import RPi.GPIO as GPIO
import thread

import zone_controller, resident_controller, monitor_controller
import models, database



GPIO.setmode(GPIO.BCM)
database.init_db()

# Config:

#### assign zones to GPIO pins
zones = database.getAllZones()    				
for zone in zones:
	GPIO.setup(zone.channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)					
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, GPIO.HIGH)

#### activate or config any other functions of the monitor





# call for a loop that constantly checks the pin state of each zone

#### start zone_monitor
#### 


thread.start_new_thread( zone_controller.startZoneMonitor() )

	  





# if program ever needs to break this code will reset and safeguard all the pins
#GPIO.cleanup()