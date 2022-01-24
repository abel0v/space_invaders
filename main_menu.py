import pygame
import pygame_menu
from main import game 
from typing import Tuple, Any

pygame.init()
surface = pygame.display.set_mode((600, 400))


def set_difficulty(selected: Tuple, value: Any):
    print(f'Set difficulty to {selected[0]} ({value})')


def start_the_game():
    global user_name
    print(f'{user_name.get_value()}, Do the job here!')
    game.rungame()
    # если кинуть что-нибудь сюда, оно откроется в отдельном окне, тут будет основная игра


menu = pygame_menu.Menu('Space Invaders', 600, 400,
                        theme=pygame_menu.themes.THEME_DARK)

user_name = menu.add.text_input('Имя:', default=' ')
menu.add.selector('Сложность игры: ', [('Hard', 1), ('Easy', 3)], onchange=set_difficulty)
menu.add.button('Играть!', start_the_game)
menu.add.button('Выход', pygame_menu.events.EXIT)
menu.mainloop(surface)
