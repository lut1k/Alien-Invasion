import pygame
from pygame.sprite import Group
from button import Button
from game_functions import check_events, update_screen, update_bullets, create_fleet, update_aliens
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from settings import Settings


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    scoreboard = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    create_fleet(ai_settings, screen, ship, aliens)

    while True:
        check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets, scoreboard)
        update_screen(ai_settings, screen, stats, scoreboard, ship, aliens, bullets, play_button)
        if stats.game_active:
            update_bullets(ai_settings, screen, stats, scoreboard, ship, aliens, bullets)
            ship.update()
            update_aliens(ai_settings, stats, screen, ship, scoreboard, aliens, bullets)


if __name__ == '__main__':
    run_game()

