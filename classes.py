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


class Room:
    def __init__(self, roomid, opening, temperature, ):
        self.id = roomid
        self.opening = opening
        self.temperature = temperature


class Opening:
    def __init__(self,  status):
        self.status = status      #this will eventually be replaced by a specific


class Window(Opening):
    def __init__(self, status, windowid):
        Opening.__init__(self, status)
        self.windowid = windowid


class Door(Opening):
    def __init__(self, status, doorid):
        Opening.__init__(self,status)
        self.doorid = doorid
