#Created 05/13/2023
#Exercise 12-4- Rocket: Make a game that begins with a rocket in the center of the screen. Allow the player to move the rocket up, down, left, or right using the four arrow keys. Make sure the rocket never moves beyong any edge of the screen.
import pygame

class Rocket:

  def __init__(self, r_game):
    self.screen = r_game.screen
    self.screen_rect = r_game.screen.get_rect()

    #Load the ship image and get its rect.
    self.image = pygame.image.load('rocketship.png')
    self.rect = self.image.get_rect()
    self.rect.center = self.screen_rect.center

    #Store floats of the rocket's positions
    self.x = float(self.rect.x)
    self.y = float(self.rect.y)
    #Movement flags; start with a ship that not moving
    self.going_right = False
    self.going_left = False
    self.going_up = False
    self.going_down = False

  def update(self):
    if self.going_left and self.rect.left > 0:
      self.x -= 1
    if self.going_right and self.rect.right < self.screen_rect.right:
      self.x += 1
    if self.going_up and self.rect.top > 0:
      self.y -= 1
    if self.going_down and self.rect.bottom < self.screen_rect.bottom:
      self.y += 1
    self.rect.y = self.y
    self.rect.x = self.x

  def blitme(self):
    self.screen.blit(self.image, self.rect)
