import pygame
import random
from bullet import BaddieBullet
from globals import Globals

class Boss():

    def __init__(self, width, height, x, y, color):
        self.width  = 200
        self.height = 200
        self.x      = 640
        self.y      =10
        self.new_x  = x
        self.new_y  = y
        self.speed  = .1
        self.color  = (255, 0, 255)
        self.alive  = True
        self.sprite_1 = pygame.image.load("resources/sprites/roboticus2.png")
        self.boom_1 = pygame.mixer.Sound("resources/sound/boom_1.wav")
        self.lazer_3_snd = pygame.mixer.Sound("resources/sound/lazer_3.wav")
        self.bullets = []
        self.health = 20000
        self.ammo = 100000
        self.damage = 10
        return

    def fire(self):
        if self.alive == True:
            if self.ammo > 0:
                self.ammo -= 1
                if random.randint(1, 100) == 1:
                    if not Globals.mute == True:
                        self.lazer_2_snd.play()
                else:
                    if not Globals.mute == True:
                        self.lazer_3_snd.play()
                self.ammo -= 1
                # self.lazer_1.play()
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

        spaceship_rect = pygame.Rect(Globals.spaceship.x, Globals.spaceship.y,Globals.spaceship.width,Globals.spaceship.height)

        for bullet in self.bullets:
            if bullet == None:
                break
            bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)

            if bullet_rect.colliderect(spaceship_rect):
                bullet.setAlive(False)
                Globals.spaceship.health -= 1
                self.lazer_1_snd.play()

        self.y = self.new_y

        if random.randint(1, 150) ==1:
            self.bullets.append(self.fire())

        self.bullets = live_bullets
        if self.y >= 720:
            self.setAlive(False)

        return self.alive


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
        
