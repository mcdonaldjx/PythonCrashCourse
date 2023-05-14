import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
  """A class to manage bullets fired from the ship."""

  def __init__(self, ai_game):
    """Create a bullet object at the ship's current position."""
    super().__init__()
    self.screen = ai_game.screen
    self.settings = ai_game.settings
    self.color = self.settings.bullet_color

    #Create a bullet rect at (0, 0) and then set correct position.
    self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height) #Create a rect from scratch
    self.rect.midtop = ai_game.ship.rect.midtop #Match the ship's midtop to the bullet's so it looks like it was fired from the ship

    #Store the bullet's position as a float to match later finer adjustments to the speed
    self.y = float(self.rect.y)

  def update(self):
    """Move the bullet up the screen. Manages the bullet's position."""
    #Update the exact position of the bullet.
    self.y -= self.settings.bullet_speed
    #Update the rect position.
    self.rect.y = self.y

  def draw_bullet(self):
    """Draw the bullet to the screen."""
    pygame.draw.rect(self.screen, self.color, self.rect)
