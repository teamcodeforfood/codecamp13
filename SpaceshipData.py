# Core imports
import pygame
import random

from GameScreen import GameScreen
from ScreenManager import ScreenManager

from globals import Globals

# Screens
from screens.Background import Background
from screens.Hud import Hud
from screens.MenuScreen import MenuScreen
from screens.PlayScreen import PlayScreen

class SpaceshipData:

    def __init__(self,width,height,frame_rate):
        self.screen_manager = ScreenManager()
        self.screen_manager.setOverlayScreen(Hud())
        self.screen_manager.setBackgroundScreen(Background())
        self.screen_manager.setCurrentScreen(MenuScreen())
        self.screen_manager.setScreenQueue(PlayScreen())

        self.screen_manager.next.load(frame_rate, width, height)

        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.screen_manager.bg.update()
<<<<<<< HEAD

        if pygame.K_LEFT in keys or pygame.K_a in keys:
            self.spaceship.moveLeft(self.spaceship.spaceship_speed)
        if pygame.K_RIGHT in keys or pygame.K_d in keys:
            self.spaceship.moveRight(self.spaceship.spaceship_speed,self.upper_limit)
        if pygame.K_UP in keys or pygame.K_w in keys:
            self.spaceship.moveUp(self.spaceship.spaceship_speed)
        if pygame.K_DOWN in keys or pygame.K_s in keys:
            self.spaceship.moveDown(self.spaceship.spaceship_speed,self.height)

        if pygame.K_SPACE in newkeys:
            self.bullets.append(self.spaceship.fire())

         

        # Add baddies
        if random.randint(1, (self.frame_rate)) == 1:
            self.addBaddie()

        if random.randint(1, (self.frame_rate)) == 1:
            self.addBaddie2()

        if random.randint(1, self.frame_rate) == 1:
            self.addTestPowerups()

        if random.randint(1, self.frame_rate) == 1:
            self.addPowerups()

        if random.randint(1, self.frame_rate * 2) == 1:
            self.addPlane()

        for bullet in self.bullets:
            bullet.moveBullet()
            bullet.checkBackWall(self.width)
        if not self.spaceship.alive:
            self.spaceship.spaceship_speed = 0
                
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
      
        spaceship_rect = pygame.Rect(self.spaceship.x, self.spaceship.y,self.spaceship.width,self.spaceship.height)

        for baddie in self.baddies:
            if baddie.alive:
                baddie_rect = pygame.Rect(baddie.x, baddie.y, baddie.width, baddie.height)

                if(baddie_rect.colliderect(spaceship_rect)):
                    self.spaceship.health -=10
                    baddie.setAlive(False)
                    if(self.spaceship.health<=0):
                        self.spaceship.setAlive(False)
                        print "Spaceship dead"

        for powerups in self.powerups:
            if powerups.alive:
                Powerups_rect = pygame.Rect(powerups.x,powerups.y,powerups.width, powerups.height)
                TestPowerups_rect = pygame.Rect(powerups.x,powerups.y,powerups.width, powerups.height)

                if(TestPowerups_rect.colliderect(spaceship_rect)):
                    powerups.setAlive(False)
                    self.spaceship.spaceship_speed += 2
                    self.speed_boost_time = 0
                    self.speed_boost = True
                if(Powerups_rect.colliderect(spaceship_rect)):
                    powerups.setAlive(False)
                    self.spaceship.spaceship_speed += 2
                    self.speed_boost_time = 0
                    self.speed_boost = True

                    # For debugging purposes
                    print "Powerup activated"

        if self.speed_boost == True:
            if self.speed_boost_time <= 1200:
                self.speed_boost_time += 1
            else:
                self.speed_boost = False
                self.speed_boost_time = 0
                self.spaceship.spaceship_speed = 5

                # For debugging purposes
                print "Speed boost ended"

        self.bullets = live_bullets
        self.baddies = live_baddies
        self.powerups = live_powerups

        # self.screen_manager.current_screen.update()
        self.screen_manager.hud.update(self.score, self.spaceship.ammo, self.spaceship.health)
            
        return

    def addBaddie(self):
        new_baddie = TestBaddie( self.baddie_width, self.baddie_height, self.width, random.randint(0,(self.height-self.baddie_height)), self.baddie_color )
        self.baddies.append( new_baddie )
                   
        return
    def addBaddie2(self):
        new_baddie = Test2Baddie( self.baddie_width, self.baddie_height, self.width, random.randint(0,(self.height-self.baddie_height)), self.baddie_color )
        self.baddies.append( new_baddie )
                   
        return
=======
>>>>>>> 1b443d05ff189f84cf018af54efa570a70658207
        
        if self.screen_manager.current_screen.update(keys, newkeys) == False:
            self.screen_manager.current_screen = self.screen_manager.next

            # this is kind of hacky
            self.screen_manager.display_hud = True
        else:
            self.screen_manager.current_screen.update(keys, newkeys)

        if self.screen_manager.display_hud == True:
            self.screen_manager.hud.update(Globals.score, Globals.spaceship.ammo, Globals.spaceship.health)
        
        return

    def draw(self,surface):
        rect = pygame.Rect(0,0,1280, 720)
        surface.fill((0,0,0),rect )
        self.screen_manager.bg.draw(surface)
        
        self.screen_manager.current_screen.draw(surface)
        
        if self.screen_manager.display_hud == True:
            self.screen_manager.hud.draw(surface)

        return
