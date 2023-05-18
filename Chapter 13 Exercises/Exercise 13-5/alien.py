import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, game):
      super().__init__()
      self.image = pygame.image.load('images/alien.bmp')
      self.game = game
      self.screen = game.screen
      self.rect = self.image.get_rect()
      self.x = self.rect.x
      self.y = self.rect.y

    def update(self):
      self.y += self.game.settings.alien_speed * self.game.settings.fleet_direction
      self.rect.y = self.y
  
    def check_edges(self):
      screen_rect = self.screen.get_rect()
      return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0)
  