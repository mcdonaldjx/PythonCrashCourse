#Created 5/16/2023
#Exercise 13-4- Steady Rain: Find an image of a raindrop and create a grid of raindrops. Make the raindrops fall toward the bottom of the screen until they disappear.

import pygame
from raindrop import Raindrop

class Steady_Rain:

  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((500, 500))
    self.bg_color = (255, 255, 255)
    self.drops = pygame.sprite.Group()
    self.create_drops()
    
  def run(self):
    while True:
      self._update_drops()
      self._update_screen()

  def _update_screen(self):
    """Update images on the screen then flip to the new screen"""
    self.screen.fill(self.bg_color)
    self.drops.draw(self.screen)
    pygame.display.flip()
  
  def create_drops(self):
    s = Raindrop(self)
    drop_width, drop_height = s.rect.size
    current_x, current_y = drop_width, drop_height
    while current_y < (500 - 3 * drop_height):
      while current_x < (500 - 2 * drop_width):
        self.create_drop(current_x, current_y)
        current_x += 2 * drop_width

      current_x = drop_width
      current_y += 2 * drop_height
        
        
  def create_drop(self, x, y):
    drop = Raindrop(self)
    drop.x = x
    drop.y = y
    drop.rect.x = x
    drop.rect.y = y
    self.drops.add(drop)

  def _update_drops(self):
    for drop in self.drops:
      drop.update()
    for drop in self.drops.copy():
      if drop.rect.top >= 500:
        self.drops.remove(drop)
        self.create_drop(drop.x, drop.rect.height) #Create a new drop at the same x, but a different y
    
if __name__ == '__main__':
  game = Steady_Rain()
  game.run()
