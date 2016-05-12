__author__ = 'Goomba'
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)





class Zone:
	"""This constructor is to be called when instantiating a new zone. It should be used only in the setup of the system"""
	


	def __init__(self, name, channel):
		self.name = name
		self.channel = channel
	
	def id(self):
		print self.name + " is assigned to channel " + str(self.channel) + "\n"		#function to identify the gpio pin a zone is configured to
	
	#def setup(self):
	#    GPIO.setup(self.channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #This line recieves a channel name and sets it up to be an input 
																	 #with a pull up resistor. When a zone alarms, the circuit voltage 
																	 #will drop and a 'event_detected()' function will trigger

class Home:
	def __init__(self, residents, address, temperature, occupied):
		self.residents = residents
		self.address = address
		self.temperature = temperature
		self.occupied = occupied

	def isoccupied(self):
		if self.occupied is True:

			return str(self.occupied) + ", " + str(self.address) + " is occupied by " + str(self.residents) + "."
		else:
			return str(self.occupied) + ", " + str(self.address) + " is not occupied at this time."
