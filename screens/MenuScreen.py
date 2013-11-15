import pygame
from GameScreen import GameScreen

class MenuScreen(GameScreen):
    def load(self):
        pass

    def draw(self, surface):
        rect = pygame.Rect(0, 0, 1280, 720)
        pygame.draw.rect(surface, (0, 0, 0), rect)

        self.text.drawTextLeft(surface, "spacegame", (255, 255, 255), 50, 50)
        self.text.drawTextLeft(surface, "press enter to begin", (255, 255, 255), 50, 75)

    def update(self, *args):
        if pygame.K_SPACE in args[0]:
            return False