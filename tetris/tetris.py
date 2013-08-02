#!/usr/bin/python
#coding=utf-8
import sys
import pygame
from pygame.locals import *

# reload(sys)
# sys.setdefaultencoding("utf-8")
window_width, window_heigth = (540, 536)

color_table = ((0, 0, 0),
               (0, 0, 255), 
               (0, 255, 0),
               (0, 255, 255),
               (255, 0, 0),
               (255, 0, 255),
               (255, 255, 0),
               (0, 128, 128),
               )

class Room(object):

    # 10*18 space
    Width, Heigth = (10,18)

    def __init__(self):
        self.space = list([0]*Room.Width*Room.Heigth)
    
    def set_space(self, (x, y), value):
        if (x >= Room.Width or y <= Room.Heigth):
            raise ValueError, (x, y), value
        self.space[x+y*Room.Width] = value
        print 'Board (%s,%s)' %(x, y), 'set to %s' %value
    
    def get_space(self, (x, y)):
        return self.space[x+y*Room.Width]

    def empty_space(self):
        for i in range(Room.Width * Room.Heigth):
            self.space[i] = 0
        print "Room's space is clear" 


class Board(object):
    def __init__(self, style):
        self.style = style
        self.color = color_table[self.style]
        # oooo
        if self.style == 1: 
            self.count = 4
            self.position = (4, 17)
            self.shape = [[0,0],[-1,0],[1,0],[2,0]]
        # ooo
        #   o
        elif self.style == 2:
            self.count = 4
            self.position = (4, 17)
            self.shape = [[0,0],[-1,0],[1,0],[1,-1]]
        # ooo
        # o
        elif self.style == 3:
            self.count = 4
            self.position = (4, 17)
            self.shape = [[0,0],[-1,-1],[-1,0],[1,0]]
        # oo
        #  oo
        elif self.style == 4:
            self.count = 4
            self.position = (4, 17)
            self.shape = [[0,0],[-1,0],[0,-1],[1,-1]]
        #  oo
        # oo
        elif self.style == 5:
            self.count = 4
            self.position = (4, 17)
            self.shape = [[0,0],[-1,-1],[0,-1],[1,0]]
        # ooo
        #  o
        elif self.style == 6:
            self.count = 4
            self.position = (4, 17)
            self.shape = [[0,0],[-1,0],[0,-1],[1,0]]
        # oo
        # oo
        elif self.style == 7:
            self.count = 4
            self.position = (5, 17)
            self.shape = [[0,0],[-1,0],[-1,-1],[0,-1]]
        else:
            raise ValueError, 'Style %s not support'%self.style
        
    def rotate(self):
        if self.style == 7:
            return 
        elif self.style == 1:
            
        for i in range(self.count):
            x = self.shape[i][1]*-1
            y = self.shape[i][0]
            self.shape[i][0] = x
            self.shape[i][1] = y


class Game(object):
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        
        self.room = Room()
        # Create surface for display
        #self.backsurface = pygame.Surface(self.screen.get_size())
        self.background = pygame.image.load('background.png').convert()
    
    def draw_square(self, x, y, color):
        pygame.draw.rect(self.screen, color,
                          Rect(14+x*25+3*(x+1), 521-(y+1)*25-3*(y+1), 25, 25))
    
    def draw_room(self):
        for x in range(Room.Width):
            for y in range(Room.Heigth):
                if self.room.get_space((x, y)) != 0:
                    self.draw_square(x, y, color_table[self.room.get_space((x, y))])
    
    def draw_board(self, board):
        for i in range(board.count):
            x = board.shape[i][0] + board.position[0]
            y = board.shape[i][1] + board.position[1]
            self.draw_square(x, y, board.color)

    def run(self):
        b = Board(1)
        b.position = (5,5)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            #self.backsurface.blit(self.background,(0,0))
            self.screen.blit(self.background,(0,0))
            self.draw_room()
            b.rotate()
            self.draw_board(b)
            pygame.display.flip()
            self.clock.tick(5)
        pass


def main():
    # Initial pygame
    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print 'Warning: no sound card!'
        pygame.mixer = None

    # Set window properties
    pygame.display.set_caption('Tetris')
    screen = pygame.display.set_mode((window_width, window_heigth), 0, 32)

    # Start game main loop
    teris_game = Game(screen)
    teris_game.run()
    return 0

if __name__ == '__main__':
    main()
