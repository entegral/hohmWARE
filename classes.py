class Home():
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


class Room(Home):
    def __init__(self, residents, address, temperature, occupied, doors, windows):
        Home.__init__(self, residents, address, temperature, occupied)
        self.doors = doors
        self.windows = windows


class Opening(Room):
    def __init__(self, residents, address, temperature, occupied, doors, windows, status):
        Room.__init__(self, residents, address, temperature, occupied, doors, windows)
        self.status = status

my_room = Room(['Robby'], '702 SW Cheltenham St', 70, False, 1, 3)
print my_room.residents
print my_room.windows
print my_room.isoccupied()