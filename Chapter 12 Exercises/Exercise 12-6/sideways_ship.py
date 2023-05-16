import pygame

class Ship:

  def __init__(self, game):
    self.image = pygame.image.load('images/sideways_ship.bmp')
    self.screen = game.screen
    self.screen_rect = self.screen.get_rect()
    self.rect = self.image.get_rect()
    self.y = float(250)
    self.moving_up = False
    self.moving_down = False

  def update(self):
    if self.moving_up and self.rect.top > 0:
      self.y -= 1
    elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
      self.y += 1
    self.rect.y = self.y
  def blitme(self):
    self.screen.blit(self.image, self.rect)
  
