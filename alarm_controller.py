import models, database, zone_controller, resident_controller

def runAlarm():
	# take snapshot of every sensor and save their states
	# send a text message notifying admin(s) of alarm status
	# initiate a monitoring process that sends all sensor data to a cloud based backup system (pictures from cameras, entry points used, etc)
	# 