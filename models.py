__author__ = 'Goomba'
#import RPi.GPIO as GPIO  #these must be turned off until testing on a rasp Pi
#GPIO.setmode(GPIO.BCM)
from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()


class Zone(Base):

    """This is an object needed to associate regions of the house with a gpio
    pin.  It is currently used to setup pins to detect home intrusion, but
    eventually it will also include pin-association information required to
    control various functions of the house (i.e. relays for lighting, fans, AC,
    music, TV, etc.)"""

    __tablename__ = 'zones'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    channel = Column(Integer, unique=True)

    def __repr__(self):
        return '<zone %r>' % (self.name)


class Resident(Base):
    """This is an object that will store information relating to the people
    living in the household. It stores personal information that
    enables this app to interact with the people in the household."""

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

    """This is an object that represents a household. The attributes are likely
    to change as features are added to this home automation software."""

    __tablename__ = 'house'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique = True)
    address = Column(String, unique= True)
    residents = relationship('Resident', back_populates="house")

    def __repr__(self):
        return '<house %r>' % (self.name)


class Data_Point(Base):
    """This is an object that will collect various home sensor data and log it
    with a timestamp."""

    __tablename__ = 'log'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default= datetime.datetime.utcnow)
    temperature = Column(Integer, unique= False)
    open_doors = Column(String, unique= False)

    def __repr__(self):
        return '<log %r>' % (self.timestamp)
