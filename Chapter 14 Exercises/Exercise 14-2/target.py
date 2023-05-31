import pygame
from pygame.sprite import Sprite

class Target(Sprite):

    def __init__(self, game):
      super().__init__()
      self.screen = game.screen
      self.color = (255,0,0)
      self.game = game
      self.rect = pygame.Rect(450, 250, 20, 60)
      self.x = float(self.rect.x)
      self.y = float(self.rect.y)

    def update(self):
      self.y += self.game.settings.target_speed * self.game.settings.target_direction
      self.rect.y = self.y
  
    def check_edges(self):
      screen_rect = self.screen.get_rect()
      return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0)

    def draw(self):
      pygame.draw.rect(self.screen, self.color, self.rect)