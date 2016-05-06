import shelve



config = shelve.open('homeconfig')

residents = config['residents']
zones = config['zones']