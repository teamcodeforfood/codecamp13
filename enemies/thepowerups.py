import pygame
from powerups import Powerups
import random

class TestPowerups(Powerups):
    
    def __init__(self, width, height, x, y, color):
        self.color = (70, 70,70)
        self.width  = width
        self.height = height
        self.health = 200
        self.x      = random.randint(0,1280)
        self.y      = 0
        self.new_x  = y
        self.new_y  = x
        self.speed  = 2
        self.alive  = True
        self.sprite = pygame.image.load("resources/sprites/blue_xp.png")
        pass

    def tick(self, back_wall, upper_wall, lower_wall):
        self.new_y = self.y + self.speed
        if self.new_x < back_wall:
            self.setAlive(False)
        # if self.new_y < upper_wall:
            # self.new_y = upper_wall
        # elif self.new_y + self.height > lower_wall:
            # self.new_y = lower_wall - self.height
        self.y = self.new_y
        return self.alive
    def getAlive(self):
        return self.alive

    def getDimensions(self):
        return self.x,self.y,self.width,self.height

    def setAlive(self,alive):
        self.alive = alive
    
    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        # pygame.draw.rect(surface, self.color, rect)
        surface.blit(self.sprite, rect)
        return
        