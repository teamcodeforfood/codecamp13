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

        rect_1 = pygame.Rect(self.x, self.y, self.wwidth, self.height)
        pygame.draw.rect(surface, (255, 0 ,0), rect_1)

        if self.value <= 0:
            self.value = 0
            
        rect_2 = pygame.Rect(self.x, self.y, self.value , self.height )
        pygame.draw.rect(surface, (0, 255, 0), rect_2)
        pass

    def update(self, new_val):
        if new_val <= 0:
            self.value = 0
            
        self.value = new_val
        if self.value > 100:
            self.value = 100
        pass

    def update_pos(self, x, y):
        self.x = x
        self.y = y