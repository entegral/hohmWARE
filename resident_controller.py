__author__ = "Brewski"


import models
import database
import resident_view


import os, platform

def createNewResident():
	#need to finish this fucntion to add new residents and then make a function to delete them
	name = input('What is the name of the new resident?\n')
	email = input('What is the email of the new resident?\n')
	phone = input('What is the phone number of the new resident?\n')
	ip = input('What is the static IP address of the new resident?\n')
	mac = input('What is the mac address of the new resident?\n')
	newResident = models.Resident(name, email, phone, ip, mac)
	database.addResident(newResident)

def listAllResidents():
	residents = database.getAllResidents()
	resident_view.printAllResidents(residents)

def listFirstResident():
	resident = database.getFirstResident()
	resident_view.printResident(resident)

def listResidentByName():
	listAllResidentsData
	resident = database.getResidentByName(name)
	resident_view.printAllResident(resident)

def returnAllResidents():
	residents = database.getAllResidents()
	return residents

def returnResidentByName():
	name = input('What is the name of the resident you would like to get?\n')
	resident = database.getResidentByName(name)
	return resident

def updateResidentName():
	resident = database.getResidentByName()
	name = input('What is the new name of this user?\n')
	resident.name = name
	database.db_session.commit()

def deleteResident():
	database.deleteResident()

# resident monitor functions ##############################################################################################################

def startResidentMonitor():

	# get list of residents from the database and iterate through them checking 
	# for their presence on the local network, based on their static IPs and a ping
	
	residents = database.returnAllResidents
	for resident in residents:	
		# ping resident IP and set alarm state if nobody is home	
		resident_at_home = ping(resident.ip)
		if resident_at_home == True:					# set alarm state to OFF
			time.sleep()
		else:											# set alarm state to ON
			time.sleep(60)
			if ping(resident.ip) == False and :
				alarm_controller.runAlarm()				# wait 2 seconds, then ping the IP again to confirm resident is gone

			else:



	while True:
		time.sleep(0.01)


def ping(ipaddress):
    """
    Returns True if host responds to a ping request
    """

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"

    # Ping
    return os.system("ping " + ping_str + " " + ipaddress) == 0

