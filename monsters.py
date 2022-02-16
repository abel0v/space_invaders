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
        self.rect.y += 71

    def update(self):
        screen_rect = self.screen.get_rect() 
        for monster in monsters.sprites():
            if monster.rect.x < screen_rect.left:
                self.direction = -1
                self.down()
            elif monster.rect.x > screen_rect.right - 71:
                self.direction = 1
                self.down()

        if self.direction == 1:
            self.left()
        else:
            self.right()


