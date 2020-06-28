import pygame, sys
from vars import *

class Snake():
    def __init__(self, x, y):
        self.pos = [x*cell_size, y*cell_size]
        self.width = cell_size
        self.height = cell_size
        self.snake_body = pygame.Surface((self.width, self.height))
        self.rect = self.snake_body.get_rect()
        self.rect.topleft = self.pos
        self.length = 1
        self.body = [self.pos]
        self.eatt = 0
        self.score = 0
        
        self.dir = [1,0]

    def update(self, food_pos):
        self.pos[0] += self.dir[0]*cell_size
        self.pos[1] += self.dir[1]*cell_size
        if self.pos[0] > 599 or self.pos[0] < 0:
            self.die()
        if self.pos[1] > 599 or self.pos[1] < 0:
            self.die()

        if self.pos == food_pos:
            self.eat()

        self.set_body()

        if self.hit_tail():
            sys.exit()

    def draw_snake(self, window):
        for pos in self.body:
            self.snake_body.fill(GREEN)
            window.blit(self.snake_body, pos)

    def eat(self):
        self.length += 1
        self.score += 1
        self.eatt = 1
        return self.eatt

    def set_body(self):
        x, y = self.pos
        self.body.insert(0, [x, y])
        self.body = self.body[:self.length]

    def hit_tail(self):
        if self.length > 1:
            for id, pos in enumerate(self.body):
                if self.pos == pos and id != 0:
                    return True
        return False

    def die(self):
        sys.exit()
