import models, database




def monitorProcess():
	alarm = True
	while alarm:
		GPIO.add_event_detect(zones, GPIO.RISING, callback=doorClosed())
		GPIO.add_event_detect(zones, GPIO.FALLING, callback=doorOpened())
		sleep(1)




def doorOpened():
	print "AYYYYE, THE BLAST DOOR HAS BEEN BREACHED!!!"

def doorClosed():
	print "Ayyyyyyye, de doors be calmer than a whooooores tit."


