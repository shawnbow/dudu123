#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""用于测试游戏中的功能的垃圾代码集散地"""

#       Redistribution and use in source and binary forms, with or without
#       modification, are permitted provided that the following conditions are
#       met:
#       
#       * Redistributions of source code must retain the above copyright
#         notice, this list of conditions and the following disclaimer.
#       * Redistributions in binary form must reproduce the above
#         copyright notice, this list of conditions and the following disclaimer
#         in the documentation and/or other materials provided with the
#         distribution.
#       * Neither the name of the  nor the names of its
#         contributors may be used to endorse or promote products derived from
#         this software without specific prior written permission.
#       
#       THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#       "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#       LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#       A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#       OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#       SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#       LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#       DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#       THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#       (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#       OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#       

import os
import sys
import pygame
from sys import exit
from pygame.locals import *
from copy import copy
import time
import random
import math
from lib import *
import glob
from zipfile import *
import json
import game
import stage
import glob

WIDTH = 815
HEIGHT = 700


def to_tmp(p):
    zf = ZipFile(p,"r")
    
    p = os.getcwd() + os.path.sep + "tmp" + os.path.sep
    print p
    ioconv = zf.extractall(p)
    zf.close()

def read_map_cfg():
    p = os.getcwd() + os.sep + "tmp" + os.sep + "map.cfg"
    
    f = open(p,"r")
    txt = "".join(f.readlines())
    f.close()
    print txt
    dic = json.loads(txt)
    print dic

def init_floor():
    p = OTHER_RES_PATH + "tile.bmp"
    image = load_image(p,"")
    
    debug_print(image)

    
    """土"""
    stage.Soil.image = pygame.Surface((32,32))
    stage.Soil.image.blit(image,(0,0),Rect(0,0,32,32)) #土
    
    """水"""
    stage.Water.image = pygame.Surface((32,32))
    stage.Water.image.blit(image,(0,0),Rect(96,0,32,32)) #水
        
    """冰"""
    stage.Ice.image = pygame.Surface((32,32))
    stage.Ice.image.fill((255,255,255))

    """草"""
    stage.Grass.image = pygame.Surface((32,32))
    stage.Grass.image.blit(image,(0,0),Rect(64,0,32,32)) 


    """铁"""
    stage.Iron.image = pygame.Surface((32,32))
    stage.Iron.image.blit(image,(0,0),Rect(32,0,32,32))
    debug_print(stage.Iron.image )
    


    image = load_image(OTHER_RES_PATH + "gray.bmp","")
    
    """灰"""
    stage.Gray.image = pygame.Surface((32,32))
    stage.Gray.image.blit(image,(0,0),Rect(0,0,32,32)) 

def main():
    born_pos = [[50,50],[350,50],[650,50]]
    i = 0

    if live_drone_count < 5:
        if self.add_drone() == True:#()
            #Drone.count += 1
            live_drone_count += 1    


if __name__ == '__main__':
    main()

