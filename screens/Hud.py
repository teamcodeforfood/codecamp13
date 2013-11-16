import pygame
from GameScreen import GameScreen
from meter import Meter
from globals import Globals
from spaceship import Weapons

class Hud(GameScreen):
    def load(self):
        self.health_meter = Meter(100, 20, 100, 0, 100, 64, (720 - 64))
        self.ammo_meter = Meter(100, 20, 100, 0, 100, 64, (720 - 90))

        # Hotbar
        self.hotbar_bg = pygame.image.load("resources/sprites/hotbar/HotBar.png")
        self.hotbar_sel = pygame.image.load("resources/sprites/hotbar/SelectionRing.png")
        self.hotbar_cur = 1

        # HUD overlays
        self.health_img = pygame.image.load("resources/overlays/health.png")
        self.ammo_img = pygame.image.load("resources/overlays/ammo.png")

        # Hotbar items
        self.lazer1 = pygame.image.load("resources/sprites/hotbar/lazer_1.png")
        self.lazer2 = pygame.image.load("resources/sprites/hotbar/lazer_2.png")
        self.lazer3 = pygame.image.load("resources/sprites/hotbar/lazer_3.png")

    def update(self, *args):
        self.score = args[0]
        self.ammo = args[1]
        self.health = args[2]
        self.missed = args[3]
        self.gamedifficulty = args[4]
        self.powerstat = args[5]

        self.ammo_meter.update(self.ammo)
        self.health_meter.update(self.health)

    def draw(self, surface):
        self.text.drawTextLeft(surface, "Score:  " + str(self.score), (255, 255, 255), 10, 35)
        # self.text.drawTextLeft(surface, "Ammo    " + str(self.ammo), (255, 255, 255), 10, 55)
        # self.text.drawTextLeft(surface, "Health   " + str(self.health), (255, 255, 255), 10, 75)
        # self.text.drawTextLeft(surface, "Missed   " + str(self.missed), (255, 255, 255), 10, 95)
        # self.text.drawTextLeft(surface, "Difficulty   " + str(self.gamedifficulty), (255, 255, 255), 585, 35)
        # print "Enemies killed: " + str(self.gamedifficulty)

        self.ammo_meter.draw(surface)
        self.health_meter.draw(surface)

        surface.blit(self.health_img, pygame.Rect(45, (720 - 64), 20, 20))
        surface.blit(self.ammo_img, pygame.Rect(45, (720 - 90), 20, 20))

        hw = 160
        hh = 32

        rect = pygame.Rect((1280 - hw) - 32, (720 - hh) - 32, hw, hh)
        surface.blit(self.hotbar_bg, rect)

        # rect_slot_1 = pygame.Rect((1280 - hw) - 32, (720 - hh) - 32, 32, 32)
        # surface.blit(self.hotbar_sel, rect_slot_1)

        # Weapons
        weap_rect = pygame.Rect((1280 - hw) - 32, (720 - hh) - 32, 32, 32)

        surface.blit(self.lazer1, weap_rect)

        weap_rect.x += 32
        surface.blit(self.lazer2, weap_rect)

        weap_rect.x += 32
        surface.blit(self.lazer3, weap_rect)

        ##

        weap_rect = pygame.Rect(((1280 - hw) - 32) + (16 * (Globals.spaceship.active_weapon)), (720 - hh) - 32, 32, 32)
        surface.blit(self.hotbar_sel, weap_rect)

    def lose_screen(self):
        return True