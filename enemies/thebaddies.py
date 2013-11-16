import pygame
from baddie import Baddie
from bullet import BaddieBullet
from globals import Globals
import random

# Triangle one
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
        self.damage = 10
        self.ammo = 100000
        self.sprite_1 = pygame.image.load("resources/sprites/shipjosh1_2.png")
        self.lazer_1 = pygame.image.load("resources/sprites/lazer_2.png")
        self.lazer_1_snd = pygame.mixer.Sound("resources/sound/hurt_1.wav")
        self.lazer_2_snd = pygame.mixer.Sound("resources/sound/lazer_2.wav")
        self.lazer_3_snd = pygame.mixer.Sound("resources/sound/lazer_3.wav")
        self.bullets = []
        self.dir = 1

        pass

    def fire(self):
        if self.alive == True:
            if self.ammo > 0:
                if random.randint(1, 100) == 1:
                    self.lazer_2_snd.play()
                else:
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

        spaceship_rect = pygame.Rect(Globals.spaceship.x, Globals.spaceship.y,Globals.spaceship.width,Globals.spaceship.height)

        for bullet in self.bullets:
            bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)

            if bullet_rect.colliderect(spaceship_rect):
                bullet.setAlive(False)
                Globals.spaceship.health -= 1
                self.lazer_1_snd.play()

        self.y = self.new_y
<<<<<<< HEAD
        
        if random.randint(1, 150) == 1:
=======

        if self.y >= 720:
            Globals.spaceship.missed += 1
            print Globals.spaceship.missed
            self.setAlive(False)

        if random.randint(1, 100) == 1:
>>>>>>> caef6c1c4a27cf3ccac487b332a8fd96e7de43d9
            self.bullets.append(self.fire())

        for bullet in self.bullets:
            bullet.moveBullet()

        # self.bullets = live_bullets

        if self.y >= 720:
            self.setAlive(False)

        return self.alive

    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        # pygame.draw.rect(surface, self.color, rect)
        surface.blit(self.sprite_1, rect)

        for bullet in self.bullets:
            bullet.draw(surface)

        return

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
        self.ammo = 100000
        self.sprite_1 = pygame.image.load("resources/sprites/shipjosh2_2.png")
        self.lazer_1 = pygame.image.load("resources/sprites/lazer_2.png")
        self.bullets = []
        pass

    def fire(self):
        if self.alive == True:
            if self.ammo > 0:
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

        if self.y >= 720:
            Globals.spaceship.missed += 1
            print Globals.spaceship.missed
            self.setAlive(False)

        if random.randint(1, 100) == 1:
            self.bullets.append(self.fire())

        for bullet in self.bullets:
            bullet.moveBullet()

        self.bullets = live_bullets

        return self.alive

    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        # pygame.draw.rect(surface, self.color, rect)
        surface.blit(self.sprite_1, rect)

        for bullet in self.bullets:
            bullet.draw(surface)

        return