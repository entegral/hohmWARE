
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
    return Zone.query.first()

def getZoneByName(name):
    return Zone.query.filter(Zone.name == name).one()

def deleteZone(name):
    q = getZoneByName(name)
    db_session.delete(q)
    db_session.commit()


# Resident Database connections

def addResident(resident):
    db_session.add(resident)
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
