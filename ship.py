import pygame

class Ship:

    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

# Movement flag
    def update(self):
        if self.moving_right:
            self.rect.x += 10
        elif self.moving_left:
            self.rect.x -= 10
        elif self.moving_up:
            self.rect.y += 10
        elif self.moving_down:
            self.rect.y -= 10
