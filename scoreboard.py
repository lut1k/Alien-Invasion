import pygame.font


class Scoreboard:
    """Class for displaying game information."""

    def __init__(self, ai_settings, screen, stats):
        """Initializes evaluation attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for score output
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Converts the current score into a graphic image."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{0:,}".format(round(rounded_score))
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # The score is displayed in the upper right corner of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Display score."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def prep_high_score(self):
        """Converts an record score into a graphic image."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{0:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top