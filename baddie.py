import pygame
import random
import spaceship
from globals import Globals

class Baddie():

    def __init__(self,x,y):
        self.width  = 20
        self.height = 20
        self.x      = random.randint(0,1280)
        self.y      = 0
        self.new_x  = x
        self.new_y  = y
        self.speed  = .3
        self.color  = (255, 255, 255)
        self.alive  = True
        self.sprite_1 = pygame.image.load("resources/sprites/shipjosh1_2.png")
        return

    def tick(self,back_wall,upper_wall,lower_wall):
        # self.new_x = self.x + random.randint(-1,1)
        self.new_y = self.y + self.speed
        if self.new_x < back_wall:
            self.setAlive(False)
        if self.new_y > 720:
            Globals.spaceship.missed += 1
            print Globals.spaceship.missed
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
        surface.blit(self.sprite_1, rect)
        return
        
