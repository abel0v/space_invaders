import pygame

class Game:
    def __init__(self):
        self.x_pos = 400
        self.v = 20 
        self.fps = 60
        self.running = True
        self.x_ch = 0
    def run(self):
        pygame.init()
        
        playerImage = pygame.image.load('main_spr/space_gg.png')
        spaceInvader = pygame.image.load('main_spr/space_invader1.png')
        bulletImage = pygame.image.load('main_spr/space_bullet.png')

        pygame.display.set_caption('Space Invader')

        size = width, height = 800, 600
        screen = pygame.display.set_mode(size)
        clock = pygame.time.Clock()
        bulet_x = -100
        bulet_y = -100
        bullets = []
        def player(x):
            screen.blit(playerImage, (x - 35, 500 + 10))

        '''def bullet(x, y):
            screen.blit(bulletImage, (x, y))'''

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x_ch = -1.7 
                    if event.key == pygame.K_RIGHT:
                        self.x_ch = 1.7
                    if event.key == pygame.K_SPACE:
                        bullets.append((len(bullets), [self.x_pos + 2, 430]))
                        '''bulet_x = self.x_pos + 2
                        bulet_y = 500'''
                if event.type == pygame.KEYUP:
                    self.x_ch = 0
            self.x_pos += self.x_ch
            screen.fill((0, 0, 0))
            #pygame.draw.circle(screen, (255, 0, 0), (int(self.x_pos), 300), 20)
            pygame.draw.line(screen, (0, 255, 0), (400, 0), (400, 600), 2)
            #screen.blit(playerImage, (int(self.x_pos - 35), 500))
            player(self.x_pos)
            
            for i in bullets:
                print(i[0], i[1][0], i[1][1])
                i[1][1] -= 20                    
                screen.blit(bulletImage, (i[1][0], i[1][1]))
                #bullet(i[0], bulet_y)

            if self.x_pos <= 0:
                self.x_pos = 0
            elif self.x_pos >= 800:
                self.x_pos = 800
            
            clock.tick(self.fps)
            pygame.display.update()
        pygame.quit()
game = Game()
game.run()
