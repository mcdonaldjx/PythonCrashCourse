import pygame, sys
from sideways_ship import Ship
from bullet import Bullet
from settings import Settings
from alien import Alien

class Sideways_Shooter:
  """Overall class to manage game assets and behavior"""
  
  def __init__(self):
    """Initialize the game, and create game resources."""
    pygame.init()
    self.screen = pygame.display.set_mode((500,500))
    self.settings = Settings()
    
    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()
    self.aliens = pygame.sprite.Group()
    
    self.bg_color = (255, 255, 255)
    self._create_fleet()
  
  def run_game(self):
    """Start the main loop for the game."""
    while True:
      self._check_events()
      self.ship.update()
      self._update_bullets()
      self._update_aliens()
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

  def _check_bullet_alien_collisions(self):
    collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
  
  def _check_fleet_edges(self):
    for alien in self.aliens:
      if alien.check_edges():
        self._change_fleet_direction()
        break
  
  def _fire_bullet(self):
    """Create a new bullet and add it to the bullets group."""
    new_bullet = Bullet(self)
    self.bullets.add(new_bullet) #Add the bullet to the group

  def _create_alien(self, x_pos, y_pos):
    alien = Alien(self)
    alien.x = x_pos
    alien.rect.x = x_pos
    alien.rect.y = y_pos
    print(f"Alien created at {x_pos},{y_pos}")
    self.aliens.add(alien)

  
  def _create_fleet(self):
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

    
  def _change_fleet_direction(self):
    for alien in self.aliens.sprites():
      alien.rect.x -= self.settings.fleet_drop_speed
    self.settings.fleet_direction *= -1
  
  def _update_bullets(self):
    """Update position of bullets and get rid of old bullets."""
    #Update bullet positions
    self.bullets.update() #Calls update for every bullet in the group
    #Get rid of bullets that have disappeared.
    for bullet in self.bullets.copy():
      if bullet.rect.left >= 500:
        self.bullets.remove(bullet)
    self._check_bullet_alien_collisions()

  def _update_aliens(self):
    self._check_fleet_edges()
    self.aliens.update()
    
  
  def _update_screen(self): #Helper function (denoted by a single underscore)
    """Update images on the screen, and flip to the new screen."""
    self.screen.fill(self.settings.bg_color)
    for bullet in self.bullets.sprites():
        bullet.draw_bullet()
    self.aliens.draw(self.screen)
    self.ship.blitme() # Draw the ship onto the screen 
    pygame.display.flip()  

if __name__ == '__main__':
    # Make a game instance and run the game.
  ai = Sideways_Shooter()
  ai.run_game()