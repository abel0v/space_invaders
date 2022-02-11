import pygame
import pygame_menu
from typing import Tuple, Any
from space import Hp

pygame.init()
pygame.display.set_caption('Space Invaders')
programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)

surface = pygame.display.set_mode((600, 400))
click = pygame.mixer.Sound('Bat_2.wav')
click.set_volume(0.2)


pygame.mixer.music.load('menu.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)


# установка сложности
def set_difficulty(selected: Tuple, value: Any):
    print(f'Set difficulty to {selected[0]} ({value})')


# запуск игры
def start_the_game():
    global user_name
    print(f'{user_name.get_value()}, Do the job here!')

    Hp.start()
    # если кинуть что-нибудь сюда, оно откроется в отдельном окне, тут будет основная игра


# -------------тема---------
font = pygame_menu.font.FONT_MUNRO
mytheme = pygame_menu.themes.THEME_DARK.copy()
mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL
mytheme.title_font = font
mytheme.widget_font = font
mytheme.title_background_color = (72, 61, 139)
mytheme.background_color = (51, 51, 51)
menu = pygame_menu.Menu('Space Invaders', 600, 400,
                        theme=mytheme)
# ------------------------------

# clock = pygame.time.Clock()
# done = False
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP] or keys[pygame.K_DOWN]:
#         click.play()
#         pygame.display.flip()

user_name = menu.add.text_input('Name:', default=' ', font_color=(240, 230, 140))

menu.add.selector('difficulty:', [('Hard', 1), ('Easy', 3)], onchange=set_difficulty, font_color=(240, 230, 140))
menu.add.button('Sound', font_color=(240, 230, 140))
menu.add.button('Play!', start_the_game, font_color=(240, 230, 140))
menu.add.button('Exit', pygame_menu.events.EXIT, font_color=(240, 230, 140))

menu.mainloop(surface)
