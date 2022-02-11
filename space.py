import pygame
import sys
import controller
from gun import Gun
from pygame.sprite import Group
from monsters import Monsters
from statistic import Statistic
import time



def start():
    pygame.init()
    pygame.display.set_caption('space')
    screen = pygame.display.set_mode((1200, 800))
    background = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    monsters = Group()
    statistic = Statistic()
    controller.create_army(screen, monsters)


    while True:
        controller.events(screen, gun, bullets)
        controller.screen_update(background, screen, gun, monsters, bullets)
        bullets.update()
        gun.gun_update()
        controller.update_bullets(monsters, bullets)
        controller.monsters_update(statistic, screen, gun, monsters, bullets)


start()
