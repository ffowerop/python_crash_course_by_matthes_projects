import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self, ai_game):
		"""Initializes an alien and sets it's initial position"""
		super().__init__()
		self.screen = ai_game.screen
		#Loads alien's image and gets it's rectangle
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		#Every new alien appears in top left corner of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		#Saving alien width and height
		ai_game.alien_width = self.rect.width
		ai_game.alien_height = self.rect.height
		#Saving float coordinates of an alien's center
		self.x = float(self.rect.x)
