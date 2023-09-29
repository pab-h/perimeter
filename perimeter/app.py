import pygame

from figure import Figure

class App:
    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode((600, 600))

        self.clock = pygame.time.Clock()

        self.fps = 30

        self.runnig = False

        self.figure = Figure()

    def __del__(self):
        pygame.quit()

    def run(self):
        self.runnig = True

        while self.runnig:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runnig = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.display.fill("BLACK")
                    self.figure.add_vetex_by_mouse()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.figure.stroke(self.display)

            self.figure.draw(self.display)

            pygame.display.update()

            self.clock.tick(self.fps)