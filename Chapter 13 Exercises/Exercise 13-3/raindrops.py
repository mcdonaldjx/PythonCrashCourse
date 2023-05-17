#Created 5/16/2023
#Exercise 13-3- Raindrops: Find an image of a raindrop and create a grid of raindrops. Make the raindrops fall toward the bottom of the screen until they disappear.

import pygame
from raindrop import Raindrop

class Raindrops:

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
    star_width, star_height = s.rect.size
    current_x, current_y = star_width, star_height
    while current_y < (500 - 3 * star_height):
      while current_x < (500 - 2 * star_width):
        self.create_drop(current_x, current_y)
        current_x += 2 * star_width

      current_x = star_width
      current_y += 2 * star_height
        
        
  def create_drop(self, x, y):
    star = Raindrop(self)
    star.x = x
    star.y = y
    star.rect.x = x
    star.rect.y = y
    self.drops.add(star)

  def _update_drops(self):
    for drop in self.drops:
      drop.update()
    for drop in self.drops.copy():
      if drop.rect.top >= 500:
        self.drops.remove(drop)
    
if __name__ == '__main__':
  game = Raindrops()
  game.run()
  
