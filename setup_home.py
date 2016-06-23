import sqlite3
import database
from models import Zone, House, Resident
import zone_controller, resident_controller

#initialize the sqlalchemy/sqlite database
database.init_db()

###  ask for input about the home and save into variables  ###
numberofzones = input('How many zones would you like to setup?\n')
numberofresidents = input('How many people live in your home?\n')


#  data input specific for each zone  #
current_zone = 0
while current_zone <= int(numberofzones) - 1:
    zone_controller.createNewZone()
    current_zone = current_zone + 1

#  data input specific for each person in the home #
current_resident = 0
while current_resident <= int(numberofresidents) - 1:
    resident_controller.createNewResident()
    current_resident = current_resident + 1

