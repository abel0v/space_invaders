import pygame
import time


class Monsters(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Monsters, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('data/space_invader1.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def right(self):
        self.x += 0.1
        self.rect.x = self.x

    def left(self):
        self.x -= 0.1
        self.rect.x = self.x

    def down(self):
        self.y += 0.1
        self.rect.y = self.y

    def update(self):
        self.down()

