import pygame
from bullet import Bullet

class Spaceship():

    def __init__(self,width,height,x,y,color):
        pygame.mixer.init()

        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.color  = color
        self.health = 100
        # TODO: ammo is really high for testing purposes
        self.ammo   = 100
        self.spaceship_speed = 2.5
        self.alive = True
        self.missed = 0
        self.space_ship_img = pygame.image.load("resources/sprites/ship_1.png")
        
        # Sound effects
        self.lazer_1 = pygame.mixer.Sound("resources/sound/lazer_1.wav")

        return

    def moveLeft(self, dx):
        self.x -= dx
        # check the wall
        if self.x < 0:
            self.x = 0
        return

    def moveRight(self, dx, upper_limit):
        self.x += dx
        # check the wall
        #if self.x > upper_limit:
         #  self.x = upper_limit
        return

    def moveUp(self, dy):
        self.y -= dy
        # check the wall
        if self.y < 0:
            self.y = 0
        return

    def moveDown(self, dy, board_height):
        self.y += dy
        # check the wall
        if self.y > board_height - self.height:
            self.y = board_height - self.height
        return

    def fire(self):
        if self.alive == True:
            if self.ammo > 0:
                self.ammo -= 1
                self.lazer_1.play()
                return Bullet(self.x + (self.width / 2), (self.y + (self.height / 2)))
            else:
                return None

    def draw(self, surface):
        if self.alive == True:
            rect = pygame.Rect( self.x, self.y, self.width, self.height )
            # pygame.draw.rect(surface, self.color, rect)
            surface.blit(self.space_ship_img, rect)
        return

    def setAlive(self,alive):
        self.alive = alive
