from spaceship import Spaceship

class Globals():

    def setup():
        pygame.font.init()
        pygame.display.init()

    bullet_width = 5
    bullet_height = 5

    spaceship_height = 32
    spaceship_width = 32

    baddie_height = 32
    baddie_width = 32

    score = 0
    ammo = 0

    spaceship = Spaceship(10,20,(1280 / 2), (720) -10, (255,255,255))