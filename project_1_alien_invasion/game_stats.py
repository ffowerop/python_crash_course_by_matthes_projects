import json

class GameStats():
	"""Keeps track of the game stats"""
	def __init__(self,ai_game):
		self.settings = ai_game.settings
		self.reset_stats()
		#Game starts in inactive mode
		self.game_active = False
		self.high_score = self.load_high_score()

	def reset_stats(self):
		self.ships_left = self.settings.ship_limit
		self.score = 0

	def load_high_score(self):
		with open('highscore.json') as f:
			return int(json.load(f))

	def save_high_score(self):
		with open('highscore.json', 'w') as f:
			json.dump(self.high_score, f)