
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import Base, Zone, Resident, House

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

# Zone database connections

def addZone(zone):
    db_session.add(zone)
    db_session.commit()

def getAllZones():
    return Zone.query.all()

def getFirstZone():
    print (Zone.query.first())
    return Zone.query.first()

def getZoneByName():
    name = input('What is the name of the zone you would like?')
    return Zone.query.filter(Zone.name == name).one()

# Resident Database connections

def addResident(resident):
    db_session.add(resident)
    db_session.commit()

def getAllResidents():
    return Resident.query.all()

def getFirstResident():
    return Resident.query.first()

def getResidentByName():
    name = input('What is the name of the resident you would like?')
    return Resident.query.filter(Resident.name == name).one()

