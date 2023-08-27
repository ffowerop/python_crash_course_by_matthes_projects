class Settings:
	"""Class for storing all the settings of the game"""
	def __init__(self):
		"""Intitialize game settings"""
		self.screen_width = 1200
		self.screen_height = 760
		self.bg_color = (230, 230, 230)
		#Ship parametrs
		self.ship_limit = 3
		#Bullet parametrs
		self.bullet_width = 3000
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullet_allowed = 10
		#Alien parametrs
		self.fleet_drop_speed = 30

		self.speedup_scale = 5
		self.score_scale = 1.5
		self.intitialize_dynamic_settings()

	def intitialize_dynamic_settings(self):
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 1.5
		self.alien_speed_factor = 1.0
		self.alien_points = 50

		self.fleet_direction = 1

	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)