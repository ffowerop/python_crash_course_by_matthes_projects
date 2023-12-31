import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""Class that manages the ship"""
	def __init__(self, ai_game):
		"""Initializes a ship and sets it's initial position"""
		super().__init__()
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings

		#Loads ship's image and gets it's rectangle
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		#Every new ship appears at the middle of bottom of the screen
		self.rect.midbottom = self.screen_rect.midbottom
		#Saving float coordinate of the ship's center
		self.x = float(self.rect.x)
		#Movememnt indicator
		self.moving_left = False
		self.moving_right = False

	def blitme(self):
		#Draws a ship in current position
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""Update ship's position depending of the indicator"""
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed_factor
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed_factor
		#Updates ship's center position on the ground of self.x
		self.rect.x = self.x

	def center_ship(self):
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)