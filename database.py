
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import Base, Zone, Resident, House, Pet
import datetime

engine = create_engine('sqlite:///homeware.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)

    #import RPi.GPIO

    ###     the following functions simplify the process of calling database interactions

# Zone database connections

def addZone(zone):
    db_session.add(zone)
    db_session.commit()

def getAllZones():
    return Zone.query.all()

def getFirstZone():
    return Zone.query.first()

def getZoneByName(name):
    return Zone.query.filter(Zone.name == name).one()

def deleteZone(name):
    q = getZoneByName(name)
    db_session.delete(q)
    db_session.commit()


# Resident Database connections

def addResident(name):
    db_session.add(name)
    db_session.commit()

def getAllResidents():
    return Resident.query.all()

def getFirstResident():
    return Resident.query.first()

def getResidentByName(name):
    return Resident.query.filter(Resident.name == name).one()

def deleteResident(name):
    q = getResidentByName(name)
    db_session.delete(q)
    db_session.commit()

def deleteAllResidents():
    q = getAllResidents()
    db_session.delete(q)
    db_session.commit()

# House Database connections

def addHouse(house):
    db_session.add(house)
    db_session.commit()

def checkIfHouseExists():
    return House.query.one_or_none()

def getHouse():
    return House.query.one_or_none()

def getAllHouses():
    data = House.query.all()
    print (data)
    return House.query.all()

def getHouseByName(address):
    return House.query.filter(House.address == address).one()

def deleteHouse(address):
    q = getHouseByName(address)
    db_session.delete(q)
    db_session.commit()
    print('House deleted')

# Log Database Calls

def addDataPoint(datapoint):
    db_session.add(datapoint)
    db_session.commit()

# functions about the pet feeding schedule
def getTodaysPetInfo():
    current_date = datetime.datetime.utcnow()
    today = current_date - datetime.timedelta(days=1)
    q = Pet.query.filter(Pet.date <= today).all()
    return q

def getAllPetInfo():
    return Pet.query.all()

# Miscellaneous

def fedAnimals(fedAnimals):
    db_session.add(fedAnimals)
    db_session.commit()

def deleteAll():
    q = getAllHouses()
    r = getAllResidents()
    z = getAllZones()
    db_session.delete(q)
    db_session.delete(r)
    db_session.delete(z)
    db_session.commit()
    print('All house data deleted')
