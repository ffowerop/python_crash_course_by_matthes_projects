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

	def prep_score(self):		
		rounded_score = round(self.game_stats.score, -1)
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color,
				self.settings.bg_color)
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
		self.screen.blit(self.score_image, self.score_rect)

