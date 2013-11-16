import pygame

class Meter():
    def __init__(self, max, min, value, x, y):
        self.max = max
        self.min = min
        self.value = value
        self.x = x
        self.y = y

    def draw(self, surface):
        rect = pygame.Rect(self.x, self.y, 100, 25 )
        pygame.draw.rect(surface, (0, 0, 0), rect)

        rect_1 = pygame.Rect(self.x + 2, self.y + 2, 198, 23 )
        pygame.draw.rect(surface, (255, 0 ,0), rect_1)

        rect_2 = pygame.Rect(self.x + 1, self.y + 2, self.value , 23 )
        pygame.draw.rect(surface, (0, 255, 0), rect_2)
        pass

    def update(self, new_val):

        self.value = new_val
        if self.value > 198:
            self.value = 198
        pass