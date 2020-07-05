import pygame
from settings import IMAGE_PATH


class Ship:

    def __init__(self, ai_settings, screen):
        """Initializes the ship and sets its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading a ship image and getting a rectangle.
        self.image = pygame.image.load(IMAGE_PATH + 'ship.bmp')
        self.rect = self.image.get_rect()

        # Each new ship appears at the bottom of the screen.
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the position of the ship with the flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blit_me(self):
        """Draws a ship at its current position."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Places the ship in the center of the lower side."""
        self.center = self.screen_rect.centerx
