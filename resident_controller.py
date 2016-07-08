__author__ = "Brewski"


import models, database, resident_view, house_controller


import os, platform

def createNewResident():
	#need to finish this fucntion to add new residents and then make a function to delete them
	name = input('What is the name of the new resident?\n')
	email = input('What is the email of the new resident?\n')
	phone = input('What is the phone number of the new resident?\n')
	ip = input('What is the static IP address of the new resident?\n')
	mac = input('What is the mac address of the new resident?\n')
	newResident = models.Resident(name= name, email= email, phone= phone, ip= ip, mac= mac)
	database.addResident(newResident)

def setupResidents():
	numberofresidents = input('How many residents would you like to add to the home?\n')
	current_resident = 0
	while current_resident <= int(numberofresidents) - 1:
	    createNewResident()
	    current_resident = current_resident + 1

# resident monitor functions ##############################################################################################################

def residentsAtHome():
	
	"""
	get list of residents from the database and iterate through them checking 
	for their presence on the local network, based on their static IPs and a ping function
	"""

	residents = database.returnAllResidents
	residents_at_home = []
	for resident in residents:								# ping resident IP and set alarm state if nobody is home	
		if ping(resident.ip) == True:						# set alarm state to OFF
			residents_at_home.append(resident.name)
			time.sleep(0.01)
		else:												# set alarm state to ON
			time.sleep(3)
			if ping(resident.ip) == True:
				residents_at_home.append(resident.name)		# wait 60 seconds, then ping the IP again to confirm resident is gone, if so, break without adding to residents_at_home
			else:
				pass
	if len(residents_at_home) > 0:
		result = True
	else:
		result = False
	return result
	

def ping(ipaddress):
    
    """
    Returns True if host responds to a ping request
    """

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"

    # Ping
    return os.system("ping " + ping_str + " " + ipaddress) == 0


# Generic resident functions

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
	name = input('What resident would you like to delete?\n')
	database.deleteResident(name)
