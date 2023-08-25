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
			self._check_events()
			self.ship.update()
			self._update_screen()

	def _check_keydown_events(self, event):
		if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
			sys.exit()
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		if event.key == pygame.K_LEFT:
			self.ship.moving_left = True

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		if event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _check_events(self):
		"""Handles keyboard and mouse events"""
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					self._check_keydown_events(event)
				elif event.type == pygame.KEYUP:
					self._check_keyup_events(event)

	def _update_screen(self):
		"""Updates the screen image and shows new screen"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		#Show last rendered screen
		pygame.display.flip()


if __name__ == '__main__':
	#Creates game instance and runs it
	ai = AlienInvasion()
	ai.run_game()