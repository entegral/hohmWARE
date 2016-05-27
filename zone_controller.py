import models
import database
import zone_view


def listAllZones():
	zones = database.getAllZones()
	zone_view.printZones(zones)

def listFirstZone():
	zone = database.getFirstZone()
	zone_view.printZone(zone)
