from GameScreen import GameScreen

class ScreenManager():
    def __init__(self):
        self.current_screen = None
        self.hud = None
        self.display_hud = False

    def draw(self, surface):
        self.current_screen.draw(surface)

    def setCurrentScreen(self, screen):
        self.current_screen = screen

    def setOverlayScreen(self, hud):
        self.hud = hud
        self.hud.load()

    def setBackgroundScreen(self, screen):
        self.bg = screen
        self.bg.load()

    def setScreenQueue(self, screen):
        self.next = screen

    def gamePause(self):
        self.current_screen = self