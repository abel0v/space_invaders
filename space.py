import pygame
import sys
import controller
from gun import Gun
from pygame.sprite import Group

def start():
    pygame.init()
    pygame.display.set_caption('space')
    screen = pygame.display.set_mode((1200, 800))
    background = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()

    while True:
        controller.events(screen, gun, bullets)
        controller.screen_update(background, screen, gun, bullets)
        bullets.update()
        gun.gun_update()


start()
