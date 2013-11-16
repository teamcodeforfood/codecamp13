# Player and enemy
from spaceship import Spaceship
from baddie import Baddie
from powerups import Powerups

# Game managers
import text
from globals import Globals

# Baddies
from enemies.test import *
from enemies.thebaddies import *
from enemies.plane import *
from enemies.boss1 import *

# Powerups
from enemies.thepowerups import *

import pygame
from GameScreen import GameScreen

class PlayScreen(GameScreen):
    def load(self, *args):
        # pygame.mixer.init()

        print args
        self.frame_rate = 120
        self.text_color = (255,0,0)
        self.width  = args[1]
        self.height = args[2]
        self.upper_limit = 1260
        self.bullets = []
        self.baddies = []
        self.thebaddies =[]
        self.baddie_width = 32
        self.baddie_height = 32
        self.baddie_color = (255,0,0)
        self.bosses = []
        self.boss_width = 100
        self.boss_height = 100
        self.boss_color = (255, 0, 255)
        self.powerups = []
        self.thepowerups = []
        self.powerups_width = 16
        self.powerups_height = 16
        self.powerups_color = (0,255,0)
        self.score = 0
        self.baddies_killed = 0
        self.current_level = 0
        self.resources_path = "resources"     
        self.speed_boost_time = 0 
        self.speed_boost = False
        self.gamedifficulty = 1

        # Sound effects
        self.hit_1 = pygame.mixer.Sound("resources/sound/hit_1.wav")
        self.powerup_1 = pygame.mixer.Sound("resources/sound/powerup_1.wav")
        self.hurt_1 = pygame.mixer.Sound("resources/sound/hurt_1.wav")

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

        if pygame.K_p in newkeys:
            return False

        if pygame.K_SPACE in newkeys:
            self.bullets.append(Globals.spaceship.fire())

        if pygame.K_r in newkeys:
            self.bullets.append(Globals.spaceship.fire())
            self.bullets.append(Globals.spaceship.fire('l'))
            self.bullets.append(Globals.spaceship.fire('r'))

        #
        # Spawning
        #
        # Add baddies
        if self.gamedifficulty == 10:
            self.addBoss()
        if random.randint(1, 250 - self.gamedifficulty) == 1:
            self.addBaddie()

        if random.randint(1, 250 - self.gamedifficulty) == 1:
            self.addBaddie2()

        if random.randint(1, self.frame_rate*3) == 1:
            self.addTestPowerups()

        if random.randint(1, self.frame_rate*4) == 1:
            self.addPowerups()

        if random.randint(1, 500) == 1:
            self.addPlane()

        # Update bullet
        for bullet in self.bullets:
            if bullet is not None:
                bullet.moveBullet()
                bullet.checkBackWall(self.width)
        if not Globals.spaceship.alive:
            Globals.spaceship.spaceship_speed = 0
                
        for baddie in self.baddies:
            baddie.tick(0,0,self.height)

        for baddie in self.thebaddies:
            baddie.tick(0,0,self.height)

        for powerups in self.powerups:
            powerups.tick(0,0,self.height)

        for powerups in self.thepowerups:
            powerups.tick(0,0,self.height)

        for bullet in self.bullets:
            if bullet == None:
                break

            if not bullet.alive:
                continue
            else:
                for boss in self.bosses:
                            if not boss.alive:
                                continue
                            x,y,w,h = boss.getDimensions()
                            bullet.checkHitBaddie(x,y,w,h)
                            if bullet.getHit():
                                bullet.setAlive(False)
                                boss.health -=100
                                bullet.hit = False
                                self.hit_1.play()
                                if boss.health <= 0:
                                    boss.setAlive(False)
                            if bullet.y < 0:
                                bullet.setAlive(False)
                for baddie in self.baddies:
                    if not baddie.alive:
                        continue
                    x,y,w,h = baddie.getDimensions()
                    bullet.checkHitBaddie(x,y,w,h)
                    if bullet.getHit():
                        bullet.setAlive(False)
                        baddie.health -=100
                        bullet.hit = False
                        Globals.score += 100
                        self.gamedifficulty +=1
                        Globals.spaceship.gamedifficulty +=1
                        self.hit_1.play()
                        if baddie.health <= 0:
                            baddie.setAlive(False)
                    if bullet.y < 0:
                        bullet.setAlive(False)

        for bullet in self.bullets:
            if bullet == None:
                break

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
        live_thepowerups = []
        for bullet in self.bullets:
            if bullet == None:
                break

            if bullet.alive:
                live_bullets.append(bullet)
        for baddie in self.baddies:
            if baddie.alive:
                live_baddies.append(baddie)

        for powerups in self.powerups:
            if powerups.alive:
                live_powerups.append(powerups)

        for powerups in self.thepowerups:
            if powerups.alive:
                live_thepowerups.append(powerups)
      
        spaceship_rect = pygame.Rect(Globals.spaceship.x, Globals.spaceship.y,Globals.spaceship.width,Globals.spaceship.height)

        # Check baddies
        for baddie in self.baddies:
            if baddie.alive:
                baddie_rect = pygame.Rect(baddie.x, baddie.y, baddie.width, baddie.height)

                if(baddie_rect.colliderect(spaceship_rect)):
                    Globals.spaceship.health -= baddie.damage
                    self.hurt_1.play()
                    baddie.setAlive(False)
                    if(Globals.spaceship.health<=0):
                        Globals.spaceship.setAlive(False)
                        print "Spaceship dead"
                    if(baddie.health <= 10):
                        self.spaceship.setAlive(False)

        for boss in self.bosses:
            if boss.alive:
                boss_rect = pygame.Rect(boss.x, boss.y, boss.width, boss.height)

                if(boss_rect.colliderect(spaceship_rect)):
                    Globals.spaceship.health -= boss.damage
                    self.hurt_1.play()
                    boss.setAlive(False)
                    if(Globals.spaceship.health<=0):
                        Globals.spaceship.setAlive(False)
                        print "Spaceship dead"
                    if(boss.health <= 10):
                        self.spaceship.setAlive(False)

        for baddie in self.thebaddies:
            if baddie.alive:
                baddie_rect = pygame.Rect(baddie.x, baddie.y, baddie.width, baddie.height)

                if(baddie_rect.colliderect(spaceship_rect)):
                    Globals.spaceship.health -=10
                    baddie.setAlive(False)
                    if(Globals.spaceship.health<=0):
                        Globals.spaceship.setAlive(False)
                        print "Spaceship dead"

        for powerups in self.thepowerups:
            if powerups.alive:
                TestPowerups_rect = pygame.Rect(powerups.x,powerups.y,powerups.width, powerups.height)

                if(TestPowerups_rect.colliderect(spaceship_rect)):
                    powerups.setAlive(False)
                    Globals.spaceship.spaceship_speed += .5
                    self.speed_boost_time = 0
                    self.speed_boost = True

                    self.powerup_1.play()

                    # For debugging purposes
                    print "Powerup activated"
 # HAHAHAHAH

        for powerups in self.powerups:
            if powerups.alive:
                powerups_rect = pygame.Rect(powerups.x,powerups.y,powerups.width, powerups.height)

                if(powerups_rect.colliderect(spaceship_rect)):
                    powerups.setAlive(False)
                    Globals.spaceship.ammo += 100

                    self.powerup_1.play()

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
        self.thepowerups = live_thepowerups


    def draw(self, surface):
        Globals.spaceship.draw(surface)
        for boss in self.bosses:
            boss.draw(surface)
        for bullet in self.bullets:
            bullet.draw(surface)
        for baddie in self.baddies:
            baddie.draw(surface)
        for baddie in self.thebaddies:
            baddie.draw(surface)
        for powerups in self.powerups:
            powerups.draw(surface)
        for powerups in self.thepowerups:
            powerups.draw(surface)

    def addBoss(self):
        new_boss = Boss( self.boss_width, self.boss_height, self.width, random.randint(0,(self.height-self.boss_height)), self.boss_color )
        self.bosses.append( new_boss )
                   
        return
    
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
        self.thepowerups.append( new_powerups )    

        return

    def addPlane(self):
        new_plane = Plane()
        self.baddies.append(new_plane)
