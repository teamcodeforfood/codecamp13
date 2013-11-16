import pygame
import random
from bullet import BaddieBullet

class Boss():

    def __init__(self, width, height, x, y, color):
        self.width  = 100
        self.height = 100
        self.x      = 640
        self.y      = 100
        self.new_x  = x
        self.new_y  = y
        self.speed  = .5
        self.color  = (255, 0, 255)
        self.alive  = True
        self.sprite_1 = pygame.image.load("resources/sprites/redcapsule.png")
        self.boom_1 = pygame.mixer.Sound("resources/sound/boom_1.wav")
        self.bullets = []
        self.health = 1000
        return

    def fire(self):
        if self.alive == True:
            if self.ammo > 0:
                self.ammo -= 1
                return BaddieBullet(self.x + (self.width / 2), (self.y + (self.height / 2)))
            else:
                return None

    def tick(self,back_wall,upper_wall,lower_wall):
        live_bullets = []

        for bullet in self.bullets:
            if bullet.alive:
                live_bullets.append(bullet)


        # self.new_x = self.x + random.randint(-1,1)
        self.new_y = self.y + self.speed
        if self.new_x < back_wall:
            self.setAlive(False)
        # if self.new_y < upper_wall:
            # self.new_y = upper_wall
        # elif self.new_y + self.height > lower_wall:
            # self.new_y = lower_wall - self.height
        self.y = self.new_y

        if random.randint(1, 255) == 1:
            self.bullets.append(self.fire())

        for bullet in self.bullets:
            bullet.moveBullet()

        self.bullets = live_bullets

        return self.alive

    def getAlive(self):
        return self.alive

        if alive == False:
            self.boom_1.play()
            self.boom_1.play()
            self.boom_1.play()

    def getDimensions(self):
        return self.x,self.y,self.width,self.height

    def setAlive(self,alive):
        self.alive = alive
    
    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        # pygame.draw.rect(surface, self.color, rect)
        surface.blit(self.sprite_1, rect)

        for bullet in self.bullets:
            bullet.draw(surface)

        return
        
