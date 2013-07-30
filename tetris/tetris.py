#!/usr/bin/python
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import game
import pygame
from pygame.locals import *

window_width = 412
window_heigth = 426

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
    teris_game = game.Game(screen)
    teris_game.run()
    
    return 0

if __name__ == '__main__':
    main()

    
    
    