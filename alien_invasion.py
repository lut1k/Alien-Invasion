import pygame
from pygame.sprite import Group
from game_functions import check_events, update_screen, update_bullets
from ship import Ship
from settings import Settings


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_settings, screen)
    bullets = Group()

    while True:
        check_events(ai_settings, screen, ship, bullets)
        ship.update()
        update_bullets(bullets)
        update_screen(ai_settings, screen, ship, bullets)


if __name__ == '__main__':
    run_game()

