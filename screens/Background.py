import pygame
from GameScreen import GameScreen

class Background(GameScreen):
    def load(self):
        self.bg_images = list()
        self.bg_images.append(pygame.image.load("resources/test_bg.png"))

    def update(self, *args):
        pass

    def draw(self, surface):
        screen.blit(myimage, imagerect)
        pass