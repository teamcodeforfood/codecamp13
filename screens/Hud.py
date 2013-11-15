import pygame
from GameScreen import GameScreen

class Hud(GameScreen):
    def load(self):
        pass

    def update(self, *args):
        self.game_score = args[0]
        pass

    def draw(self, surface):
        self.text.drawTextLeft(surface, str(self.game_score), (255, 255, 255), 10, 50)
        # self.text.drawTextLeft(surface, "Hello", (255, 255, 255), 10, 50)

        pass

