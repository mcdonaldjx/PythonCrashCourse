import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

  def __init__(self, game):
    super().__init__()
    self.screen = game.screen
    self.color = (255,165,0)

    self.rect = pygame.Rect(0, 0, 15, 5)
    self.rect.midright = game.ship.rect.midright
    self.x = float(self.rect.x)

  def update(self):
    self.x += 3
    self.rect.x = self.x

  def draw_bullet(self):
    pygame.draw.rect(self.screen, self.color, self.rect)
