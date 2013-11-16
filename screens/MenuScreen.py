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
        self.text.drawTextLeft(surface, "Galaxy Jam", (51, 255, 255), 550, 340)
        self.text.drawTextLeft(surface, "press space to begin", (255, 255, 255), 475, 380)

    def update(self, *args):
        rect = pygame.Rect(0, 0, 1280, 720)
        if pygame.K_SPACE in args[0]:
            return False
