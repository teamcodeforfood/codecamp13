import pygame
from GameScreen import GameScreen

class LoseScreen(GameScreen):
    def load(self):
        pass

    def draw(self, surface):
        rect = pygame.Rect(0, 0, 1280, 720)
        pygame.draw.rect(surface, (200, 200, 200), rect)

    def lose_screen(self):
        return True