import sys

import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """" Overall class to manage game assets and behavior """

    def __init__(self):
        """" Initialize the game, and create game resources """
        pygame.init()
        settings = Settings()
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        pygame.display.set_caption("Igor Invasion")
        # Set the background color.
        self.bg_color = settings.bg_color
        # Initialize our ship
        self.ship = Ship(self)

    def _check_events(self):
        # Respond to keypresses and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                # move the ship to the right
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False


    def _update_screen(self):
        # Redrow the screen during each pass through the loop.
        self.screen.fill(self.bg_color)
        # show ship
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def run_game(self):
        """" Start the main loop for the game. """
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()
            self._update_screen()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
