import pygame
from vars import *

class Snake():
    def __init__(self, x, y, width, height):
        self.pos = (x*20, y*20)
        self.width = width
        self.height = height
        self.snake_body = pygame.Surface((self.width, self.height))
        self.rect = self.snake_body.get_rect()
        self.rect.topleft = self.pos

    def draw_snake(self, window):
        self.snake_body.fill(GREEN)
        window.blit(self.snake_body, self.pos)
