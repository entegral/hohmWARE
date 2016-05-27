
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import models

engine = create_engine('sqlite:///homeware.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

models.Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)

    #import RPi.GPIO

def getAllZones():
    return models.Zone.query.all()

def getFirstZone():
    return models.Zone.query.first()

def addZone(zone):
    db_session.add(zone)
    db_session.commit()


def getAllResidents():
    return models.Resident.query.all()

def addResident(resident):
    db_session.add(resident)
    db_session.commit()


