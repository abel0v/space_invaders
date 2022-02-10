import pygame

<<<<<<<< HEAD:main_menu.py
pygame.init()
surface = pygame.display.set_mode((1200, 800))
background = (0, 0, 0)
gun = Gun(surface)


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
========
class game():
    def rungame():
        pygame.init()
        pygame.display.set_caption('Движущийся круг 2')
        size = width, height = 800, 400
        screen = pygame.display.set_mode(size)

        running = True
        x_pos = 0
        v = 50  # пикселей в секунду
        fps = 60
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((0, 0, 0))
            pygame.draw.circle(screen, (255, 0, 0), (int(x_pos), 200), 20)
            x_pos += v / fps
            if x_pos >= 800:
                x_pos = 0
            clock.tick(fps)
            pygame.display.flip()
        pygame.quit()
       
>>>>>>>> origin/master:Main.py
