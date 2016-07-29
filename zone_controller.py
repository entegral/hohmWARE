__author__ = "Brewski"

# import RPi.GPIO as GPIO

import models, database, zone_view, house_controller


# Create new zones
def createNewZone():
	name = input('What would you like to call the new zone?\n')
	gpio = input('What gpio would you like to give the new zone?\n')
	newZone = models.Zone(name, gpio)
	database.addZone(newZone)
	message = " '%s' zone has been added to the database.\n " % (name)
	print (message)

def setupZones():
	# input specific data for each zone
	numberofzones = input('how many zones would you like to setup?\n')
	current_zone = 0
	while current_zone <= int(numberofzones) - 1:
	    createNewZone()
	    current_zone = current_zone + 1


# Display/print Zone functions
def listAllZones():
	zones = database.getAllZones()
	zone_view.printZoneNames(zones)

def listFirstZone():
	zone = database.getFirstZone()
	zone_view.printZoneName(zone)

def listZoneByName():
	listAllZones()

	zone = database.getZoneByName(name)
	zone_view.printZoneName(zone)


# Read and/or return zone functions
def returnAllZones():
	zones = database.getAllZones()
	return zones

def returnZoneByName():
	listAllZones()
	name = input('What is the name of the zone you would like to get?\n')
	zone = database.getZoneByName(name)
	return zone


# Update Zone functions
def updateZoneName():
	listAllZones()
	zone = database.getZoneByName()
	name = input("What would you like to rename '%s' to?\n" % (zone.name))
	zone.name = name
	database.db_session.commit()


# Delete Zone Functions
def deleteZone():
	name = input('What is the name of the zone you would like to delete?\n')
	database.deleteZone(name)



# zone monitor functions

def startZoneMonitor():

	zones = database.returnAllZones()
	for zone in zones:
		GPIO.add_event_detect(zone.channel, GPIO.RISING, callback=doorClosed())
		GPIO.add_event_detect(zone.channel, GPIO.FALLING, callback=doorOpened())

def doorOpened():

	""" This function sends out an alert if:
		(1) when the front door has opened,
		and (2) if nobody is home """

	message_to_residents = 'Wake up lads! Flint has  boarrded the ship!'
	if resident_controller.residentsAtHome() == False:
		house_controller.sendSMS(message_to_residents, database.getAllResidents())
		house_controller.securityLogger()


def doorClosed():
	print ("Ayyyyyyye, de doors be more lonely than a whooooores tit.")

def doorCheck():
	"""This function checks the state of each door and returns a list of the names of the
	doors that are currently open."""
	zones = database.returnAllZones()
	open_doors = []
	for zone in zones:
		state = GPIO.input(zone.channel)
		if state == 1:
			open_doors.append(zone.name)
	return open_doors
