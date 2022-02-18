import pygame
import sys
import controller
from gun import Gun
from pygame.sprite import Group
from monsters import Monsters
from statistic import Statistic
import time
from scores import Scores


def start():
    pygame.init()
    pygame.display.set_caption('space')
    screen = pygame.display.set_mode((1200, 800))
    background = (0, 0, 0)
    clock = pygame.time.Clock()
    gun = Gun(screen)
    bullets = Group()
    monsters = Group()
    statistic = Statistic()
    sc = Scores(screen, statistic)
    controller.create_army(screen, monsters)

    while True:
        controller.events(screen, gun, bullets)
        if statistic.game_start:
            controller.screen_update(background, screen, statistic, sc, gun, monsters, bullets)
            bullets.update()
            gun.gun_update()
            controller.update_bullets(screen, statistic, sc, monsters, bullets)
            controller.monsters_update(statistic, screen, sc, gun, monsters, bullets)
            clock.tick(120)
