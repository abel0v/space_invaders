import pygame, sys
from bullet import Bullet
from monsters import Monsters


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


def screen_update(background, screen, gun, monsters, bullets):
    screen.fill(background)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    gun.output()
    monsters.draw()
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_army(screen, monsters):
    monster = Monsters(screen)
    monster_width = monster.rect.width
    number_ino_x = int((700 - 2 * monster_width) / monster_width)
    for monster_number in range(number_ino_x):

        ino = Monsters(screen)
        ino.x = monster_width + monster_width * monster_number
        ino.rect.x = ino.x
        monsters.add(monster)
