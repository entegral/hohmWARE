import sqlite3
from database import init_db, db_session
from models import Zone, House, Resident

#initialize the sqlalchemy/sqlite database
init_db()

###  ask for input about the home and save into variables  ###
numberofzones = input('How many zones would you like to setup?\n')
numberofresidents = input('How many people live in your home?\n')


#  data input specific for each zone  #
current_zone = 0
while current_zone <= numberofzones - 1:
	zone_name = raw_input('What would you like to call zone %s ?' % (current_zone + 1))
	gpio_input = raw_input('What pin on the raspberry pi are you connecting this zone to?\n')
	z = Zone(zone_name,gpio_input)
	db_session.add(z)
	db_session.commit()
	current_zone = current_zone + 1
	print "'%s' zone has been added to the database.\n" % (zone_name)

#  data input specific for each person in the home #
current_resident = 0
while current_resident <= numberofresidents - 1:
	res_name = raw_input('What is the name of resident number %s ?\n' % (current_resident + 1))
	res_email = raw_input("What is %s's email address?\n" % (res_name))
	res_phone = raw_input("What is %s's cell phone number ?\n" % (res_name))
	res_mac = raw_input("What is the MAC address of %s's cell phone?\n" % (res_name))
	r = Resident(res_name, res_email, res_phone, res_mac)
	current_resident = current_resident + 1

# save data to shelf for persistence #
configfile = shelve.open('homeconfig')
configfile['residents'] = residents
configfile['zones'] = zones
configfile.close()

