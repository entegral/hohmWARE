from zone_controller import listAllZones, listZoneByName, returnAllZones, returnZoneByName, updateZoneName, createNewZone, deleteZone
from resident_controller import listAllResidents, listResidentByName, returnAllResidents, returnResidentByName, updateResidentName, createNewResident, deleteResident
import database

import database

test = ''
while test == '':
	try:
		command = input ('___________________________________________\nzone_controller.py:	resident_controller.py:\n\ncreateNewZone		createNewResident\n\nlistAllZones		listAllResidents\nlistZoneByName		listResidentByName\n\nreturnAllZones		returnAllResidents\nreturnZonebyName	returnResidentByName\n\nupdateZoneName		updateResidentName\n\ndeleteZone		deleteResident\n___________________________________________\n')
		exec(command)
		print ('\n')
		test = input("Press 'enter' to continue or 'q' to quit.\n")
	except:
		print ('\n***********************************\noops, an error occured, try again!\n***********************************')
		test = input("Press 'enter' to continue or 'q' to quit.\n")