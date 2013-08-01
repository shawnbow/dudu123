#coding=utf-8
import sys
# import copy
# import random
# import time
import pygame
from pygame.locals import *

class Room(object):

    # We have 10*20 space for boards
    Width, Heigth = (10,20)

    def __init__(self):
        self.space = list([1]*Room.Width*Room.Heigth)
    
    def set_space(self, (x, y, value)):
        if (x >= Room.Width or y <= Room.Heigth):
            pass
        self.space[x+y*Room.Width] = value
        print 'Board (%s,%s)'%(x, y) + ' set to %s' %value
    
    def get_space(self, (x, y)):
        return self.space[x+y*Room.Width]

    def empty_space(self):
        for i in range(Room.Width * Room.Heigth):
            self.space[i] = 0
        print r"Room's space is clear" 

class Board(object):
    def __init__(self):
        self.count = 4
        self.color = (255, 0, 0)


class Game(object):
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        
        self.room = Room()
        self.room.set_space((0, 0, 1))
        self.room.set_space((0, 1, 1))
        # Create surface for display
        #self.backsurface = pygame.Surface(self.screen.get_size())
        self.background = pygame.image.load('background.bmp').convert()
        
    def draw_room(self):
        for x in range(Room.Width):
            for y in range(Room.Heigth):
                if self.room.get_space((x, y)) != 0:
                    pygame.draw.rect(self.screen, (255,0,0) , Rect(x*20+3*(x+1),426-(y+1)*20-3*(y+1),20,20))
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            #self.backsurface.blit(self.background,(0,0))
            self.screen.blit(self.background,(0,0))
            self.draw_room()
            pygame.display.flip()
            self.clock.tick(40)
        pass


if __name__ == '__main__':
    r = Room()
    r.empty_space()
    r.set_space((0, 19, 4))
    r.get_space((0, 19))