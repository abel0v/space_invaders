import pygame


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
