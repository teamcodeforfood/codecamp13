import pygame
from baddie import Baddie
import random
import decimal

class Plane(Baddie):
    
    def __init__(self):
        self.color = (55, 55, 55)
        self.width  = 32
        self.height = 32
        self.health = 800
        self.x      = 0
        self.y      = random.randint(0, 700)
        self.new_x  = self.x
        self.new_y  = self.y
        self.speed  = .4
        self.damage = 100000
        self.alive  = True
        self.sprite_1 = pygame.image.load("resources/sprites/asteroid_1.png")
        pass

    def tick(self, back_wall, upper_wall, lower_wall):
        self.new_x = self.x + self.speed
        if self.new_x > 1280:
            self.setAlive(False)
        else:
            self.x = self.new_x
        self.y = self.new_y
        return self.alive

    def draw(self, surface):
        rect = pygame.Rect(self.x, self.y, self.width, self.height )
        surface.blit(self.sprite_1, rect)