import pygame
import sys
import random
from vars import *
from snake import *
from food import *


class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("snake")
        self.clock = pygame.time.Clock()
        self.grid = [[0 for n in range(30)] for i in range(30)]
        self.cell_size = 20
        self.snake = Snake(2, 2, self.cell_size, self.cell_size)

        self.food = Food(self.snake.pos[0], self.snake.pos[1])

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.snake.dir = [1, 0]
                if event.key == pygame.K_LEFT:
                    self.snake.dir = [-1, 0]
                if event.key == pygame.K_UP:
                    self.snake.dir = [0, -1]
                if event.key == pygame.K_DOWN:
                    self.snake.dir = [0, 1]

    def update(self):
        self.snake.update()
        self.clock.tick(10)

    def draw(self):
        self.window.fill(GREY)

        self.draw_grid(self.window)
        self.food.draw_food(self.window)
        self.snake.draw_snake(self.window)

        pygame.display.flip()

################################################################################
    # Grid is 30x30 (20 by 20)
    def draw_grid(self, window):
        x,y = 0, 0
        for row in self.grid:
            for col in self.grid:
                pygame.draw.rect(window, BLACK, [x, y, self.cell_size, self.cell_size], 1)
                x += self.cell_size
            x = 0
            y += self.cell_size
