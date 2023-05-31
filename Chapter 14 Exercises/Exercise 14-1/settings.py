class Settings:
  """A class to store all the game's settings."""

  def __init__(self):
    """Initialize the game's settings."""
    #Screen settings
    self.screen_width = 800
    self.screen_height = 600
    self.bg_color = (230, 230, 230)

    #Ship settings
    self.ship_speed = 2.0
    self.ship_limit = 3
    
    #Bullet settings
    self.bullet_speed = 4.0
    self.bullet_width = 300
    self.bullet_height = 15
    self.bullet_color = (60, 60, 60)
    self.bullets_allowed = 3

    #Alien settings
    self.alien_speed = 1.0
    self.fleet_drop_speed = 10
    # fleet_direction of 1 representions right; -1 represents left
    self.fleet_direction = 1