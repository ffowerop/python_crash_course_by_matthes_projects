import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button

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
		self.screen_rect = self.screen.get_rect()
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")

		#Creates instance for keeping game stats
		self.game_stats = GameStats(self)

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

		self.play_button = Button(self, "PLAY")

	def run_game(self):
		"""Starts the main loop of the game"""
		while True:
			self._check_events()
			if self.game_stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_aliens()
			self._update_screen()

	def _fire_bullet(self):
		if len(self.bullets) < self.settings.bullet_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		self.bullets.update()
		#Removes flown away from screen bullets
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
		self._check_bullet_alien_collision()

	def _check_bullet_alien_collision(self):
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True)
		#Destroys all bullets and creates new alien fleet
		if not self.aliens:
			self.bullets.empty()
			self._create_fleet()

	def _create_alien(self, alien_number, row_number):
		alien = Alien(self)
		alien.x = self.alien_width + self.alien_width * 2 * alien_number
		alien.rect.x = alien.x
		alien.rect.y = self.alien_height + self.alien_height * 2 * row_number
		return alien

	def _create_fleet(self):
		"""Creats invasion fleet"""
		alien = Alien(self)
		available_space_x = self.settings.screen_width - 2 * self.alien_width
		number_aliens_x = available_space_x // (self.alien_width * 2)
		available_space_y = (self.settings.screen_height - 
								3 * self.alien_height - self.alien_height)
		number_rows = available_space_y // (self.alien_height * 2)
		for j in range (number_rows):
			for i in range(number_aliens_x):
				self.aliens.add(self._create_alien(i, j))

	def _check_fleet_edges(self):
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _update_aliens(self):
		"""Checks if fleet has reached the edge of screen
		and updates all alien positions"""
		self._check_fleet_edges()
		self.aliens.update()
		#Checks collision of any alien with ship
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()
		self._check_aliens_bottom()

	def _ship_hit(self):
		if self.game_stats.ships_left > 0:
			#Decrease ships left
			self.game_stats.ships_left -= 1
			
			#Delete all aliens and bullets
			self.aliens.empty()
			self.bullets.empty()
			#Creates new fleet and moves ship to the center
			self._create_fleet()
			self.ship.center_ship()
			#Pause for 5 sec
			sleep(0.5)
		else:
			self.game_stats.game_active = False
			pygame.mouse.set_visible(True)
	def _check_aliens_bottom(self):
		#Checks if any alien reaches the bottom
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= self.screen_rect.bottom:
				self._ship_hit()
				break

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
				elif event.type == pygame.MOUSEBUTTONDOWN:
					mouse_pos = pygame.mouse.get_pos()
					self._check_play_button(mouse_pos)

	def _check_play_button(self, mouse_pos):
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.game_stats.game_active:
			self.game_stats.reset_stats()
			self.game_stats.game_active = True
			self.aliens.empty()
			self.bullets.empty()
			self._create_fleet()
			self.ship.center_ship()
			pygame.mouse.set_visible(False)

	def _update_screen(self):
		"""Updates the screen image and shows new screen"""
		self.screen.fill(self.settings.bg_color)		
		for bullet in self.bullets.sprites():
			bullet.draw()
		self.ship.blitme()
		self.aliens.draw(self.screen)
		#Shows play button if game is not active
		if not self.game_stats.game_active:
			self.play_button.draw_button()
		#Show last rendered screen
		pygame.display.flip()


if __name__ == '__main__':
	#Creates game instance and runs it
	ai = AlienInvasion()
	ai.run_game()