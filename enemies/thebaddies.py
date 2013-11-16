import pygame
from baddie import Baddie
import random

class TestBaddie(Baddie):
    
    def __init__(self, width, height, x, y, color):
        self.color = (255, 0,0)
        self.width  = width
        self.height = height
        self.health = 300
        self.x      = random.randint(0,1280)
        self.y      = 0
        self.new_x  = y
        self.new_y  = x
        self.speed  = .5
        self.alive  = True
<<<<<<< HEAD
        self.damage = 10
        self.sprite_1 = pygame.image.load("resources/sprites/baddie_1.png")
=======
        self.sprite_1 = pygame.image.load("resources/sprites/shipjosh1_2.png")
>>>>>>> dd23559bf13af9e71dfe1967a848542ba7a0a4dd
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
        self.damage = 10
        self.speed  = .6
        self.alive  = True
        self.sprite_1 = pygame.image.load("resources/sprites/shipjosh2_2.png")
        pass