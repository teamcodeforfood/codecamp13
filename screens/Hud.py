import pygame
from GameScreen import GameScreen

class Hud(GameScreen):
    def load(self):
        pass

    def update(self, *args):
        self.game_score = args[0]
        self.ammo = args[1]
        self.health = args[2]
        pass

    def draw(self, surface):
        self.text.drawTextLeft(surface, "Score    " + str(self.game_score), (255, 255, 255), 10, 35)
        self.text.drawTextLeft(surface, "Ammo    " + str(self.ammo), (255, 255, 255), 10, 55)
        self.text.drawTextLeft(surface, "Health   " + str(self.health), (255, 255, 255), 10, 75)

        pass

