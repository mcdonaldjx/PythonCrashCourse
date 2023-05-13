import pygame, sys
from settings import Settings
from ship import Ship

class AlienInvasion:
  """Overall class to manage game assets and behavior"""
  def __init__(self):
    """Initialize the game, and create game resources."""
    pygame.init()
    self.clock = pygame.time.Clock()
    self.settings = Settings()

    #For windowed mode
    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

    #For full screen mode:
    #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    #self.settings.screen_width = self.screen.get_rect().width
    #self.settings.screen_height = self.screen.get_rect().height
    
    pygame.display.set_caption("Alien Invasion")

    self.ship = Ship(self)

    #Set the background color.
    self.bg_color = (230, 230, 230)
  
  def run_game(self):
    """Start the main loop for the game."""
    while True:
      # Watch for keyboard and mouse events. Events are actions that the user performs
      self._check_events()
      self.ship.update()
      self._update_screen()
      #Make the most recently drawn screen visible.
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

  def _check_keyup_events(self, event):
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = False
  
  def _update_screen(self): #Helper function (denoted by a single underscore)
    """Update images on the screen, and flip to the new screen."""
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme() # Draw the ship onto the screen 
    pygame.display.flip()  

if __name__ == '__main__':
    # Make a game instance and run the game.
  ai = AlienInvasion()
  ai.run_game()
