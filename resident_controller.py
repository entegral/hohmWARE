__author__ = "Brewski"


import models, database, resident_view, house_controller


import os, platform

def createNewResident(name, email, user_pin, phone, ip, mac):
	role = "resident"
	newResident = models.Resident(name, email, user_pin, phone, ip, mac, role)
	database.addResident(newResident)

def createNewAdmin():
	#need to finish this fucntion to add new residents and then make a function to delete them
	name = input('What is the name of the first resident?\n This resdent will be the house administrator.\n')
	email = input('What is the email of this resident?\n')
	user_pin = input('Please choose a pin number (4 digits).\n')
	phone = input('What is the phone number of this resident?\n')
	ip = input('What is the static IP address of this resident?\n')
	mac = input('What is the mac address of this resident?\n')
	role = "admin"
	newAdmin = models.Resident(name, email, user_pin, phone, ip, mac, role)
	database.addResident(newResident)


def setupResidents():
	numberofresidents = input('How many residents would you like to add to the home?\n The first resident will be made the administrator.\n')
	current_resident = 0
	createNewAdmin()
	current_resident + 1
	while current_resident <= int(numberofresidents) - 1:
	    createNewResident()
	    current_resident = current_resident + 1


# resident monitor functions ##############################################################################################################

def residentsAtHome():

	"""
	get list of residents from the database and iterate through them checking
	for their presence on the local network, based on their static IPs and a
	ping function. Returns a list of residents who are home.
	"""

	residents = database.returnAllResidents()
	residents_at_home = []
	for resident in residents:								# ping resident IP and set alarm state if nobody is home
		if ping(resident.ip) == True:						# set alarm state to OFF
			residents_at_home.append(resident.name)
			time.sleep(0.01)
		else:												# set alarm state to ON
			time.sleep(3)
			if ping(resident.ip) == True:
				residents_at_home.append(resident.name)		# wait 60 seconds, then ping the IP again to confirm resident is gone, if so, break without adding to residents_at_home
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
