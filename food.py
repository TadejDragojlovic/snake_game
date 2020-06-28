import pygame, random
from vars import *

class Food():
    def __init__(self, snake_x, snake_y):
        # Make so the food never spawns on the player
        self.pos = (random.choice([x*20 for x in range(30)if x!=snake_x]), random.choice([y*20 for y in range(30)if y!=snake_y]))

        self.width = 20
        self.height = 20

        self.food_body = pygame.Surface((self.width, self.height))
        self.rect = self.food_body.get_rect()
        self.rect.topleft = self.pos

    def draw_food(self, window):
        self.food_body.fill(RED)
        window.blit(self.food_body, self.pos)
