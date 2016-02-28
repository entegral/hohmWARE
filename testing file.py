from classes import *

rooms = []
setup_rooms = input("How many rooms would you like to setup?")
room_count = 0
while room_count < setup_rooms:
    room_name = raw_input("What would you like to name the room?")
    doors = input("How many exterior doors are in your room?")
    windows = input("How many windows are in your room?")
    rooms.append(Room(room_name, doors + windows, 70))
    print rooms
    print rooms[0].opening
    room_count = room_count + 1

print rooms


#my_home =  Home(['Robby', 'Elizabeth', 'Colin', 'Braden'], '702 SW Cheltenham St', 70, True)
#print my_home.residents
#print my_home.temperature
#print my_home.isoccupied()
