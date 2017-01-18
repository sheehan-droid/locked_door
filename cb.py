import random


def line():
	print "=" * 80

class Card(object):
	
	def __init__(self, atk, df, hp):

		self.atk = atk
		self.df = df
		self.hp = hp
		self.actions = ["Attack", "Defense", "HP"]

	def player_generate_hp_dmg(self):
		if self.atk > enemy.df:
			return self.atk - enemy.df
		elif self.atk <= enemy.df:
			return 0
	
	def enemy_generate_hp_dmg(self):
		if self.atk > player.df:
			return self.atk - player.df
		elif self.atk <= player.df:
			return 0

	def generate_atk_dmg(self):
		return self.atk/3

	def generate_df_dmg(self):
		return self.atk/2

	def take_hp_dmg(self, hp):
		self.hp -= hp_dmg
		if self.hp < 0:
			self.hp = 0
		return self.hp

	def take_atk_dmg(self, atk):
		self.atk -= atk_dmg
		if self.atk < 0:
			self.atk = 0
		return self.atk

	def take_df_dmg(self, df):
		self.df -= df_dmg
		if self.df < 0:
			self.df = 0
		return self.df

	def get_hp(self):
		return self.hp

	def get_atk(self):
		return self.atk

	def get_df(self):
		return self.df

	def choose_action(self):
		i = 1
		print "Type 1, 2, or 3, to attack the enemy's:"
		for item in self.actions:
			print str(i) + ':', item
			i += 1


player = Card(random.randrange(4, 9), random.randrange(4, 9), random.randrange(8, 17))
enemy = Card(random.randrange(5, 10), random.randrange(5, 10), random.randrange(9, 18))

running = True
i = 0

line()
print "The cards are out! Let's play!"

while running:
	line()
	print "Your fighter's stats are:"
	print "ATK:", player.get_atk(), "DEF:", player.get_df(), "HP:", player.get_hp()
	line()
	print "The enemy's fighter looks tough. His stats:"
	print "ATK:", enemy.get_atk(), "DEF:", enemy.get_df(), "HP:", enemy.get_hp()
	line()

	player.choose_action()
	choice = raw_input("Choose action: ")
	index = int(choice) - 1

	if index == 0:
		atk_dmg = player.generate_atk_dmg()
		enemy.take_atk_dmg(atk_dmg)
		line()
		print "You attacked the enemy's ATK for ", atk_dmg
		print "Enemy ATK is now: ", enemy.get_atk()

	elif index == 1:
		df_dmg = player.generate_df_dmg()
		enemy.take_df_dmg(df_dmg)
		line()
		print "You attacked the enemy's DEF for ", df_dmg
		print "Enemy DEF is now: ", enemy.get_df()

	elif index == 2:
		hp_dmg = player.player_generate_hp_dmg()
		enemy.take_hp_dmg(hp_dmg)
		line()
		print "You attacked the enemy's HP for ", hp_dmg
		print "Enemy HP is now: ", enemy.get_hp()

	else:
		line()
		print "Try typing 1, 2, or 3 to attack the enemy."
		continue

	if enemy.get_hp() <= 0:
		line()
		print "You have defeated the enemy! Nice!"
		running = False
		break

	enemy_choice = random.randrange(1, 4)
	
	if enemy_choice == 1:
		atk_dmg = enemy.generate_atk_dmg()
		player.take_atk_dmg(atk_dmg)
		line()
		print "Enemy attacked your ATK for ", atk_dmg
		print "Your ATK is now: ", player.get_atk()

	elif enemy_choice == 2:
		df_dmg = enemy.generate_df_dmg()
		player.take_df_dmg(df_dmg)
		line()
		print "Enemy attacked your DEF for ", df_dmg
		print "Your DEF is now: ", player.get_df()

	elif enemy_choice == 3:
		hp_dmg = enemy.enemy_generate_hp_dmg()
		player.take_hp_dmg(hp_dmg)
		line()
		print "Enemy attacked your HP for ", hp_dmg
		print "Your HP is now: ", player.get_hp()

	if player.get_hp() <= 0:
		line()
		print "You have died!  Too bad."
		running = False
		break









