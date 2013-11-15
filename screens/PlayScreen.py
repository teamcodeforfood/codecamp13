# Player and enemy
from spaceship import Spaceship
from baddie import Baddie
from powerups import Powerups

# Game managers
import text
from globals import Globals

# Baddies
from enemies.test import *
from enemies.plane import *

# Powerups
from enemies.thepowerups import *

import pygame
from GameScreen import GameScreen

class PlayScreen(GameScreen):
    def load(self, *args):
        print args
        self.frame_rate = 120
        self.text_color = (255,0,0)
        self.width  = args[1]
        self.height = args[2]
        self.upper_limit = 1260
        self.bullets = []
        self.baddies = []
        self.baddie_width = 20
        self.baddie_height = 20
        self.baddie_color = (255,0,0)
        self.powerups = []
        self.thepowerups = []
        self.powerups_width = 20
        self.powerups_height = 20
        self.powerups_color = (0,255,0)
        self.score = 0
        self.baddies_killed = 0
        self.current_level = 0
        self.resources_path = "resources"     
        self.speed_boost_time = 0 
        self.speed_boost = False
        self.gamedifficulty = 1

    def update(self, *args):
        keys = args[0]
        newkeys = args[1]

        if pygame.K_LEFT in keys or pygame.K_a in keys:
            Globals.spaceship.moveLeft(Globals.spaceship.spaceship_speed)
        if pygame.K_RIGHT in keys or pygame.K_d in keys:
            Globals.spaceship.moveRight(Globals.spaceship.spaceship_speed,self.upper_limit)
        if pygame.K_UP in keys or pygame.K_w in keys:
            Globals.spaceship.moveUp(Globals.spaceship.spaceship_speed)
        if pygame.K_DOWN in keys or pygame.K_s in keys:
            Globals.spaceship.moveDown(Globals.spaceship.spaceship_speed,self.height)

        if pygame.K_SPACE in newkeys:
            self.bullets.append(Globals.spaceship.fire())

        # Add baddies
        if random.randint(1, (self.frame_rate)) == 1:
            self.addBaddie()

        if random.randint(1, (self.frame_rate)) == 1:
            self.addBaddie2()

        if random.randint(1, self.frame_rate*2) == 1:
            self.addTestPowerups()

        if random.randint(1, self.frame_rate*2) == 1:
            self.addPowerups()

        if random.randint(1, self.frame_rate) == 1:
            self.addPlane()

        for bullet in self.bullets:
            bullet.moveBullet()
            bullet.checkBackWall(self.width)
        if not Globals.spaceship.alive:
            Globals.spaceship.spaceship_speed = 0
                
        for baddie in self.baddies:
            baddie.tick(0,0,self.height)

        for powerups in self.powerups:
            powerups.tick(0,0,self.height)

        for bullet in self.bullets:
            if not bullet.alive:
                continue
            for baddie in self.baddies:
                if not baddie.alive:
                    continue
                x,y,w,h = baddie.getDimensions()
                bullet.checkHitBaddie(x,y,w,h)
                if bullet.getHit():
                    bullet.setAlive(False)
                    baddie.health -=100
                    bullet.hit = False
                    self.score += 100
                    self.gamedifficulty +=1
                    if baddie.health <= 0:
                        baddie.setAlive(False)


        for bullet in self.bullets:
            if not bullet.alive:
                continue
            for powerups in self.powerups:
                if not powerups.alive:
                    continue
                x,y,w,h = powerups.getDimensions()
                bullet.checkHitPowerups(x,y,w,h)
                if bullet.getHit():
                    bullet.setAlive(False)
                    powerups.setAlive(False)
                    bullet.hit = False
                    self.score += 100

        live_bullets = []
        live_baddies = []
        live_powerups = []
        for bullet in self.bullets:
            if bullet.alive:
                live_bullets.append(bullet)
        for baddie in self.baddies:
            if baddie.alive:
                live_baddies.append(baddie)

        for powerups in self.powerups:
            if powerups.alive:
                live_powerups.append(powerups)

        spaceship_rect = pygame.Rect(Globals.spaceship.x, Globals.spaceship.y,Globals.spaceship.width,Globals.spaceship.height)

        for baddie in self.baddies:
            if baddie.alive:
                baddie_rect = pygame.Rect(baddie.x, baddie.y, baddie.width, baddie.height)

                if(baddie_rect.colliderect(spaceship_rect)):
                    Globals.spaceship.health -=10
                    baddie.setAlive(False)
                    if(Globals.spaceship.health<=0):
                        Globals.spaceship.setAlive(False)
                        print "Spaceship dead"

        for powerups in self.powerups:
            if powerups.alive:
                Powerups_rect = pygame.Rect(powerups.x,powerups.y,powerups.width, powerups.height)
                if(Powerups_rect.colliderect(spaceship_rect)):
                    powerups.setAlive(False)
                    Globals.spaceship.spaceship_speed += .5
                    self.speed_boost_time = 0
                    self.speed_boost = True

                    # For debugging purposes
                    print "Powerup activated"


        for powerups in self.thepowerups:
            if TestPowerups.alive:
                TestPowerups_rect = pygame.Rect(TestPowerups.x,TestPowerups.y,pTestPowerups.width, TestPowerups.height)

                if(TestPowerups_rect.colliderect(spaceship_rect)):
                    Testpowerups.setAlive(False)
                    Globals.spaceship.spaceship_speed += .5
                    self.speed_boost_time = 0
                    self.speed_boost = True
                    # For debugging purposes
                    print "Powerup 2 activated"





        if self.speed_boost == True:
            if self.speed_boost_time <= 1200:
                self.speed_boost_time += 1
            else:
                self.speed_boost = False
                self.speed_boost_time = 0
                Globals.spaceship.spaceship_speed = 5

                # For debugging purposes
                print "Speed boost ended"

        self.bullets = live_bullets
        self.baddies = live_baddies
        self.powerups = live_powerups


    def draw(self, surface):
        Globals.spaceship.draw(surface)
        for bullet in self.bullets:
            bullet.draw(surface)
        for baddie in self.baddies:
            baddie.draw(surface)
        for powerups in self.powerups:
            powerups.draw(surface)
    
    def addBaddie(self):
        new_baddie = TestBaddie( self.baddie_width, self.baddie_height, self.width, random.randint(0,(self.height-self.baddie_height)), self.baddie_color )
        self.baddies.append( new_baddie )
                   
        return
    def addBaddie2(self):
        new_baddie = Test2Baddie( self.baddie_width, self.baddie_height, self.width, random.randint(0,(self.height-self.baddie_height)), self.baddie_color )
        self.baddies.append( new_baddie )
                   
        return
        

    def addPowerups(self):
        new_powerups = Powerups(self.powerups_width, self.powerups_height, self.width, random.randint(0,(self.height-self.powerups_height)), self.powerups_color )
        self.powerups.append( new_powerups )

        return
    def addTestPowerups(self):
        new_powerups = TestPowerups(self.powerups_width, self.powerups_height, self.width, random.randint(0,(self.height-self.powerups_height)), self.powerups_color )
        self.powerups.append( new_powerups )

        return

    def addPlane(self):
        new_plane = Plane()
        self.baddies.append(new_plane)
