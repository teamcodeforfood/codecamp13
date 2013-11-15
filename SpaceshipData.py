# Core imports
import pygame
import random

from GameScreen import GameScreen
from ScreenManager import ScreenManager

# Screens
from screens.Background import Background
from screens.Hud import Hud
from screens.MenuScreen import MenuScreen
from screens.PlayScreen import PlayScreen

class SpaceshipData:

    def __init__(self,width,height,frame_rate):
        self.screen_manager = ScreenManager()
        self.screen_manager.setOverlayScreen(Hud())
        self.screen_manager.setBackgroundScreen(Background())
        self.screen_manager.setCurrentScreen(MenuScreen())
        self.screen_manager.setScreenQueue(PlayScreen())

        self.screen_manager.next.load(frame_rate, width, height)

        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.screen_manager.bg.update()
        
        if self.screen_manager.current_screen.update(keys, newkeys) == False:
            self.screen_manager.current_screen = self.screen_manager.next
        else:
            self.screen_manager.current_screen.update(keys, newkeys)

        if self.screen_manager.display_hud == True:
            self.screen_manager.hud.update(self.score, self.spaceship.ammo, self.spaceship.health)
        
        return

    def draw(self,surface):
        rect = pygame.Rect(0,0,1280, 720)
        surface.fill((0,0,0),rect )
        self.screen_manager.bg.draw(surface)
        
        self.screen_manager.current_screen.draw(surface)
        
        if self.screen_manager.display_hud == True:
            self.screen_manager.hud.draw(surface)

        return
