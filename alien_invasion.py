import pygame
from game_functions import check_events, update_screen
from ship import Ship
from settings import Settings


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_settings, screen)

    while True:
        check_events(ship)
        ship.update()
        update_screen(ai_settings, screen, ship)


run_game()
