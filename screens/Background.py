import pygame
from GameScreen import GameScreen

class Background(GameScreen):
    def load(self):
        self.bg1 = pygame.image.load("resources/test_bg.png").convert()
        self.bg2 = pygame.image.load("resources/test_bg2.png").convert()

        self.imagerect1 = self.bg1.get_rect()
        self.imagerect1.y = (-self.imagerect1.height)

        self.imagerect2 = self.bg2.get_rect()
        self.imagerect2.y = self.imagerect1.y

    def update(self, *args):
        self.imagerect1.y += 1
        
        if self.imagerect1.y >= 0:
            self.imagerect2.y += 1

        if self.imagerect2.y >= 0:
            self.imagerect1.y = (-self.imagerect1.height)
            self.imagerect2.y = self.imagerect1.y

    def draw(self, surface):
        surface.blit(self.bg1, self.imagerect1)
        surface.blit(self.bg2, self.imagerect2)