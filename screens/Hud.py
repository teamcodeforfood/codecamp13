import pygame
from GameScreen import GameScreen
from meter import Meter

class Hud(GameScreen):
    def load(self):
        self.ammo_meter = Meter(100, 0, 100, 10, 100)

    def update(self, *args):
        self.score = args[0]
        self.ammo = args[1]
        self.health = args[2]
        self.missed = args[3]
        self.gamedifficulty = args[4]
        self.powerstat = args[5]

        self.ammo_meter.update(self.ammo)

    def draw(self, surface):
        self.text.drawTextLeft(surface, "Score    " + str(self.score), (255, 255, 255), 10, 35)
        self.text.drawTextLeft(surface, "Ammo    " + str(self.ammo), (255, 255, 255), 10, 55)
        self.text.drawTextLeft(surface, "Health   " + str(self.health), (255, 255, 255), 10, 75)
        self.text.drawTextLeft(surface, "Missed   " + str(self.missed), (255, 255, 255), 10, 95)
        self.text.drawTextLeft(surface, "Difficulty   " + str(self.gamedifficulty), (255, 255, 255), 585, 35)

        self.ammo_meter.draw(surface)

        self.text.drawTextLeft(surface, "Status   " + str(self.powerstat), (255, 255, 255), 1000, 400)
        self.text.drawTextLeft(surface, "Status   " + str(self.powerstat), (255, 255, 255), 1000, 400)
