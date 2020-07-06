from os.path import abspath, dirname
from pygame import image

BASE_PATH = abspath(dirname(__file__))
IMAGE_PATH = BASE_PATH + '/images/'


class Settings:
    """
    Class for storing all the settings of the game Alien Invasion.
    """
    def __init__(self):
        """Initializes game static settings."""
        self.screen_width = 1280
        self.screen_height = 720
        self.background = image.load(IMAGE_PATH + 'background.jpg')  # TODO: разобраться
        self.bg_color = (230, 230, 230)

        # Ship options
        self.ship_limit = 3

        # Bullet options
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 5

        # Game acceleration
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializes settings that change during the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1.5

        # Aliens options
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 - move right; -1 - move left

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increases speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
