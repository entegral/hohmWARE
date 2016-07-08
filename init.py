__author__ = "Brewski"

# import RPi.GPIO as GPIO
# import thread

import zone_controller, resident_controller, house_controller
import models, database



# GPIO.setmode(GPIO.BOARD)
database.init_db()

# Config:

#### check to see if house is already configured in database, if not, add house
if database.checkIfHouseExists() == None:
	house_controller.createNewHouse()
else:
	print('\nHome already configured!\n')


#### assign zones to GPIO pins
zones = database.getAllZones()    				
for zone in zones:
	GPIO.setup(zone.channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)					
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, GPIO.HIGH)

#### activate or config any other home automation functions

	

# start up / load a house object to store house data state information


# spin up threads for monitoring various modules

#### Zone state monitor
thread.start_new_thread( zone_controller.startZoneMonitor() )
#### Resident Occupancy Monitor
thread.start_new_thread( resident_controller.startResidentMonitor() )
#### House data monitor





