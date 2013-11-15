# Core imports
import pygame
import random

# Player and enemy
from spaceship import Spaceship
from baddie import Baddie
from powerups import Powerups

# Game managers
from GameScreen import GameScreen
from ScreenManager import ScreenManager
import text

# Screens
from screens.test import TestScreen
from screens.Hud import Hud
from screens.Background import Background

class SpaceshipData:

    def __init__(self,width,height,frame_rate):
        self.font = pygame.font.Font("resources/Fipps-Regular.otf",16)
        self.font2 = pygame.font.SysFont("Courier New",20)
        self.frame_rate = frame_rate
        self.text_color = (255,0,0)
        self.width  = width
        self.height = height
        self.upper_limit = self.width/3
        self.spaceship_width = 10
        self.spaceship_height = 20
        self.spaceship = Spaceship(self.spaceship_width,self.spaceship_height,(self.width / 2), (self.height) -10, (255,255,255))
        self.bullets = []
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (255,0,0)
        self.baddies = []
        self.baddie_width = 20
        self.baddie_height = 20
        self.baddie_color = (255,0,0)
        self.powerups = []
        self.powerups_width = 20
        self.powerups_height = 20
        self.powerups_color = (0,255,0)
        self.score = 0
        self.baddies_killed = 0
        self.current_level = 0
        self.resources_path = "resources"     
        self.speed_boost_time = 0 
        self.speed_boost = False


        # test_screen = TestScreen()
        # hud_screen = Hud()

        self.screen_manager = ScreenManager()
        self.screen_manager.setOverlayScreen(Hud())
        self.screen_manager.setBackgroundScreen(Background())

        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.screen_manager.bg.update()

        if pygame.K_LEFT in keys or pygame.K_a in keys:
            self.spaceship.moveLeft(self.spaceship.spaceship_speed)
        if pygame.K_RIGHT in keys or pygame.K_d in keys:
            self.spaceship.moveRight(self.spaceship.spaceship_speed,self.upper_limit)
        if pygame.K_UP in keys or pygame.K_w in keys:
            self.spaceship.moveUp(self.spaceship.spaceship_speed)
        if pygame.K_DOWN in keys or pygame.K_s in keys:
            self.spaceship.moveDown(self.spaceship.spaceship_speed,self.height)

        if pygame.K_SPACE in newkeys:
            self.bullets.append(self.spaceship.fire(self.bullet_width,self.bullet_height,self.bullet_color))

        if random.randint(1, self.frame_rate) == 1:
            self.addBaddie()+= 1
            self.addPowerups()

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
                    baddie.setAlive(False)
                    bullet.hit = False
                    self.score += 100

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

        for powerups in self.powerups:
            if powerups.alive:
                powerups_rect = pygame.Rect(powerups.x,powerups.y,powerups.width, powerups.height)

                if(powerups_rect.colliderect(spaceship_rect)):
                    powerups.setAlive(False)
                    self.spaceship.spaceship_speed += 6
                    self.speed_boost_time = 0
                    self.speed_boost = True

        if self.speed_boost == True:
            if self.speed_boost_time <= 1200:
                self.speed_boost_time += 1
            else:
                self.speed_boost = False
                self.speed_boost_time = 0
                self.spaceship.spaceship_speed = 5

        self.bullets = live_bullets
        self.baddies = live_baddies
        self.powerups = live_powerups

        # self.screen_manager.current_screen.update()
        self.screen_manager.hud.update(self.score, self.spaceship.ammo, self.spaceship.health)
            
        return

    def addBaddie(self):
        new_baddie = Baddie( self.baddie_width, self.baddie_height, self.width, random.randint(0,(self.height-self.baddie_height)), self.baddie_color )
        self.baddies.append( new_baddie )
                   
        return
    def addPowerups(self):
        new_powerups = Powerups(self.powerups_width, self.powerups_height, self.width, random.randint(0,(self.height-self.powerups_height)), self.powerups_color )
        self.powerups.append( new_powerups )

        return


    def draw(self,surface):
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill((11,96,161),rect )
        self.screen_manager.bg.draw(surface)
        self.spaceship.draw(surface)
        for bullet in self.bullets:
            bullet.draw(surface)
        for baddie in self.baddies:
            baddie.draw(surface)
        for powerups in self.powerups:
            powerups.draw(surface)




        # self.screen_manager.current_screen.draw(surface)
        self.screen_manager.hud.draw(surface)

        return
