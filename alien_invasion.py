import pygame
from pygame.sprite import Group
from game_functions import check_events, update_screen, update_bullets, create_fleet, update_aliens
from game_stats import GameStats
from ship import Ship
from settings import Settings


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    create_fleet(ai_settings, screen, ship, aliens)

    while True:
        check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            update_bullets(ai_settings, screen, ship, aliens, bullets)
            update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            update_screen(ai_settings, screen, ship, aliens, bullets)


if __name__ == '__main__':
    run_game()

