import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, ai_game):
		"""Creat bullet in current position of ship"""
		super().__init__()
		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color
		self.rect = pygame.Rect(0, 0,
			self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = self.ai_game.ship.rect.midtop
		self.y = float(self.rect.y)
		

	def update(self):
		"""Moves bullet up the screen"""
		self.y -= self.settings.bullet_speed_factor
		self.rect.y = self.y

	def draw(self):
		"""Output the bullet on the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)
		

