import pygame
import sys
import controller
from gun import Gun
from pygame.sprite import Group
from monsters import Monsters


class Hp(pygame.sprite.Sprite):
    def start():
        pygame.init()
        pygame.display.set_caption('space')
        screen = pygame.display.set_mode((1200, 800))

        background = (0, 0, 0)
        gun = Gun(screen)
        bullets = Group()
        monsters = Group()
        monsters2 = Group()
        controller.create_army(screen, monsters)

        while True:
            controller.events(screen, gun, bullets)
            controller.screen_update(background, screen, gun, monsters, monsters2, bullets)
            bullets.update()
            gun.gun_update()
