import pygame
from baddie import Baddie
import random

class TestBaddie(Baddie):
    
    def __init__(self, width, height, x, y, color):
        self.color = (255, 0,0)
        self.width  = 30
        self.height = 30
        self.health = 300
        self.x      = random.randint(0,1280)
        self.y      = 0
        self.new_x  = x
        self.new_y  = y
        self.speed  = 1
        self.alive  = True
        pass

class Test2Baddie(Baddie):
    
    def __init__(self, width, height, x, y, color):
        self.color = (0, 0, 255)
        self.width  = width
        self.height = height
        self.health = 100
        self.x      = random.randint(0,1280)
        self.y      = 0
        self.new_x  = y
        self.new_y  = x
        self.speed  = 1
        self.alive  = True
        pass