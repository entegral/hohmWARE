__author__ = 'Goomba'

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)





class Zone:
    def __init__(self, name, channel):
        self.name = name
        self.channel = channel
    def id(self):
        print self.name + "is assigned to channel" + str(self.channel) + "\n"
    def setup(self):
        GPIO.setup(self.channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #This line recieves a channel name and sets it up to be an input with a pull down resistor. When a zone alarms, it will recieve 5V signal and a 'event_detected()' function will trigger
