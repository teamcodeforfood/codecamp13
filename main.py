import pygame
from SpaceshipAdventure import SpaceshipAdventure
import sys
from globals import Globals

def main():
    pygame.init()

    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)

    if sys.argv[1] == "sound_off":
        Globals.mute = True

    c = SpaceshipAdventure(1280, 720, 120)
    c.main_loop()

    return
# pygame.

if __name__ == "__main__":
    main()
