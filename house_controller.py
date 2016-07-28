import models, database, resident_controller, zone_controller

import time
from datetime import datetime
from twilio.rest import TwilioRestClient



# house alarm related functions:

def broadcastSMS(note, residents):

	"""
	This function receives a string and sends it to residents as a text message.
	"""

	accountSID = 'AC4ef5b1267687ff3f1984829aa9e13f8b'
	authToken = 'afbcc30cede0b005efa5b9c20e365749'
	twilioCli = TwilioRestClient(accountSID, authToken)
	myTwilioNumber = '+15415000742'
	for resident in residents:
		mobile = str(resident.phone)
		message = twilioCli.messages.create(body = note, from_ = myTwilioNumber, to = mobile)
		time.sleep(0.01)



# house obj related functions:

def houseDataLogger():
	"""
	This function should take a data point every 2 minutes and persist it to
	the database.
	"""
	# take snapshot of every sensor and save their states/values
	while True:
		timestamp = datetime.now()
		temperature = zone_controller.scanTemps 						# NEED TO ADD FUNCTION TO SCAN AND RETURN TEMPERATURES AROUND THE HOUSE
		open_doors = zone_controller.door								# take pictures with all cameras and sensors

		dp = models.Data_Point(timestamp, temperature, open_doors)
		time.sleep(5)

def createNewHouse():
	if database.checkIfHouseExists() == None:
		house = models.House()
		database.addHouse(house)
		resident_controller.setupResidents()
		zone_controller.setupZones()
	else:
		print ("House already exists!")
