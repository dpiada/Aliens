import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.moving_right = False
        self.moving_left = False
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # Make the most recently drawn screen visible.
                pygame.display.flip()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.K_s:
                self.ship.rect.y -= 10
            elif event.type == pygame.K_w:
                self.ship.rect.y += 10
            elif event.type == pygame.K_d:
                self.ship.rect.x += 10
            elif event.type == pygame.K_a:
                self.ship.rect.x -= 10


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
    

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()