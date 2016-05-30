import sqlite3
import database
from models import Zone, House, Resident

#initialize the sqlalchemy/sqlite database
database.init_db()

###  ask for input about the home and save into variables  ###
numberofzones = input('How many zones would you like to setup?\n')
numberofresidents = input('How many people live in your home?\n')


#  data input specific for each zone  #
current_zone = 0
while current_zone <= int(numberofzones) - 1:
    zone_name = input('What would you like to call zone %s ?' % (current_zone + 1))
    gpio_input = input('What pin on the raspberry pi are you connecting this zone to?\n')
    zone = Zone(zone_name,gpio_input)
    try:
        database.addZone(zone)
    except:
        print ("Zone is already in database")
    current_zone = current_zone + 1
    message = " '%s' zone has been added to the database.\n " % (zone_name)
    print (message)

#  data input specific for each person in the home #
current_resident = 0
while current_resident <= int(numberofresidents) - 1:
    res_name = input('What is the name of resident number %s ?\n' % (current_resident + 1))
    res_email = input("What is %s's email address?\n" % (res_name))
    res_phone = input("What is %s's cell phone number ?\n" % (res_name))
    res_mac = input("What is the MAC address of %s's cell phone?\n" % (res_name))
    resident = Resident(res_name, res_email, res_phone, res_mac)
    database.addResident(resident)
    current_resident = current_resident + 1

