#Created 05/13/2023
#Exercise 12-4- Rocket: Make a game that begins with a rocket in the center of the screen. Allow the player to move the rocket up, down, left, or right using the four arrow keys. Make sure the rocket never moves beyong any edge of the screen.
import pygame, sys
from rocket import Rocket

class Rocket_Game:
  """Overall class to manage game assets and behavior"""
  def __init__(self):
    """Initialize the game, and create game resources."""
    pygame.init()    
    self.screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Rocket Game")

    #Set the background color.
    self.bg_color = (255, 255, 255)

    self.rocket = Rocket(self)
  
  def run_game(self):
    """Start the main loop for the game."""
    while True:
      # Watch for keyboard and mouse events. Events are actions that the user performs
      self._check_events()
      self.rocket.update()
      self._update_screen()

  def _check_events(self): #Helper function (denoted by a single underscore)
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
          if event.type == pygame.QUIT: #If the window's close button is clicked, exit the game
            sys.exit()
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
              self.rocket.going_up = True
            if event.key == pygame.K_DOWN:
              self.rocket.going_down = True
            if event.key == pygame.K_LEFT:
              self.rocket.going_left = True
            if event.key == pygame.K_RIGHT:
              self.rocket.going_right = True
          if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
              self.rocket.going_up = False
            if event.key == pygame.K_DOWN:
              self.rocket.going_down = False
            if event.key == pygame.K_LEFT:
              self.rocket.going_left = False
            if event.key == pygame.K_RIGHT:
              self.rocket.going_right = False
  
  def _update_screen(self): #Helper function (denoted by a single underscore)
    """Update images on the screen, and flip to the new screen."""
    self.screen.fill((255,255,255))
    self.rocket.blitme()
    pygame.display.flip()  

if __name__ == '__main__':
    # Make a game instance and run the game.
  rg = Rocket_Game()
  rg.run_game()
