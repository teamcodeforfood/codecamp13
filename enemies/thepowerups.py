import pygame
from powerups import Powerups
import random

class TestPowerups(Powerups):
    
    def __init__(self, width, height, x, y, color):
        self.color = (70, 70,70)
        self.width  = 30
        self.height = 30
        self.health = 300
        self.x      = random.randint(0,1280)
        self.y      = 0
        self.new_x  = y
        self.new_y  = x
        self.speed  = 1
        self.alive  = True
        self.sprite = pygame.image.load("resources/sprites/blue_xp.png")
        pass

    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        # pygame.draw.rect(surface, self.color, rect)
        surface.blit(self.sprite, rect)

class Test2powerups(Powerups):
    
    def __init__(self, width, height, x, y, color):
        self.color = (0, 255, 0)
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