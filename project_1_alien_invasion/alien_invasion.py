import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
	"""Class for managing resources and game behavior"""
	def __init__(self):
		"""Initializing the game and creating resources"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)

	def run_game(self):
		"""Starts the main loop of the game"""
		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						sys.exit()
			self.screen.fill(self.settings.bg_color)
			self.ship.blitme()
			#Show last rendered screen
			pygame.display.flip()

if __name__ == '__main__':
	#Creates game instance and runs it
	ai = AlienInvasion()
	ai.run_game()
