from spaceship import Spaceship

class Globals():

    def setup():
        pygame.font.init()
        pygame.display.init()

    bullet_width = 5
    bullet_height = 5

    spaceship_height = 20
    spaceship_width = 10

    baddie_height = 20
    baddie_width = 20

    score = 0
    ammo = 0

    spaceship = Spaceship(10,20,(1280 / 2), (720) -10, (255,255,255))