class Settings:
  """A class to store all the game's settings."""

  def __init__(self):
    """Initialize the game's settings."""
    #Screen settings
    self.screen_width = 800
    self.screen_height = 600
    self.bg_color = (255, 255, 255)
    self.misses = 0

    #Ship settings
    self.ship_speed = 2.0

    #Bullet settings
    self.bullet_speed = 3.0
    self.bullet_width = 15
    self.bullet_height = 5

    #Target settings
    self.target_speed = float(2.0)
    self.speedup_scale = 1.1
    self.target_direction = 1
    
    self.reset_target_settings()

  def reset_target_settings(self):
    self.target_speed = 2.0
    self.target_direction *= -1
  
  def increase_speed(self):
    self.target_speed *= self.speedup_scale