import pygame
from GameScreen import GameScreen

class Background(GameScreen):
    def load(self):
        self.img = pygame.image.load("resources/test_bg.png")
        self.imagerect = self.img.get_rect()

    def update(self, *args):
        self.imagerect.y -= 1
        pass

    def draw(self, surface):
        surface.blit(self.img, self.imagerect)
        pass