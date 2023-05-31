import pygame, sys
from sideways_ship import Ship
from bullet import Bullet
from button import Button
from settings import Settings
from target import Target

class Sideways_Shooter:
  """Overall class to manage game assets and behavior"""
  
  def __init__(self):
    """Initialize the game, and create game resources."""
    pygame.init()
    self.screen = pygame.display.set_mode((500,500))
    self.settings = Settings()
    self.game_active = False
    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()
    self.target = Target(self)
    
    self.bg_color = (255, 255, 255)
    self.start_button = Button(self, "Start game")
  
  def run_game(self):
    """Start the main loop for the game."""
    while True:
      self._check_events()
      if self.game_active:
        self.ship.update()
        self._update_bullets()
        self._update_target()
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
          elif event.type == pygame.MOUSEBUTTONDOWN:
            self._check_start_button(pygame.mouse.get_pos())            

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

  def _check_start_button(self, mouse_pos):
    button_clicked = self.start_button.rect.collidepoint(mouse_pos)
    if button_clicked and not self.game_active:
      self.ship = Ship(self)
      self.bullets = pygame.sprite.Group() #Create a group/list of that holds the bullets
      self._create_target(450, 250)
      self.bg_color = (230, 230, 230)
      self.settings.misses = 0
      self.game_active = True
      

  def _check_misses(self):
    if self.settings.misses >= 3:
      self.game_active = False
      
  def _check_bullet_target_collisions(self):
    collision = pygame.sprite.spritecollide(self.target, self.bullets, True)   
  
  def _check_target_edges(self):
    if self.target.check_edges():
      self._change_target_direction()
  
  def _fire_bullet(self):
    """Create a new bullet and add it to the bullets group."""
    new_bullet = Bullet(self)
    self.bullets.add(new_bullet) #Add the bullet to the group

  def _create_target(self, x_pos, y_pos):
    target = Target(self)
    target.x = x_pos
    target.rect.x = x_pos
    target.rect.y = y_pos
    
  def _change_target_direction(self):
    self.settings.target_direction *= -1
  
  def _update_bullets(self):
    """Update position of bullets and get rid of old bullets."""
    #Update bullet positions
    self.bullets.update() #Calls update for every bullet in the group
    #Get rid of bullets that have disappeared.
    for bullet in self.bullets.copy():
      if bullet.rect.left >= 500:
        self.bullets.remove(bullet)
        self.settings.misses += 1
        self._check_misses()
    self._check_bullet_target_collisions()

  def _update_target(self):
    self._check_target_edges()
    self.target.update()
    
  
  def _update_screen(self): #Helper function (denoted by a single underscore)
    """Update images on the screen, and flip to the new screen."""
    self.screen.fill(self.settings.bg_color)
    for bullet in self.bullets.sprites():
        bullet.draw_bullet()
    self.target.draw()
    self.ship.blitme() # Draw the ship onto the screen 
    if not self.game_active:
      self.start_button.draw_button()
    pygame.display.flip()  

if __name__ == '__main__':
    # Make a game instance and run the game.
  ai = Sideways_Shooter()
  ai.run_game()