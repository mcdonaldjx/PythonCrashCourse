#Created 5/16/2023
#Exercise 12-6- Sideways Shooter: Write a game that places a ship on the left side of the screen and allows the player to move the ship up and down. Make the ship fire a bullet that travels right across the screen when the player presses the spacebar. Make sure bullets are deleted once they disappear off the screen.

import pygame, sys
from sideways_ship import Ship
from bullet import Bullet

class Sideways_Shooter:
  """Overall class to manage game assets and behavior"""
  def __init__(self):
    """Initialize the game, and create game resources."""
    pygame.init()

    self.screen = pygame.display.set_mode((500,500))
  
    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()

    self.bg_color = (255, 255, 255)
  
  def run_game(self):
    """Start the main loop for the game."""
    while True:
      self._check_events()
      self.ship.update()
      self._update_bullets()
      self._update_screen()

  def _check_events(self): #Helper function (denoted by a single underscore)
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
            sys.exit()
          elif event.type == pygame.KEYDOWN:
            self._check_keydown_events(event)
          elif event.type == pygame.KEYUP:
            self._check_keyup_events(event)

  def _check_keydown_events(self, event):
    """Respond to keypresses."""
    if event.key == pygame.K_UP:
      self.ship.moving_up = True
    elif event.key == pygame.K_DOWN:
      self.ship.moving_down = True
    elif event.key == pygame.K_q:
      sys.exit()
    elif event.key == pygame.K_SPACE:
      self._fire_bullet()

  def _check_keyup_events(self, event):
    if event.key == pygame.K_UP:
      self.ship.moving_up = False
    elif event.key == pygame.K_DOWN:
      self.ship.moving_down = False

  def _fire_bullet(self):
    """Create a new bullet and add it to the bullets group."""
    new_bullet = Bullet(self)
    self.bullets.add(new_bullet) #Add the bullet to the group

  def _update_bullets(self):
    """Update position of bullets and get rid of old bullets."""
    #Update bullet positions
    self.bullets.update() #Calls update for every bullet in the group
    #Get rid of bullets that have disappeared.
    for bullet in self.bullets.copy():
      if bullet.rect.left >= 500:
        self.bullets.remove(bullet)
  
  def _update_screen(self): #Helper function (denoted by a single underscore)
    """Update images on the screen, and flip to the new screen."""
    self.screen.fill((255,255,255))
    for bullet in self.bullets.sprites():
        bullet.draw_bullet()
    self.ship.blitme() # Draw the ship onto the screen 
    pygame.display.flip()  

if __name__ == '__main__':
    # Make a game instance and run the game.
  ai = Sideways_Shooter()
  ai.run_game()
