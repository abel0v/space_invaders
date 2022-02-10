import pygame


class Gun():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('data/space_gg.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.center = float(self.rect.centerx)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.rightmove = False
        self.leftmove = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def gun_update(self):
        if self.rightmove and self.rect.right < self.screen_rect.right:
            self.center += 1.5

        if self.leftmove and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center
