import pygame
from GameScreen import GameScreen

class PauseMenu(GameScreen):
    def load(self):
        pass

    def update(self, *args):
        pass

    def draw(self, surface):
        self.text.drawTextLeft(surface, "Paused", (255, 255, 255), 10, 35)

        if newkeys:
            return True

