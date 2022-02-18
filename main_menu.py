import pygame
import pygame_menu
from pygame_menu import sound
from typing import Tuple, Any
import space

pygame.init()
pygame.display.set_caption('Space Invaders')
programIcon = pygame.image.load('data/icon.png')
pygame.display.set_icon(programIcon)

surface = pygame.display.set_mode((600, 400))
click = pygame.mixer.Sound('data/Bat_2.wav')
click.set_volume(0.2)

engine = sound.Sound()
engine.set_sound(sound.SOUND_TYPE_KEY_ADDITION, 'data/Bat_2.wav')
engine.set_sound(sound.SOUND_TYPE_KEY_DELETION, 'data/Button_2.wav')

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
    space.start()


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

user_name = menu.add.text_input('Name: ', default='', font_color=(240, 230, 140), shadow=True)
menu.add.vertical_margin(5)
menu.add.selector('difficulty:', [('Hard', 1), ('Easy', 3)], onchange=set_difficulty, font_color=(240, 230, 140))
menu.add.vertical_margin(5)
menu.add.button('Play!', start_the_game, font_color=(240, 230, 140))
menu.add.vertical_margin(10)
menu.add.button('Exit', pygame_menu.events.EXIT, font_color=(240, 230, 140))
menu.set_sound(engine, recursive=True)
menu.mainloop(surface)
