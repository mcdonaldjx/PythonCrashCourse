#Created 05/03/2023
#Exercise 12-1- Blue Sky: Make a Pygame window with a blue background.

import pygame, sys

class Blue_Sky:
  """Overall class to manage game assets and behavior"""
  def __init__(self):
    """Initialize the game, and create game resources."""
    pygame.init()    
    self.screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Blue Sky")

    #Set the background color.
    self.bg_color = (0, 0, 200)
  
  def run_game(self):
    """Start the main loop for the game."""
    while True:
      # Watch for keyboard and mouse events. Events are actions that the user performs
      self._check_events()
      self._update_screen()

  def _check_events(self): #Helper function (denoted by a single underscore)
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get(): #Returns a list of events that have taken place since the last time this function was called
          if event.type == pygame.QUIT: #If the window's close button is clicked, exit the game
            sys.exit()
  
  def _update_screen(self): #Helper function (denoted by a single underscore)
    """Update images on the screen, and flip to the new screen."""
    self.screen.fill((0,0,200))
    pygame.display.flip()  

if __name__ == '__main__':
    # Make a game instance and run the game.
  bs = Blue_Sky()
  bs.run_game()
