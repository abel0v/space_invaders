import pygame, sys
from bullet import Bullet
from monsters import Monsters
import time


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
    monsters.draw(screen)
    pygame.display.flip()


def update_bullets(monsters, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, monsters, True, True)


def checker(statistic, screen, gun, monsters, bullets):
    screen_rect = screen.get_rect()
    for monster in monsters.sprites():
        if monster.rect.bottom >= screen_rect.bottom:
            gun_kill(statistic, screen, gun, monsters, bullets)
            break


def create_army(screen, monsters):
    monster = Monsters(screen)
    monster_width = monster.rect.width
    number_monster_x = int((1200 - 2 * monster_width) / monster_width)
    monster_height = monster.rect.height
    number_monster_y = int((400 - 100 - 2 * monster_height) / monster_height)
    for row_number in range(number_monster_y):
        for monster_number in range(number_monster_x):
            monster = Monsters(screen)
            monster.x = monster_width + monster_width * monster_number
            monster.y = monster_height + monster_height * row_number
            monster.rect.x = monster.x
            monster.rect.y = monster.rect.height + 2 * monster.rect.height * row_number
            monsters.add(monster)


def monsters_update(statistic, screen, gun, monsters, bullets):
    monsters.update()
    if pygame.sprite.spritecollideany(gun, monsters):
        gun_kill(statistic, screen, gun, monsters, bullets)
    checker(statistic, screen, gun, monsters, bullets)


def gun_kill(statistic, screen, gun, monsters, bullets):
    statistic.guns_left -= 1
    monsters.empty()
    bullets.empty()
    gun.create_gun()
    create_army(screen, monsters)
    time.sleep(2)
