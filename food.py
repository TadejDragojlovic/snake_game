import pygame, random
from vars import *

class Food():
    def __init__(self):
        self.pos = (random.randint(0, 30)*20, random.randint(0, 30)*20)
        self.width = 20
        self.height = 20

        self.food_body = pygame.Surface((self.width, self.height))
        self.rect = self.food_body.get_rect()
        self.rect.topleft = self.pos

    def draw_food(self, window):
        self.food_body.fill(RED)
        window.blit(self.food_body, self.pos)
