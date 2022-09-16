import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_DOWN:
                    self.ship.moving_down = True
                elif event.type == pygame.K_UP:
                    self.ship.moving_up = True                    
                elif event.type == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.type == pygame.K_RIGHT:
                    self.ship.moving_right = True
            if event.type == pygame.KEYUP:
                if event.type == pygame.K_DOWN:
                    self.ship.moving_down = False
                elif event.type == pygame.K_UP:
                    self.ship.moving_up = False                    
                elif event.type == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.type == pygame.K_RIGHT:
                    self.ship.moving_right = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
    

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()