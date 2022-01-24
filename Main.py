import pygame

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
       
