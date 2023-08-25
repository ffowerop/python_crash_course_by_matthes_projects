import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
	"""Class for managing resources and game behavior"""
	def __init__(self):
		"""Initializing the game and creating resources"""
		pygame.init()
		self.settings = Settings()
		# #Used to play in window
		# self.screen = pygame.display.set_mode(
		# 	(self.settings.screen_width, self.settings.screen_height))
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()

	def run_game(self):
		"""Starts the main loop of the game"""
		while True:
			self._check_events()
			self.ship.update()
			self.bullets.update()
			self._remove_flow_away_bullets()
			self._update_screen()

	def _fire_bullet(self):
		new_bullet = Bullet(self)
		self.bullets.add(new_bullet)

	def _remove_flow_away_bullets(self):
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

	def _check_keydown_events(self, event):
		if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
			sys.exit()
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		if event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		if event.key == pygame.K_SPACE:
			self._fire_bullet()

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
		for bullet in self.bullets.sprites():
			bullet.draw()
		self.ship.blitme()
		#Show last rendered screen
		pygame.display.flip()


if __name__ == '__main__':
	#Creates game instance and runs it
	ai = AlienInvasion()
	ai.run_game()