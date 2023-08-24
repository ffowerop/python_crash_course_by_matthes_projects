import pygame

class Ship():
	"""Class that manages the ship"""
	def __init__(self, ai_game):
		"""Initializes a ship and sets it's initial position"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		#Loads ship's image and gets it's rectangle
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		#Every new ship appears at the middle of bottom of the screen
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		#Draws a ship in current position
		self.screen.blit(self.image, self.rect)