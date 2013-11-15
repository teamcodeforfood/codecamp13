from GameScreen import GameScreen

class ScreenManager():
    def __init__():
        self.current_screen = None

    def draw(self, surface):
        self.current_screen.draw(surface)

    def setCurrentScreen(self, screen):
        self.current_screen = screen