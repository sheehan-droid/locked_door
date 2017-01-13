import random


magic = [{'name': 'Fire', 'cost': 10, 'dmg': 60},
		 {'name': 'Thunder', 'cost': 10, 'dmg': 60},
		 {'name': 'Blizzard', 'cost': 10, 'dmg': 60}]


class Person(object):

	def __init__(self, hp, mp, atk, defs, magic):
		self.maxhp = hp
		self.hp = hp
		self.maxmp = mp
		self.mp = mp
		self.atkh = atk + 10
		self.atkl = atk - 10
		self.defs = defs
		self.magic = magic
		self.actions = ["Attack", "Magic"]

	def generate_dmg(self):
		return random.randrange(self.atkl, self.atkh)

	def generate_spell_dmg(self, i):
		mgl = magic[i]['dmg'] - 5
		mgh = magic[i]['dmg'] + 5
		return random.randrange(mgl, mgh)

	def take_dmg(self, hp):
		self.hp -= dmg
		if self.hp < 0:
			self.hp = 0
		return self.hp

	def get_hp(self):
		return self.hp

	def get_max_hp(self):
		return self.maxhp

	def get_mp(self):
		return self.mp

	def get_max_mp(self):
		return self.maxmp

	def reduce_mp(self, cost):
		self.mp -= cost

	def get_spell_name(self, i):
		return self.magic[i]['name']

	def get_spell_mp_cost(self, i):
		return self.magic[i]['cost']

	def choose_action(self):
		i = 1
		print 'Actions'
		for item in self.actions:
			print str(i) + ':', item
			i += 1

	def choose_magic(self):
		i = 1
		print 'Magic'
		for spell in magic:
			print str(i) + ':', spell['name', 'cost: ', str(spell['mp'])]
			i += 1


player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print 'AN ENEMY ATTACKS!'

while running:
	print'=' * 80
	player.choose_action()
	choice = raw_input("Choose action: ")
	index = int(choice) -1

	if index == 0:
		dmg = player.generate_dmg()
		enemy.take_dmg(dmg)
		print 'You attacked for ', dmg, 'point of damage.'
		print 'Enemy hp is now : ', enemy.get_hp()

	enemy_choice = 1

	enemy_dmg = enemy.generate_dmg()
	player.take_dmg(enemy_dmg)
	print 'Enemy attacks for: ', enemy_dmg
	print 'Player HP is now: ', player.get_hp()

	if player.get_hp() <= 0:
		running = False










