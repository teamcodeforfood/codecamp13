import pygame
import random
from bullet import Bullet

class Weapons():
    single = 0
    spread = 2
    circle = 4

class Spaceship():

    def __init__(self,width,height,x,y,color):
        pygame.mixer.init()

        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.color  = color
        self.health = 100
        self.missed = 0
        self.powerstat = 0
        # TODO: ammo is really high for testing purposes
        self.ammo   = 200
        self.spaceship_speed = 2.5
        self.alive = True
        self.gamedifficulty = 1
        self.active_weapon = 0
        self.space_ship_img = pygame.image.load("resources/sprites/ship_1.png")
        self.space_ship_img_l = pygame.image.load("resources/sprites/ship_1_l.png")
        self.space_ship_img_r = pygame.image.load("resources/sprites/ship_1_r.png")
        
        # 0 = up
        # 1 = left
        # 2 = right
        self.dir = 0

        # Sound effects
        self.lazer_1 = pygame.mixer.Sound("resources/sound/lazer_1.wav")
        self.lazer_4 = pygame.mixer.Sound("resources/sound/lazer_4.wav")
        self.boom_1 = pygame.mixer.Sound("resources/sound/boom_1.wav")
        self.nope = pygame.mixer.Sound("resources/sound/nope.wav")

        return

    def moveLeft(self, dx):
        self.x -= dx
        # check the wall
        if self.x < 0:
            self.x = 0

        self.dir = 1

        return

    def moveRight(self, dx, upper_limit):
        self.x += dx
        # check the wall
        #if self.x > upper_limit:
         #  self.x = upper_limit

        self.dir = 2

        return

    def moveUp(self, dy):
        self.y -= dy
        # check the wall
        if self.y < 0:
            self.y = 0

        self.dir = 0

        return

    def moveDown(self, dy, board_height):
        self.y += dy
        # check the wall
        if self.y > board_height - self.height:
            self.y = board_height - self.height

        self.dir = 0

        return

    def fire(self, direction='normal', type="green"):
        if self.alive == True:
            if self.ammo > 0:
                self.ammo -= random.randint(0, 1)

                if self.active_weapon == 0:
                    self.lazer_1.play()
                elif self.active_weapon == 4:
                    self.lazer_1.play()
                elif self.active_weapon == 2:
                    self.lazer_4.play()
                return Bullet(self.x + (self.width / 2), (self.y + (self.height / 2)), direction, type)
            else:
                self.nope.play()
                return None

    def draw(self, surface):
        if self.alive == True:
            rect = pygame.Rect( self.x, self.y, self.width, self.height )
            # pygame.draw.rect(surface, self.color, rect)
            if self.dir == 0:
                surface.blit(self.space_ship_img, rect)
            if self.dir == 1:
                surface.blit(self.space_ship_img_l, rect)
            if self.dir == 2:
                surface.blit(self.space_ship_img_r, rect)
        return

    def setAlive(self, alive):
        self.alive = alive

        if alive == False:
            self.boom_1.play()
            
            # Move the corpse away
            self.x = 1000
            self.y = 1000
