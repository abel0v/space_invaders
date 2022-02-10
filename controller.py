import pygame, sys
from bullet import Bullet


def events(screen, gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.rightmove = True

            elif event.key == pygame.K_a:
                gun.leftmove = True

            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.rightmove = False

            elif event.key == pygame.K_a:
                gun.leftmove = False


def screen_update(background, screen, gun, bullets):
    screen.fill(background)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    gun.output()
    pygame.display.flip()
