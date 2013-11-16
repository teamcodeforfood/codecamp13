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

    is_in_boss_battle = False

    score = 0
    ammo = 0

    # RIP - Logan's ears
    mute = True

    spaceship = Spaceship(10,20,(1280 / 2), (720) - 42, (255,255,255))

    def goGoBossMode():
        pass