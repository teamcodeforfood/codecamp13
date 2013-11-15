import pygame
import random

class Baddie():

    def __init__(self,width,height,x,y,color):
        self.width  = width
        self.height = height
        self.x      = random.randint(0,720)
        self.y      = 0
        self.new_x  = y
        self.new_y  = x
        self.speed  = .7
        self.color  = color
        self.alive  = True
        return

    def tick(self,back_wall,upper_wall,lower_wall):
        # self.new_x = self.x + random.randint(-1,1)
        self.new_y = self.y + self.speed
        if self.new_x < back_wall:
            self.setAlive(False)
        else:
            self.x = self.new_x
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
        pygame.draw.rect(surface, self.color, rect)
        return
        
