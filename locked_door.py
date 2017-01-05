from sys import exit

class Door(object):
	def enter(self):
		print "Not yet configured."
		exit(1)


class Engine(object):

	def __init__(self, door_map):
		self.door_map = door_map

	def play(self):
		current_door = self.door_map.opening_door()
		last_door = self.door_map.next_door('finished')

		while current_door != last_door:
			next_door_name = current_door.enter()
			current_door = self.door_map.next_door(next_door_name)

		current_door.enter()


class Room1(Door):

	def enter(self):
		print "What happened?  You wake up on the floor."
		print "Looking at the ceiling, you see your room is a circle."
		print "Sitting up, you notice 6 doors evenly spaced on the walls."
		print "The doors look strange."


class CentralRoom(object):

	doors = { 
	'room_1' : Room1()
	}

	def __init__(self, start_door):
		self.start_door = start_door

	def next_door(self, door_name):
		val = CentralRoom.doors.get(door_name)
		return val

	def opening_door(self):
		return self.next_door(self.start_door)

a_door = CentralRoom('room_1')
a_game = Engine(a_door)
a_game.play()