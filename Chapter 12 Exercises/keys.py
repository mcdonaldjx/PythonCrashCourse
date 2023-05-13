#Created 05/13/2023
#Exercise 12-5- Keys: Make a Pygame file that creates an empty screen. In the event loop, print the event.key attribute whenever a pygame.KEYDOWN event is detected. Run the program and press various keys to see how Pygame responds. 
import pygame, sys

class Keys:
  """Overall class to manage game assets and behavior"""
  def __init__(self):
    """Initialize the game, and create game resources."""
    pygame.init()    
    self.screen = pygame.display.set_mode((250, 250))
    pygame.display.set_caption("Keys Game")

    #Set the background color.
    self.bg_color = (255, 255, 255)
  
  def run_game(self):
    """Start the main loop for the game."""
    while True:
      # Watch for keyboard and mouse events. Events are actions that the user performs
      self._check_events()

  def _check_events(self): #Helper function (denoted by a single underscore)
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
          if event.type == pygame.QUIT: #If the window's close button is clicked, exit the game
            sys.exit()
          if event.type == pygame.KEYDOWN:
            self.print_attribute(event)
            
  def print_attribute(self, event):
    print(f"{event.key} ({pygame.key.name(event.key)}) is currently pressed down!")
    if event.key == pygame.K_q:
      sys.exit()

if __name__ == '__main__':
    # Make a game instance and run the game.
  k = Keys()
  k.run_game()
