import pygame
from GameScreen import GameScreen
import time
import random

class MenuScreen(GameScreen):
    def load(self):
        self.flashing = True
        self.flashcount = 0
        self.textbg = pygame.image.load("resources/overlays/mainmenu_o.png")

    def draw(self, surface):
        rect = pygame.Rect(0, 0, 1280, 720)
        # surface.blit(self.textbg, pygame.Rect(0, 0, 1280, 720))
        self.text.drawTitleLeft(surface, "Galaxy Jam", (253, 212, 0), 460, 340)
        self.text.drawTextLeft2(surface, "press space to begin", (100, 100, 255), 460, 400)
        self.text.drawTextLeft2(surface, "Will Code for Food", (255, 0, 0), 460, 100)
        self.text.drawTextLeft2(surface, "Josh Beitler", (255, 255, 255), 460, 120)
        self.text.drawTextLeft2(surface, "Kyler Tolleson", (255, 255, 255), 460, 140)
        self.text.drawTextLeft2(surface, "Logan Cox", (255, 255, 255), 460, 160)
        self.text.drawTextLeft2(surface, "Arrow Keys or WASD to move!", (255, 255, 255), 460, 460)
        self.text.drawTextLeft2(surface, "    Blue powerups increase your speed!", (81, 212, 255), 460, 480)
        self.text.drawTextLeft2(surface, "    Green powerups give you ammo!", (52, 255, 100), 460, 500)
        self.text.drawTextLeft2(surface, "Be careful when you get to difficulty 100!", (255, 255, 255), 460, 520)
        self.text.drawTextLeft2(surface, "Don't hit the asteroids!", (255, 255, 255), 460,540)

    def update(self, *args):
        rect = pygame.Rect(0, 0, 1280, 720)
        if pygame.K_SPACE in args[0]:
            return False

    def lose_screen(self):
        return True
