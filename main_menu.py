import pygame
import pygame_menu
from pygame_menu import sound
from typing import Tuple, Any
import space
import sys
from controller import set_diff

pygame.init()
pygame.display.set_caption('Space Invaders')
programIcon = pygame.image.load('data/icon.png')
pygame.display.set_icon(programIcon)

surface = pygame.display.set_mode((600, 400))
click = pygame.mixer.Sound('data/Bat_2.wav')
click.set_volume(0.2)

engine = sound.Sound()
engine.set_sound(sound.SOUND_TYPE_KEY_ADDITION, 'data/Bat_2.wav')

pygame.mixer.music.load('data/menu.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)


# установка сложности
def set_difficulty(selected: Tuple, value: Any):
    print(f'Set difficulty to {selected[0]} ({value})')
    set_diff(value)
# запуск игры
def start_the_game():
    global user_name
    space.start()
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


user_name = menu.add.text_input('Name:', default=' ', font_color=(240, 230, 140))
menu.add.selector('Difficulty:', [('Hard', 1), ('Easy', 3)], onchange=set_difficulty, font_color=(240, 230, 140))
menu.add.button('Play!', start_the_game, font_color=(240, 230, 140))
menu.add.button('Exit', pygame_menu.events.EXIT, font_color=(240, 230, 140))
menu.set_sound(engine, recursive=True)
menu.mainloop(surface)
