# Core imports
import pygame
import random

# Player and enemy
from spaceship import Spaceship
from baddie import Baddie

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
        self.spaceship_speed = 2
        self.bullets = []
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (255,255,255)
        self.baddies = []
        self.baddie_width = 20
        self.baddie_height = 20
        self.baddie_color = (255,0,0)
        self.score = 0
        self.baddies_killed = 0
        self.current_level = 0
        self.resources_path = "resources"     

        # test_screen = TestScreen()
        # hud_screen = Hud()

        self.screen_manager = ScreenManager()
        self.screen_manager.setOverlayScreen(Hud())
        self.screen_manager.setBackgroundScreen(Background())

        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.screen_manager.bg.update()

        if pygame.K_LEFT in keys:
            self.spaceship.moveLeft(self.spaceship_speed)
        if pygame.K_RIGHT in keys:
            self.spaceship.moveRight(self.spaceship_speed,self.upper_limit)
        if pygame.K_UP in keys:
            self.spaceship.moveUp(self.spaceship_speed)
        if pygame.K_DOWN in keys:
            self.spaceship.moveDown(self.spaceship_speed,self.height)

        if pygame.K_SPACE in newkeys:
            self.bullets.append(self.spaceship.fire(self.bullet_width,self.bullet_height,self.bullet_color))

        if random.randint(1, self.frame_rate) == 1:
            self.addBaddie()

        for bullet in self.bullets:
            bullet.moveBullet()
            bullet.checkBackWall(self.width)
                
        for baddie in self.baddies:
            baddie.tick(0,0,self.height)

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


        live_bullets = []
        live_baddies = []
        for bullet in self.bullets:
            if bullet.alive:
                live_bullets.append(bullet)
        for baddie in self.baddies:
            if baddie.alive:
                live_baddies.append(baddie)
      
        self.bullets = live_bullets
        self.baddies = live_baddies

        # self.screen_manager.current_screen.update()
        self.screen_manager.hud.update(self.score, self.spaceship.ammo)
            
        return

    def addBaddie(self):
        new_baddie = Baddie( self.baddie_width, self.baddie_height, self.width, random.randint(0,(self.height-self.baddie_height)), self.baddie_color )
        self.baddies.append( new_baddie )
                   
        return

    def draw(self,surface):
        self.screen_manager.bg.draw(surface)
        
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill((0,0,0),rect )
        self.spaceship.draw(surface)
        for bullet in self.bullets:
            bullet.draw(surface)
        for baddie in self.baddies:
            baddie.draw(surface)

        # self.screen_manager.current_screen.draw(surface)
        self.screen_manager.hud.draw(surface)

        return
