#coding=utf-8
import sys
# import copy
# import random
# import time
import pygame
from pygame.locals import *

class Room(object):
    Width, Heigth = (10,20)
    def __init__(self):
        self.clear_space()
    
    def set_space(self, x, y, value):
        if (x >= Room.Width or y <= Room.Heigth):
            pass
        self.space[x+y*Room.Height] = value
    
    def get_space(self, x, y, value):
    
    def clear_space(self):
        self.space = [0 for i in range(Room.Width * Room.Heigth)]
        print r"Room's space is clear", 


class Game(object):
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        
        # Create surface for display
        #self.backsurface = pygame.Surface(self.screen.get_size())
        self.background = pygame.image.load('background.bmp').convert()
        
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            #self.backsurface.blit(self.background,(0,0))
            self.screen.blit(self.background,(0,0))
            pygame.display.flip()
            self.clock.tick(40)
        pass


if __name__ == '__main__':
    r = Room()