import pygame

class Meter():
    def __init__(self, width, height, max, min, value, x, y):
        self.max = max
        self.min = min
        self.value = value
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.wwidth = self.value

    def draw(self, surface):
        rect = pygame.Rect(self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, (0, 0, 0), rect)

        rect_1 = pygame.Rect(self.x + 2, self.y + 2, self.wwidth, self.height -2)
        pygame.draw.rect(surface, (255, 0 ,0), rect_1)

        rect_2 = pygame.Rect(self.x + 1, self.y + 2, self.value , self.height - 2 )
        pygame.draw.rect(surface, (0, 255, 0), rect_2)
        pass

    def update(self, new_val):
        self.value = new_val
        if self.value > 198:
            self.value = 198
        pass

    def update_pos(self, x, y):
        self.x = x
        self.y = y