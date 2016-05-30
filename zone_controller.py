__author__ = "Brewski"


import models
import database
import zone_view

# Display/print Zone functions
def listAllZones():
	zones = database.getAllZones()
	zone_view.printZones(zones)

def listFirstZone():
	zone = database.getFirstZone()
	zone_view.printZone(zone)

def listZoneByName():
	listAllZones()
	zone = database.getZoneByName(name)
	zone_view.printZone(zone)


# Read and/or return zone functions
def returnAllZones():
	zones = database.getAllZones()
	return zones

def returnZoneByName():
	listAllZones()
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
def deleteZoneGPIO():
	zone = database.getZoneByName()
	zone.delete()



# test stuff below here
# listFirstZone()
