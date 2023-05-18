class Settings:
  """A class to store all the game's settings."""

  def __init__(self):
    """Initialize the game's settings."""
    #Screen settings
    self.screen_width = 800
    self.screen_height = 600
    self.bg_color = (255, 255, 255)

    #Ship settings
    self.ship_speed = 2.0

    #Bullet settings
    self.bullet_speed = 4.0
    self.bullet_width = 15
    self.bullet_height = 5

    #Alien settings
    self.alien_speed = 1.0
    self.fleet_drop_speed = 10
    # fleet_direction of 1 representions down; -1 represents up
    self.fleet_direction = 1