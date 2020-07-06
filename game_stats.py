class GameStats:
    """Tracking statistics for the game Alien Invasion"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Initializes statistics that change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
