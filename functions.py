

def createGPIOdb():
	conn = sqlite3.connect('homeconfig.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE home 
					(zone real, gpio real)''')
	c.commit()
	c.close()

def saveconfigdata():
	conn = sqlite3.connect('homeconfig.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE home 
					(zone real, gpio real)''')
	c.commit()
	c.close()	