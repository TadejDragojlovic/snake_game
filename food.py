import pygame, random
from vars import *

class Food():
    def __init__(self, snake_body):
        self.width = cell_size
        self.height = cell_size
        self.food_body = pygame.Surface((self.width, self.height))
        self.food_rect = self.food_body.get_rect()

        self.pos = self.set_pos(snake_body)
        self.food_rect.topleft = self.pos

    def draw_food(self, window):
        self.food_body.fill(RED)
        window.blit(self.food_body, self.pos)

    def set_pos(self, snake_body):
        pos = [12*cell_size, 10*cell_size]
        while pos in snake_body:
            pos = [random.randint(0, 19)*cell_size, random.randint(0, 19)*cell_size]
        return pos
