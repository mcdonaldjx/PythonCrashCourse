# Created 05/30/2023 by Jared
# 14-1. Press P to Play: Because Alien Invasion uses keyboard input to control the ship, it would be useful to start the game with a keypress. Add code that lets the player press P to start. It might help to move some code from _check_play_button() to a _start_game() method that can be called from _check_play_button() and _check_keydown_events().
import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
  """Overall class to manage game assets and behavior"""
  
  def __init__(self):
    """Initialize the game, and create game resources."""
    pygame.init()
    self.settings = Settings()
    self.clock = pygame.time.Clock()

    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics.
    self.stats = GameStats(self)
    
    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group() #Create a group/list of that holds the bullets
    self.aliens = pygame.sprite.Group()

    self._create_fleet()
    #Set the background color.
    self.bg_color = (230, 230, 230)
    
    #Start Alien Invasion in an active state.
    self.game_active = False
  
  def run_game(self):
    """Start the main loop for the game."""
    while True:
      # Watch for keyboard and mouse events. Events are actions that the user performs
      self._check_events()
      if self.game_active:
        self.ship.update()
        self._update_bullets()
        self._update_aliens()
      self._update_screen() #Make the most recently drawn screen visible.
      self.clock.tick(60)

  def _check_events(self): #Helper function (denoted by a single underscore)
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get(): #Event loop. Returns a list of events that have taken place since the last time this function was called
          if event.type == pygame.QUIT: #If the window's close button is clicked, exit the game
            sys.exit()
          elif event.type == pygame.KEYDOWN:
            self._check_keydown_events(event)
          elif event.type == pygame.KEYUP:
            self._check_keyup_events(event)

  def _check_keydown_events(self, event):
    """Respond to keypresses."""
    #Move the ship to the right
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = True
    elif event.key == pygame.K_q:
      sys.exit()
    elif event.key == pygame.K_SPACE:
      self._fire_bullet()
    elif event.key == pygame.K_p:
      if not self.game_active: 
        #Reset the game statistics
        self.stats.reset_stats()
        self.game_active = True
  
        #Hide the mouse cursor
        pygame.mouse.set_visible(False)
        
        # Get rid of any remaining bullets and aliens
        self.bullets.empty()
        self.aliens.empty()
  
        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()
      

  def _check_keyup_events(self, event):
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = False
    
  def _ship_hit(self):
    """Respond to the ship being hit by an alien."""
    if self.stats.ships_left > 0:
      # Decrement ships_left
      self.stats.ships_left -= 1

      # Get rid of any remaining bullets and aliens
      self.bullets.empty()
      self.aliens.empty()
  
      # Create a new fleet and center the ship.
      self._create_fleet()
      self.ship.center_ship()
      # Pause.
      sleep(0.5)
    else:
      self.game_active = False
      pygame.mouse.set_visible(True)
  
  def _fire_bullet(self):
    """Create a new bullet and add it to the bullets group."""
    if len(self.bullets) < self.settings.bullets_allowed:
      new_bullet = Bullet(self)
      self.bullets.add(new_bullet) #Add the bullet to the group

  def _update_bullets(self):
    """Update position of bullets and get rid of old bullets."""
    #Update bullet positions
    self.bullets.update() #Calls update for every bullet in the group
    #Get rid of bullets that have disappeared.
    for bullet in self.bullets.copy():
      if bullet.rect.bottom <= 0:
        self.bullets.remove(bullet)
    #Check for any bullets that have hit aliens.
    self._check_bullet_alien_collisions()
    

  def _check_bullet_alien_collisions(self):
    """Respond to bullet-alien collisions"""
    #Remove any bullets and aliens that have collided
    collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True) #Check group 1 (bullets) and group 2 (aliens) for collisions, Delete the bullet ? (True so yes), Delete the alien (True so yes)
    if not self.aliens:
      #Destroy existing bullets and create new fleet.
      self.bullets.empty()
      self._create_fleet()

  def _update_aliens(self):
    """Update the positions of all aliens in the fleet."""
    self._check_fleet_edges()
    self.aliens.update()

    #  Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(self.ship, self.aliens): #Look for any member of aliens to collide with the ship's sprite
      self._ship_hit()

    # Look for aliens hitting the bottom of the screen
    self._check_aliens_bottom()

  def _update_screen(self): #Helper function (denoted by a single underscore)
    """Update images on the screen, and flip to the new screen."""
    self.screen.fill(self.settings.bg_color)
    for bullet in self.bullets.sprites():
        bullet.draw_bullet()
    self.aliens.draw(self.screen)
    self.ship.blitme() # Draw the ship onto the screen    
    pygame.display.flip()

  def _create_fleet(self):
    """Create the fleet of aliens"""
    #Create an alien and keep adding aliens until there's no room left.
    #Spacing between aliens is one alien width and one alien height
    alien = Alien(self)
    alien_width, alien_height = alien.rect.size

    current_x, current_y = alien_width, alien_height
    while current_y < (self.settings.screen_height - 3 * alien_height):
      while current_x < (self.settings.screen_width - 2 * alien_width):
        self._create_alien(current_x, current_y)
        current_x += 2 * alien_width

      #Finished a row; reset x value, and increment y value.
      current_x = alien_width
      current_y += 2 * alien_height

  def _create_alien(self, x_position, y_position):
    """Create an alien and place it in the fleet"""
    new_alien = Alien(self)
    new_alien.x = x_position
    new_alien.rect.x = x_position
    new_alien.rect.y = y_position
    self.aliens.add(new_alien)

  def _check_fleet_edges(self):
    """Respond appropiately if any aliens have reached an edge."""
    for alien in self.aliens.sprites(): #For every alien in fleet
      if alien.check_edges(): #Check if it hit an edge, if so, change its direction
        self._change_fleet_direction()
        break

  def _change_fleet_direction(self):
    """Drop the entire fleet and change the fleet's direction"""
    for alien in self.aliens.sprites():
      alien.rect.y += self.settings.fleet_drop_speed
    self.settings.fleet_direction *= -1

  def _check_aliens_bottom(self):
    """Check if any aliens have reached the bottom of the screen."""
    for alien in self.aliens.sprites():
      if alien.rect.bottom >= self.settings.screen_height:
        # Treat this the same as if the ship got hit.
        self._ship_hit()
        break
      
if __name__ == '__main__':
    # Make a game instance and run the game.
  ai = AlienInvasion()
  ai.run_game()
