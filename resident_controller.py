__author__ = "Brewski"


import models
import database
import zone_view


def listAllResidents():
	residents = database.getAllResidents()
	zone_view.printAllResidentsData(residents)

def listFirstResident():
	resident = database.getFirstResident()
	zone_view.printResidentData(resident)

def listResidentByName():
	listAllResidentsData
	resident = database.getResidentByName(name)
	zone_view.printAllResidentData(resident)

def returnAllResidents():
	residents = database.getAllResidents()
	return residents

def returnResidentByName():
	resident = database.getResidentByName()
	return resident

def updateResidentName():
	resident = database.getResidentByName()
	name = input('What is the new name of this user?')
	resident.name = name
	database.db_session.commit()


# test stuff below here

