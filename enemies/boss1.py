import pygame
import random
from bullet import BaddieBullet
from globals import Globals
import inspect
import time
from meter import Meter

class Boss():

    def __init__(self, width, height, x, y, color):
        # debuging... :/
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        print 'caller name:', calframe[1][3]

        Globals.is_in_boss_battle = True

        self.width  = 200
        self.height = 200
        self.x      = (1280 / 2) - (width / 2)
        self.y      = 25
        self.new_x  = x
        self.new_y  = y
        self.speed  = 1
        self.color  = (255, 0, 255)
        self.alive  = True
        self.sprite_1 = pygame.image.load("resources/sprites/roboticus2.png")
        self.boom_1 = pygame.mixer.Sound("resources/sound/boom_1.wav")
        self.lazer_3_snd = pygame.mixer.Sound("resources/sound/lazer_3.wav")
        self.lazer_1_snd = pygame.mixer.Sound("resources/sound/lazer_1.wav")
        self.lazer_2_snd = pygame.mixer.Sound("resources/sound/lazer_2.wav")
        self.roar_1 = pygame.mixer.Sound("resources/sound/boss_roar_1.ogg")
        self.bullets = []
        self.health = 20000
        self.ammo = 100000
        self.damage = 10
        self.direction = 1
        self.animate_in = False

        # Health
        self.health_meter = Meter(25, 5, 100, 0, 100, self.x + (self.width / 2), self.y - 10)

        # Globals.goGoBossMode()

        pygame.mixer.music.stop()

        pygame.mixer.music.load("resources/music/boss_battle.ogg")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        return

    def boss_anim(self, surface):
        # do we need this

        self.animate_in = True

    def fire(self, direction):
        # return BaddieBullet(self.x + (self.width / 2), (self.y + (self.height / 2)), "boss")
        if self.alive == True:
            bullet = BaddieBullet(self.x + (self.width / 2), (self.y + (self.height + 5)), "boss")
            bullet.direction = direction
            return bullet
        else:
            return None

    def tick(self,back_wall,upper_wall,lower_wall):
        # self.speed = random.randint(1, 4)

        # self.health_meter.update_pos(self.x + (self.width / 2), self.y - 10)
        self.health_meter.update(self.health / 100)

        if self.direction == 1:
            if self.x <= (1280 - self.width):
                self.x += self.speed
            else:
                self.direction = -1
        elif self.direction == -1:
            if self.x >= 0:
                self.x -= self.speed
            else:
                self.direction = 1

        live_bullets = []

        for bullet in self.bullets:
            if bullet.alive:
                live_bullets.append(bullet)

        if random.randint(1, 500) == 1:
            self.roar_1.play()

        # self.new_x = self.x + random.randint(-1,1)
        # self.new_y = self.y + self.speed
        # if self.new_x < back_wall:
            # self.setAlive(False)

        # self.y = self.new_y

        if random.randint(1, 100) == 1: 
            self.bullets.append(self.fire("down"))
            self.bullets.append(self.fire("l"))
            self.bullets.append(self.fire("r"))
            self.bullets.append(self.fire("-l"))
            self.bullets.append(self.fire("-r"))
            self.bullets.append(self.fire("fl"))
            self.bullets.append(self.fire("fr"))
            self.bullets.append(self.fire("ll"))
            self.bullets.append(self.fire("rr"))
            self.bullets.append(self.fire("-ll"))
            self.bullets.append(self.fire("-rr"))

        for bullet in self.bullets:
            bullet.moveBullet()

        # self.bullets = live_bullets

        spaceship_rect = pygame.Rect(Globals.spaceship.x, Globals.spaceship.y,Globals.spaceship.width,Globals.spaceship.height)

        for bullet in self.bullets:
            if not bullet == None:
                bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)

                if bullet_rect.colliderect(spaceship_rect):
                    bullet.setAlive(False)
                    Globals.spaceship.health -= 1
                    self.lazer_1_snd.play()

        # self.y = self.new_y

        # self.bullets = live_bullets

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

        # self.bullets = live_bullets

        return self.alive

    def getAlive(self):
        return self.alive

    def getDimensions(self):
        return self.x,self.y,self.width,self.height

    def setAlive(self,alive):
        self.alive = alive

        if alive == False:
            pygame.mixer.music.stop()
        
            # i = 0
            # while i <= 10:
            self.boom_1.play()
            

    def draw(self, surface):
        if self.animate_in == False:
            self.boss_anim(surface)
        else:
            rect = pygame.Rect( self.x, self.y, self.width, self.height )
            # pygame.draw.rect(surface, self.color, rect)
            surface.blit(self.sprite_1, rect)

            for bullet in self.bullets:
                bullet.draw(surface)

        self.health_meter.draw(surface)

        return
        
