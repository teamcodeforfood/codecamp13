import pygame

class Text:
    def __init__(self):
        self.main_font = pygame.font.Font("resources/ABSTRACT.TTF",7)
        self.main_font2 = pygame.font.Font("resources/ABSTRACT.TTF",14)

    def drawTextLeft(self, surface, text, color, x, y):
        textobj = self.main_font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomleft = (x, y)
        surface.blit(textobj, textrect)
        return

    def drawTitleLeft(self, surface, text, color, x, y):
        textobj = self.main_font2.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomleft = (x, y)
        surface.blit(textobj, textrect)
        return

    def drawTextRight(self, surface, text, color, x, y):
        textobj = self.main_font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomright = (x, y)
        surface.blit(textobj, textrect)
        return