import pygame
from SpaceshipAdventure import SpaceshipAdventure

def main():
    pygame.font.init()
<<<<<<< HEAD
<<<<<<< HEAD
    c = SpaceshipAdventure(400, 600, 30)
=======
    pygame.mixer.init()
    c = SpaceshipAdventure(1920, 1080, 30)
>>>>>>> f90f968527bfffd5765f2939658ade6802db1ee9
=======
    pygame.mixer.init()
    c = SpaceshipAdventure(1920, 1080, 120)
>>>>>>> a45098ffef0858c57a7db865293725b9313c8b7e
    c.main_loop()
    return
    
if __name__ == "__main__":
    main()
