import models, database, resident_controller, zone_controller

import time
from twilio.rest import TwilioRestClient



# house alarm related functions:

def broadcastSMS(note):
	
	""" this function receives a string and sends it to residents as a text message"""

	accountSID = 'AC4ef5b1267687ff3f1984829aa9e13f8b'
	authToken = 'afbcc30cede0b005efa5b9c20e365749'
	twilioCli = TwilioRestClient(accountSID, authToken)
	myTwilioNumber = '+15415000742'
	resident = database.getAllResidents()
	for resident in residents:	
		mobile = str(resident.phone)
		message = twilioCli.messages.create(body = note, from_ = myTwilioNumber, to = mobile)
		time.sleep(0.01)



# house obj related functions:

def houseMonitor():
	# take snapshot of every sensor and save their states
	pass

def notifyResidents():
	# send a text message / email notifying admin(s) of alarm status
	pass

def createNewHouse():
	address = input("What is the address of your house?\n")
	resident_controller.setupResidents()
	zone_controller.setupZones()
	temperatures = []
	house = models.House(address= address)
	database.addHouse(house)



