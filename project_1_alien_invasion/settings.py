class Settings:
	"""Class for storing all the settings of the game"""
	def __init__(self):
		"""Intitialize game settings"""
		self.screen_width = 1200
		self.screen_height = 760
		self.bg_color = (230, 230, 230)
		#Ship parametrs
		self.ship_speed = 1.5
		self.ship_limit = 3
		#Bullet parametrs
		self.bullet_speed = 1.5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullet_allowed = 10
		#Alien parametrs
		self.alien_speed = 1.0
		self.fleet_direction = 1
		self.fleet_drop_speed = 1000