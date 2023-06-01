import pygame.font

class Button:

  def __init__(self, game, text):
    self.screen = game.screen
    self.screen_rect = game.screen.get_rect()
    self.width, self.height = len(text), 30
    self.button_color = (100, 0, 0)
    self.text_color = (255, 255, 255)
    self.font = pygame.font.SysFont(None, 48)
    self.rect = pygame.Rect(0, 0, self.width, self.height)
    if text == "Easy":
      self.rect.center = (50,250)
    elif text == "Medium":
      self.rect.center = self.screen_rect.center
    elif text == "Hard":
      #self.rect.right.x = self.screen_rect.midright.x
      self.rect.center = (450,250)
    self._prep_msg(text)

  def _prep_msg(self, text):
    self.text_image = self.font.render(text, True, self.text_color, self.button_color)
    self.text_image_rect = self.text_image.get_rect()
    self.text_image_rect.center = self.rect.center

  def draw_button(self):
    """Draw blank button and then draw message."""
    self.screen.fill(self.button_color, self.rect)
    self.screen.blit(self.text_image, self.text_image_rect)