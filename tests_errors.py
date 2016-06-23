from zone_controller import *
from resident_controller import *

test = ''
while test == '':
	command = input ('___________________________________________\nzone_controller.py:	resident_controller.py:\n\ncreateNewZone		createNewResident\n\nlistAllZones		listAllResidents\nlistZoneByName		listResidentByName\n\nreturnAllZones		returnAllResidents\nreturnZonebyName	returnResidentByName\n\nupdateZoneName		updateResidentName\n\ndeleteZone		deleteResident\n___________________________________________\n')
	exec(command + '()')
	input ("Press 'enter' to continue...\n")