import pygame
import sys
import random
from vars import *


class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("snake")
        self.grid = [[0 for n in range(30)] for i in range(30)]
        self.cell_size = 20


    def run(self):
        while(True):
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        pass

    def draw(self):
        self.window.fill(WHITE)

        self.draw_grid(self.window)

        pygame.display.flip()

################################################################################
    # Grid is 30x30 (20 by 20)
    def draw_grid(self, window):
        x,y = 0, 0
        for row in self.grid:
            for col in self.grid:
                pygame.draw.rect(window, GREY, [x, y, self.cell_size, self.cell_size], 1)
                x += self.cell_size
            x = 0
            y += self.cell_size
