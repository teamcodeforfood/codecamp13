import pygame
from GameScreen import GameScreen

class MenuScreen(GameScreen):
    def load(self):
        pass

    def draw(self, surface):
        rect = pygame.Rect(0, 0, 1280, 720)
        pygame.draw.rect(surface, (0, 0, 0), rect)

        self.text.drawTextLeft(surface, "Galaxy Jam", (51, 255, 255), 585, 340)
        self.text.drawTextLeft(surface, "press space to begin", (255, 255, 255), 540, 380)

    def update(self, *args):
        if pygame.K_SPACE in args[0]:
            return False