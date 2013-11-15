import pygame
import random

class Gamedata():

	        def __init__(self,width,height,x,y,color):
	            self.width  = 20
	            self.height = 20
	            self.x      = random.randint(0,720)
	            self.y      = 0
	            self.new_x  = y
	            self.new_y  = x
	            self.speed  = 1
	            self.color  = (255,255,0)
	            self.alive  = True
	            self.orig_width = self.width
	            return