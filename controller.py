import pygame, sys
from bullet import Bullet
from space_monsters import Monsters
import time


def events(screen, gun, bullets):
    Sound1 = pygame.mixer.Sound('data/W.wav')
    Sound1.set_volume(0.2)
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
                Sound1.play()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.rightmove = False

            elif event.key == pygame.K_a:
                gun.leftmove = False


def screen_update(background, screen, statistic, sc, gun, monsters, bullets):
    screen.fill(background)
    for i in range(statistic.guns_left):
        img = pygame.image.load("data/space_gg.png")
        screen.blit(img, (20 + i * 80, 5))
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    gun.output()
    monsters.draw(screen)
    pygame.display.flip()


def update_bullets(screen, statistic, sc, monsters, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, monsters, True, True)

    if collisions:
        for monsters in collisions.values():
            statistic.score += 10 * len(monsters)

        sc.image_scores()
        check_main_score(statistic, sc)
    if len(monsters) == 0:
        bullets.empty()
        create_army(screen, monsters)


def checker(statistic, screen, gun, sc, monsters, bullets):
    screen_rect = screen.get_rect()
    for monster in monsters.sprites():
        if monster.rect.bottom >= screen_rect.bottom - 46:
            gun_kill(statistic, screen, sc, gun, monsters, bullets)
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

def set_diff(dif=1):
    if dif == 1:
        Monsters.speed = 0.7
    else:
        Monsters.speed = 0.3

def monsters_update(statistic, screen, sc, gun, monsters, bullets):
    monsters.update(monsters)
    if pygame.sprite.spritecollideany(gun, monsters):
        gun_kill(statistic, screen, sc, gun, monsters, bullets)
    checker(statistic, screen, sc, gun, monsters, bullets)


def gun_kill(statistic, screen, sc, gun, monsters, bullets):
    if statistic.guns_left > 0:
        statistic.guns_left -= 1
        monsters.empty()
        bullets.empty()
        create_army(screen, monsters)
        time.sleep(2)
    else:
        img = pygame.image.load("data/game_over.png")
        statistic.game_start = False
        Sound2 = pygame.mixer.Sound('data/New_zone.wav')
        Sound2.set_volume(0.6)
        screen.fill((0, 0, 0))
        screeng = pygame.display.set_mode((1200, 800))
        time.sleep(0.5)
        Sound2.play()
        screeng.blit(img, (400, 200))
        pygame.display.flip()
        time.sleep(5)
        sys.exit()

def check_main_score(statistic, sc):
    if statistic.score > statistic.main_score:
        statistic.main_score = statistic.score
        sc.image_main_score()
        with open('main_score.txt', 'w') as f:
            f.write(str(statistic.main_score))
