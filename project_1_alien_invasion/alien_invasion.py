import sys

import pygame

class AlienInvasion:
	"""Class for managing resources and game behavior"""
	def __init__(self):
		"""Initializing the game and creating resources"""
		pygame.init()

		self.screen = pygame.display.set_mode((1200, 760))
		pygame.display.set_caption("Alien Invasion")

	def run_game(self):
		"""Starts the main loop of the game"""
		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						sys.exit()
			#Show last rendered screen
			pygame.display.flip()

if __name__ == '__main__':
	#Creates game instance and runs it
	ai = AlienInvasion()
	ai.run_game()
