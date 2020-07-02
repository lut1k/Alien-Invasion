from os.path import abspath, dirname

from pygame import image, transform

BASE_PATH = abspath(dirname(__file__))
IMAGE_PATH = BASE_PATH + '/images/'


class Settings:
    """
    Class for storing all the settings of the game Alien Invasion.
    """
    def __init__(self):
        """Initializes game settings."""
        self.screen_width = 1280
        self.screen_height = 720
        self.background = image.load(IMAGE_PATH + 'background.jpg')  # TODO: разобраться
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5

        # Bullet options
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 5

        # Aliens options
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 1
        self.fleet_direction = 1  # 1 - move right; -1 - move left
