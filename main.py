import pygame
from SpaceshipAdventure import SpaceshipAdventure
import sys
from globals import Globals

def main():
    pygame.init()

    c = SpaceshipAdventure(1280, 720, 120)
    c.main_loop()

    return
# pygame.

if __name__ == "__main__":
    main()
