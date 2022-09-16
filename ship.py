import pygame
from settings import Settings

#Class Ship keeps instruction to create and move the spaceship
class Ship:
    
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

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

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.settings.ship_speed
        #I WANT MOVE ONLY FOR LEFT AND RIGHT FOR NOW
        #elif self.moving_up and self.rect.top > self.screen_rect.top:
        #    self.rect.y -= self.settings.ship_speed
        #elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
        #    self.rect.y += self.settings.ship_speed
