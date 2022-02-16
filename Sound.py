import pygame_menu
import pygame


class Mixers(pygame.sprite.Sprite):
    def sounder():
        pygame.init()
        pygame.display.set_caption('Space Invaders')
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        font = pygame_menu.font.FONT_MUNRO
        mytheme = pygame_menu.themes.THEME_DARK.copy()
        mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL
        mytheme.title_font = font
        mytheme.widget_font = font
        mytheme.title_background_color = (72, 61, 139)
        mytheme.background_color = (51, 51, 51)
        surface = pygame.display.set_mode((600, 400))
        menu = pygame_menu.Menu('Space Invaders', 600, 400, theme=mytheme)
        menu.add.range_slider('Sound', 100, (0, 100), 1,
                              rangeslider_id='range_slider',
                              value_format=lambda x: str(int(x)), align=pygame_menu.locals.ALIGN_LEFT)
        menu.add.range_slider('Sound effects', 100, (0, 100), 1,
                              rangeslider_id='range_sliders',
                              value_format=lambda x: str(int(x)), align=pygame_menu.locals.ALIGN_LEFT)
        menu.mainloop(surface)
