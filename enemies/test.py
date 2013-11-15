import pygame
from baddie import Baddie
import random

class TestBaddie(Baddie):
    
    def __init__(self, width, height, x, y, color):
        self.color = (55, 55, 55)
        self.width  = 20
        self.height = 20
        self.x      = random.randint(0,1280)
        self.y      = 0
        self.new_x  = y
        self.new_y  = x
        self.speed  = 1
        self.alive  = True
        pass