from GameScreen import GameScreen

class ScreenManager():
    def __init__(self):
        self.current_screen = None
        self.hud = None

    def draw(self, surface):
        self.current_screen.draw(surface)

    def setCurrentScreen(self, screen):
        self.current_screen = screen

    def setOverlayScreen(self, hud):
        self.hud = hud