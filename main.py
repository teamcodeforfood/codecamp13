import pygame
from SpaceshipAdventure import SpaceshipAdventure

def main():
    pygame.init()
    c = SpaceshipAdventure(1280, 720, 120)
    c.main_loop()

    return
    
if __name__ == "__main__":
    main()
