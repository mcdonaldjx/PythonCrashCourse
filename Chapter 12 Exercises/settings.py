class Settings:
  """A class to store all the game's settings."""

  def __init__(self):
    """Initialize the game's settings."""
    #Screen settings
    self.screen_width = 800
    self.screen_height = 600
    self.bg_color = (230, 230, 230)

    #Ship settings
    self.ship_speed = 6.0
