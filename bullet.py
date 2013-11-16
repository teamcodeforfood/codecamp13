import pygame

class Bullet():

    def __init__(self, x, y, direction='normal', type="green"):
        self.width  = 5
        self.height = 10
        self.x      = x
        self.y      = y
        self.speed  = 5
        self.color  = (255, 0, 0)
        self.alive  = True
        self.hit    = False
        self.sprite_1 = pygame.image.load("resources/sprites/lazer_1.png")
        self.sprite_2 = pygame.image.load("resources/sprites/lazer_3.png")
        self.sprite_3 = pygame.image.load("resources/sprites/lazer_4.png")
        self.direction = direction
        self.type = type
        return

    def checkHitBaddie(self,x,y,w,h):
        if self.hitRectangle(x, y, w, h):
            self.setAlive(False)
            self.hit = True
            
    def checkHitPowerups(self,x,y,w,h):
        if self.hitRectangle(x, y, w, h):
            self.setAlive(False)
            self.hit = True

    def checkBackWall(self,back_wall):
        if (self.x + self.width) > back_wall:
            self.setAlive(False)
        return

    def moveBullet(self):
        if self.type == "red":
            self.sprite_1 = self.sprite_3
        elif self.direction != "normal":
            self.sprite_1 = self.sprite_2

        if self.direction == 'up':
            self.y -= self.speed
        if self.direction == 'down':
            self.y += self.speed
        elif self.direction == "l":
            self.y -= self.speed
            self.x -= self.speed / 2
        elif self.direction == "r":
            self.y -= self.speed
            self.x += self.speed / 2
        elif self.direction == "-l":
            self.y += self.speed
            self.x -= self.speed / 2
        elif self.direction == "-r":
            self.y += self.speed
            self.x += self.speed / 2
        elif self.direction == "fl":
            self.x -= self.speed
        elif self.direction == "fr":
            self.x += self.speed
        else:
            self.y -= self.speed
        return

    def setAlive(self,alive):
        self.alive = alive
        return
    
    def getHit(self):
        return self.hit

    def hitRectangle(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)) :
                return True
        return False
    
    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        surface.blit(self.sprite_1, rect)
        return
        
###

class BaddieBullet():

    def __init__(self, x, y):
        self.width  = 16
        self.height = 16
        self.x      = x
        self.y      = y
        self.speed  = 6
        self.color  = (255, 0, 0)
        self.alive  = True
        self.hit    = False
        self.sprite_1 = pygame.image.load("resources/sprites/lazer_2.png")
        return

    def checkBackWall(self,back_wall):
        if (self.x + self.width) > back_wall:
            self.setAlive(False)
        return

    def moveBullet(self):
        self.y += self.speed
        return

    def setAlive(self,alive):
        self.alive = alive
        return
    
    def getHit(self):
        return self.hit

    def hitRectangle(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)) :
                return True
        return False
    
    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        surface.blit(self.sprite_1, rect)
        return