from models import Zone, House, Resident
import zone_controller, resident_controller, database

import RPi.GPIO as GPIO
import sqlite3

"""This script runs if no database information exists, or if the database has been cleared."""

#  ask for input about the home and save into variables
numberofzones = input('How many zones would you like to setup?\n')
numberofresidents = input('How many people live in your home?\n')


#  data input specific for each zone  
current_zone = 0
while current_zone <= int(numberofzones) - 1:
    zone_controller.createNewZone()
    current_zone = current_zone + 1

#  data input specific for each person in the home
current_resident = 0
while current_resident <= int(numberofresidents) - 1:
    resident_controller.createNewResident()
    current_resident = current_resident + 1

# create house object
house = database.checkIfHouseExists()
if house == None:
	house_controller.createNewHouse()