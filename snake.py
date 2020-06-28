import pygame, sys
from vars import *
from food import *
from game import *

class Snake():
    def __init__(self, x, y, width, height):
        self.pos = [x*20, y*20]
        self.width = width
        self.height = height
        self.snake_body = pygame.Surface((self.width, self.height))
        self.rect = self.snake_body.get_rect()
        self.rect.topleft = self.pos
        self.length = 1
        self.eatt = 0

        self.dir = [1,0]

    def update(self, food_pos):
        self.pos[0] += self.dir[0]*20
        self.pos[1] += self.dir[1]*20
        if self.pos[0] > 600 or self.pos[0] < 0:
            print("DEAD")
            sys.exit()
        if self.pos[1] > 600 or self.pos[1] < 0:
            print("DEAD")
            sys.exit()

        if self.pos == food_pos:
            self.eat()

    def draw_snake(self, window):
        self.snake_body.fill(GREEN)
        window.blit(self.snake_body, self.pos)

    def eat(self):
        self.length += 1
        self.eatt = 1
        return self.eatt
