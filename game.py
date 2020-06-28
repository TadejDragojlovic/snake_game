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
        self.grid = [[0 for n in range(20)] for i in range(20)]
        self.cell_size = cell_size
        self.snake = Snake(2, 2)
        self.food = Food(self.snake.body)
        
        self.font = pygame.font.SysFont('arial', 48, True, False)

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
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_RIGHT and self.snake.dir != [-1, 0]:
                    self.snake.dir = [1, 0]
                if event.key == pygame.K_LEFT and self.snake.dir != [1, 0]:
                    self.snake.dir = [-1, 0]
                if event.key == pygame.K_UP and self.snake.dir != [0, 1]:
                    self.snake.dir = [0, -1]
                if event.key == pygame.K_DOWN and self.snake.dir != [0, -1]:
                    self.snake.dir = [0, 1]

    def update(self):
        self.snake.update(self.food.pos)
        if self.snake.eatt:
            self.food = Food(self.snake.body)
            self.snake.eatt = 0

        self.clock.tick(10)

    def draw(self):
        self.window.fill(WHITE)

        self.draw_grid(self.window)
        self.food.draw_food(self.window)
        self.snake.draw_snake(self.window)
        self.draw_score(self.window)

        pygame.display.flip()

################################################################################
    # Grid is 30x30 (20 by 20)
    def draw_grid(self, window):
        x,y = 0, 0
        for row in self.grid:
            for col in self.grid:
                pygame.draw.rect(window, WHITE, [x, y, self.cell_size, self.cell_size])
                x += self.cell_size
            x = 0
            y += self.cell_size

    def draw_score(self, window):
        text = self.font.render(str(self.snake.score), False, BLACK)
        window.blit(text, (530, 10))
