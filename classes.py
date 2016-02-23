class Home():
    def __init__(self, address, temperature, occupied):
        self.address = address
        self.temperature = temperature
        self.occupied = occupied

    def isOccupied(self, occupied):
        return self.occupied

class Room(Home):
    def __init__(self, address, temperature, occupied, doors, windows):
        Home.__init__(address, temperature, occupied)
        self.doors = doors
        self.windows = windows
        