from classes2 import Zone
import sqlite3
from database.py import init_db
from models.py import Zone, House



###  ask for input about the home and save into variables  ###
numberofzones = input('How many zones would you like to setup?\n')
numberofresidents = input('How many people live in your home?\n')


#  data input specific for each zone  #
current_zone = 0
while current_zone <= numberofzones - 1:
	zone_name = raw_input('What would you like to call zone %s ?' % (current_zone + 1))
	gpio_input = raw_input('What pin on the raspberry pi are you connecting this zone to?\n')
	z = Zone(zone_name,gpio_input)
	current_zone = current_zone + 1

#  data input specific for each person in the home #
n = 0
while n <= numberofresidents - 1:
	if n == 0:
		response = raw_input("Who is the admin of the house?")

		n = n + 1
		print residents
	else:
		residents.append(raw_input("What is the name of roommate # %s?" % (str(n))))
		n = n + 1
		print residents

# save data to shelf for persistence #
configfile = shelve.open('homeconfig')
configfile['residents'] = residents
configfile['zones'] = zones
configfile.close()

#initialize the sqlalchemy/sqlite database
init_db()