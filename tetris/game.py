#coding=utf-8
import sys
# import copy
# import random
# import time
import pygame
from pygame.locals import *


class Game(object):
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        
        # Create surface for display
        self.backsurface = pygame.Surface(self.screen.get_size())
        self.background = pygame.image.load('background.bmp').convert()
        
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.backsurface.blit(self.background,(0,0))
            self.screen.blit(self.backsurface,(0,0))
            pygame.display.flip()
            self.clock.tick(40)
        pass



