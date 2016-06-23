__author__ = "Brewski"


import models
import database
import zone_view

# Create new zones
def createNewZone():
	name = input('What would you like to call the new zone?')
	gpio = input('What gpio would you like to give the new zone?')
	newZone = models.Zone(name, gpio)
	database.addZone(newZone)
	message = " '%s' zone has been added to the database.\n " % (name)
	print (message)

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
	name = input('What is the name of the zone you would like to get?')
	zone = database.getZoneByName(name)
	return zone	


# Update Zone functions
def updateZoneName():
	listAllZones()
	zone = database.getZoneByName()
	name = input("What would you like to rename '%s' to?" % (zone.name))
	zone.name = name
	database.db_session.commit()


# Delete Zone Functions
def deleteZone():
	name = input('What is the name of the zone you would like to delete?')
	database.deleteZone(name)



# zone monitor functions

def startZoneMonitor():
	
	zones = database.returnAllZones
	for zone in zones:
		GPIO.add_event_detect(zone.channel, GPIO.RISING, callback=doorClosed())
		GPIO.add_event_detect(zone.channel, GPIO.FALLING, callback=doorOpened())
	while True:
		time.sleep(1/5)





def doorOpened():
	print ("AYYYYE, THE BLAST DOOR HAS BEEN BREACHED!!!")


def doorClosed():
	print ("Ayyyyyyye, de doors be calmer than a whooooores tit.")



