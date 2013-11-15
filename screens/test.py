import pygame
from GameScreen import GameScreen

class TestScreen(GameScreen):
    def load(self):
        pass

    def draw(self, surface):
        rect = pygame.Rect(0, 0, 1280, 720)
        pygame.draw.rect(surface, (200, 200, 200), rect)