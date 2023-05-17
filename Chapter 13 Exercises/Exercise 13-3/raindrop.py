import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):

  def __init__(self, game):
    super().__init__()
    self.image = pygame.image.load('images/raindrop.bmp')
    self.screen = game.screen
    self.rect = self.image.get_rect()
    self.speed = float(1.1)

  def update(self):
    self.y += self.speed
    self.rect.y = self.y
    
