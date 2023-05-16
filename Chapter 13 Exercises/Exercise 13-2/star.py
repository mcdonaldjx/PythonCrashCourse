import pygame
from pygame.sprite import Sprite

class Star(Sprite):

  def __init__(self, game):
    super().__init__()
    self.image = pygame.image.load('images/star.bmp')
    self.screen = game.screen
    self.rect = self.image.get_rect()
    
