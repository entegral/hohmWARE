__author__ = 'Goomba'
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
from database.py import Base
from sqlalchemy import Column, Integer, String



class Zone(Base):
	
	"""This constructor is to be called when instantiating a new zone. 
	It should be used only in the setup of the database and configuration 
	of the system"""

	__tablename__ = 'zones'
	id = Column(Integer, primary_key=True)
	name = Column(String(50), unique=True)
	channel = Column(Integer, unique=True)

	def __init__(self, name, channel):
		self.name = name
		self.channel = channel	

	def __repr__(self):
        return '<zone %r>' % (self.name)

	def identifyyourself(self):
		print self.name + " is assigned to channel " + str(self.channel) + "\n"		#function to identify the gpio pin a zone is configured to
	
		#The following line recieves a channel name and sets it up to be an input 
		#with a pull up resistor. When a zone alarms, the circuit voltage 
		#will drop and a 'event_detected()' function will trigger																	
	
	#def setup(self):
	#    GPIO.setup(self.channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)


class Residents(Base):
	"""This is an object that will store information relating to the people
	living in the House object below. It will store personal information that
	will enable this app to function and determine the current state of the 
	house."""

	__tablename__ = 'residents'
	id = Column(Integer, primary_key=True)
	name = Column(String, unique=False)
	email = Column(String, unique=True)
	phone = Column(String, unique=True)
	mac =  Column(String,unique=True)

	def __init__(self, name, email, phone, mac):
		self.name = name
		self.email = email
		self.phone = phone
		self.mac = mac

	def __repr__(self):
		return '<residents %r>' %(self.name)


class House(Base):

	"""This is an object that will be repeatedly instantiated to ensure that
	 an accurate state of the house is maintained. The atributes' values will
	 be used to determine the state of the house. i.e. 'alarm armed', 'alarm 
	 disarmed',	'current temp', etc"""

	__tablename__ = 'house'
	id = Column(Integer, primary_key=True)
	residents = Column(String, unique=False)
	address = Column(String, unique=False)
	temperature = Column(Integer,unique=False)
	occupied = Column(String,unique=False)

	def __init__(self, residents, address, temperature, occupied):
		self.residents = residents
		self.address = address
		self.temperature = temperature
		self.occupied = occupied

	def __repr__(self):
        return '<house %r>' % (self.name)

	def isoccupied(self):
		if self.occupied is True:

			return str(self.occupied) + ", " + str(self.address) + " is occupied by " + str(self.residents) + "."
		else:
			return str(self.occupied) + ", " + str(self.address) + " is not occupied at this time."
