import pygame
from GameScreen import GameScreen
import time
import random

class MenuScreen(GameScreen):
    def load(self):
        self.flashing = True
        self.flashcount = 0

    def draw(self, surface):
        rect = pygame.Rect(0, 0, 1280, 720)
        self.text.drawTextLeft(surface, "Galaxy Jam", (253, 212, 0), 550, 340)
        self.text.drawTextLeft(surface, "press space to begin", (255, 255, 255), 475, 380)
        self.text.drawTextLeft(surface, "Will Code for food", (255, 0, 0), 950, 30)
        self.text.drawTextLeft(surface, "Josh Beitler", (255, 255, 255), 1000, 50)
        self.text.drawTextLeft(surface, "Kyler Tolleson", (255, 255, 255), 975, 70)
        self.text.drawTextLeft(surface, "Logan Cox", (255, 255, 255), 1025, 90)
        self.text.drawTextLeft(surface, "Arrow Keys or WASD to move!", (255, 255, 255), 425, 650)
        self.text.drawTextLeft(surface, "Blue powerups increase your speed!", (81, 212, 255), 350, 670)
        self.text.drawTextLeft(surface, "Green powerups give you ammo!", (52, 255, 100), 405, 690)
        self.text.drawTextLeft(surface, "Be careful when you get to difficulty 100!", (255, 255, 255), 308, 710)

    def update(self, *args):
        rect = pygame.Rect(0, 0, 1280, 720)
        if pygame.K_SPACE in args[0]:
            return False
