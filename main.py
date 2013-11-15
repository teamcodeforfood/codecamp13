import pygame
from SpaceshipAdventure import SpaceshipAdventure

def main():
    pygame.font.init()
    pygame.mixer.init()
    c = SpaceshipAdventure(1920, 1080, 30)
    c.main_loop()
    return
    
if __name__ == "__main__":
    main()

