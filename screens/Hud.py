import pygame
from GameScreen import GameScreen

class Hud(GameScreen):
    def load(self):
        pass

    def draw(self, surface):
        # self.drawTextLeft(surface, str(self.score), (255, 255, 255), 10, 50, self.font)
        self.text.drawTextLeft(surface, "Hello", (255, 255, 255), 10, 50)

        pass

