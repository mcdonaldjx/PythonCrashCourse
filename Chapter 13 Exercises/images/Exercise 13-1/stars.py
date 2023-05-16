#Created 5/16/2023
#Exercise 12-7- Stars: Find an image of a star. Make a grid of stars appear on the screen.

import pygame
from star import Star

class Stars:

  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((500, 500))
    self.bg_color = (255, 255, 255)
    self.stars = pygame.sprite.Group()
    self.create_stars()
    
  def run(self):
    while True:
      self._update_screen()

  def _update_screen(self):
    """Update images on the screen then flip to the new screen"""
    self.screen.fill(self.bg_color)
    self.stars.draw(self.screen)
    pygame.display.flip()
  
  def create_stars(self):
    s = Star(self)
    star_width, star_height = s.rect.size
    current_x, current_y = star_width, star_height
    while current_y < (500 - 2 * star_height):
      while current_x < (500 - star_width):
        self.create_star(current_x, current_y)
        current_x += 2 * star_width

      current_x = star_width
      current_y += 2 * star_height
        
        
  def create_star(self, x, y):
    star = Star(self)
    star.x = x
    star.y = y
    star.rect.x = x
    star.rect.y = y
    self.stars.add(star)
    
if __name__ == '__main__':
  game = Stars()
  game.run()
