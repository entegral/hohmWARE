__author__ = 'Goomba'
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Zone(Base):
    
    """This constructor is to be called when instantiating a new zone. 
    It should be used only in the setup of the database and configuration 
    of the system"""

    __tablename__ = 'zones'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    channel = Column(Integer, unique=True)

    def __repr__(self):
        return '<zone %r>' % (self.name)


class Resident(Base):
    """This is an object that will store information relating to the people
    living in the House object below. It will store personal information that
    will enable this app to function and determine the current state of the 
    house."""

    __tablename__ = 'residents'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False)
    email = Column(String, unique=False)
    phone = Column(String, unique=False)
    ip = Column(String,unique=False)
    mac = Column(String,unique=False)
    house_id = Column(Integer, ForeignKey('house.id'))
    house = relationship('House', back_populates="residents")

    def __repr__(self):
        return '<residents %r>' %(self.name)


class House(Base):

    """This is an object that will be repeatedly instantiated to ensure that
     an accurate state of the house is maintained. The atributes' values will
     be used to determine the state of the house. i.e. 'alarm armed', 'alarm 
     disarmed', 'current temp', etc"""

    __tablename__ = 'house'
    id = Column(Integer, primary_key=True)
    address = Column(String, unique=False)
    residents = relationship('Resident', back_populates="house")
    temperatures = Column(Integer,unique=False, nullable = True)

    def __repr__(self):
        return '<house %r>' % (self.address)
