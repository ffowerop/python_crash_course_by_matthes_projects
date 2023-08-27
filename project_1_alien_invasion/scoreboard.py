import pygame.font

class Scoreboard():
	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen_rect
		self.settings = ai_game.settings
		self.game_stats = ai_game.game_stats
		#Font settings
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
		#Preparing initial image
		self.prep_score()
		self.prep_high_score()
		self.prep_level()

	def prep_score(self):		
		rounded_score = round(self.game_stats.score, -1)
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color,
				self.settings.bg_color)
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_high_score(self):		
		high_score = round(self.game_stats.high_score, -1)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True,
				self.text_color, self.settings.bg_color)
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def prep_level(self):
		level_str = str(self.game_stats.level)
		self.level_image = self.font.render(level_str, True,
				self.text_color, self.settings.bg_color)
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 20

	def show_score(self):
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)

	def check_high_score(self):
		if self.game_stats.score > self.game_stats.high_score:
			self.game_stats.high_score = self.game_stats.score
			self.prep_high_score()

