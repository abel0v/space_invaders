import pygame.font
from gun import Gun
from pygame.sprite import Group


class Scores:

    def __init__(self, screen, statistic):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.statistic = statistic
        self.text_color = (139, 195, 74)
        self.font = pygame.font.SysFont(None, 36)
        self.image_scores()
        self.image_main_score()
    
    def image_scores(self):
        """преобразывает текст счета в графическое изображение"""
        self.score_img = self.font.render(str(self.statistic.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_main_score(self):
        self.main_score_image = self.font.render(str(self.statistic.main_score), True, self.text_color, (0, 0, 0))
        self.main_score_rect = self.main_score_image.get_rect()
        self.main_score_rect.centerx = self.screen_rect.centerx
        self.main_score_rect.top = self.screen_rect.top + 20

    
    def show_score(self):
        """вывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.main_score_image, self.main_score_rect)
        
