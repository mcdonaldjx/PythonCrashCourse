#Created 5/16/2023
#Exercise 12-8- Better Stars: You can make a more realistic star pattern by introducing randomness when you place each star. Using your code in Exercise 13-1, adjust each star’s position by a random amount.

import pygame
from star import Star
from random import randint

class Better_Stars:

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
    random_x = randint(2, 10)
    random_y = randint(1, 10)
    while current_y < (500 - random_x * star_height):
      while current_x < (500 - random_y * star_width):
        self.create_star(current_x, current_y)
        current_x += random_x * star_width

      current_x = star_width
      current_y += random_y * star_height
        
        
  def create_star(self, x, y):
    star = Star(self)
    star.x = x
    star.y = y
    star.rect.x = x
    star.rect.y = y
    self.stars.add(star)
    
if __name__ == '__main__':
  game = Better_Stars()
  game.run()
