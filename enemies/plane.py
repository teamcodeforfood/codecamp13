import pygame
from baddie import Baddie
import random

class Plane(Baddie):
    
    def __init__(self):
        self.color = (55, 55, 55)
        self.width  = 20
        self.height = 10
        self.x      = 0
        self.y      = random.randint(0, 720)
        self.new_x  = self.x
        self.new_y  = self.y
        self.speed  = 1
        self.alive  = True
        pass

    def tick(self, back_wall, upper_wall, lower_wall):
        self.new_x = self.x + self.speed
        if self.new_x > 1280:
            self.setAlive(False)
        else:
            self.x = self.new_x
        self.y = self.new_y
        return self.alive