__author__ = "Brewski"

# import RPi.GPIO as GPIO
# import thread

import zone_controller, resident_controller, house_controller
import models, database



# GPIO.setmode(GPIO.BOARD)
database.init_db()

# ___________________________________________________________________________
# Config yo shit:
# ___________________________________________________________________________

#### check to see if house object is already in database, if not, add one
house_controller.createNewHouse()


#### assign zones to GPIO pins
# zones = database.getAllZones()
# for zone in zones:
# 	GPIO.setup(zone.channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# GPIO.setup(2, GPIO.OUT)
# GPIO.output(2, GPIO.HIGH)


# ___________________________________________________________________________
# spin up threads for monitoring various modules
# ___________________________________________________________________________

#### Zone state monitor
# thread.start_new_thread( zone_controller.startZoneMonitor() )
# #### Resident Occupancy Monitor
# thread.start_new_thread( resident_controller.startResidentMonitor() )
# #### House data logger
# thread.start_new_thread( house_controller.houseDataLogger() )
