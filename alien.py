import pygame
from pygame.sprite import Sprite
from settings import IMAGE_PATH


class Alien(Sprite):
    """A class representing one alien."""
    def __init__(self, ai_settings, screen):
        """Initializes a alien and sets his starting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load(IMAGE_PATH + 'alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blit_me(self):
        """Displays an alien in its current position."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Returns True if the alien is on the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Moves an alien to the right."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
