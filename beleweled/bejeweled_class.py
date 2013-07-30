#coding=utf-8
import pygame
import sys
import copy
import random
import time
from pygame.locals import *

reload(sys)
sys.setdefaultencoding("utf-8")

windowWidth,windowHeight=(800,600)
boardWidth,boardHeight=(8,8)        #8 * 8
gemNum=64
gemImageNum=5                       #钻石种类
gemSize=32                          #位图的实际像素是64 但这里设置为32为了后面MoveAction()有用 
                                    #其实后面也可以单独设置，只是懒得改了.....
#color
BLACK=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(0,0,0)

startX=44
startY=44
endX=556
endY=556

LEFT=1
RIGHT=2
UP=3
DOWN=4

moverate=25

Diamond=['red.png','green.png','blue.png','orange.png','yellow.png']
gemImages=[]


class Game:

    def __init__(self):
        pygame.init()
        self.score=0
        #load the images
        self.bg=pygame.image.load(r'background.jpg')
        for i in Diamond:
            gem=pygame.image.load(i)
            gemImages.append(gem)
        #trans.png是一个透明图层，用来暂时掩盖被消去的位置或交换的位置    
        self.trans=pygame.image.load('trans.png')
        #---------------------------------------------------------------
        
        self.screen=pygame.display.set_mode((windowWidth,windowHeight))
        self.clock=pygame.time.Clock()    
        pygame.display.set_caption('Bejeweled')
        
        #init the mainBoard
        #生成二维List[[{},{},...],[],....]
        self.mainBoard=[[{} for i in range(boardWidth)]for j in range(boardHeight)]
        for i in range(boardWidth):
            for j in range(boardHeight):
               #生成一个具备x,y坐标的宝石，并把它加入二维List
               cube={} 
               cube['imageColor']=gemImages[random.randint(0,4)]
               cube['x']=startX+j*64
               cube['y']=startY+i*64
               self.mainBoard[i][j]=cube
        #盘面初始化之初可能就有相连的可以消去的部分，所以用下面的方法更正
        #FindMatchedGems()遍历盘面查找能消掉的位置       
        matchedGemInit=self.FindMatchedGems()
        #直到都无法自动匹配为止
        while matchedGemInit!=[]:
            for gem in matchedGemInit:
                self.mainBoard[gem[0]][gem[1]]['imageColor']=gemImages[random.randint(0,4)]
                matchedGemInit.remove(gem)
            matchedGemInit+=self.FindMatchedGems()

                              
    #检查点击位置是否在Board内         
    def CheckIfInBoard(self,pos):
        if(pos[0]>startX and pos[0]<endX and pos[1]>startY and pos[1]<endY):
            x=int((pos[0]-startX)/64)
            y=int((pos[1]-startY)/64)
            return (y,x)                    #第y行x列
        return None

    def CheckFromClick(self,first,second):
        for pos in [first,second]:
            if self.mainBoard[pos[0]][pos[1]]['imageColor']==self.mainBoard[pos[0]][pos[1]-1]['imageColor']\
               ==self.mainBoard[pos[0]][pos[1]-2]['imageColor']:
                pygame.draw.rect(self.screen,BLACK,(self.mainBoard[pos[0]][pos[1]]['x'],\
                                                    self.mainBoard[pos[0]][pos[1]]['y'],\
                                                    64,64),width=0 )
                pygame.display.update()
                return True
            
    #完成宝石交换位置的动态效果，其实做的感觉还不是太好    
    def MoveAction(self,firstGem,secondGem):
        direction=firstGem['direction']
        moveX=0
        moveY=0
        Process=0
        while Process<=100 :
            process=Process
            process*=0.01
            
            if direction==LEFT:
                moveX=-int(process*gemSize)
            elif direction==RIGHT:
                moveX=int(process*gemSize)
            elif direction==UP:
                moveY=-int(process*gemSize)
            elif direction==DOWN:
                moveY=int(process*gemSize)
            firstGem['x']+=moveX
            firstGem['y']+=moveY
            
            secondGem['x']+=-moveX
            secondGem['y']+=-moveY

            self.screen.blit(firstGem['imageColor'],(firstGem['x'],firstGem['y']))
            self.screen.blit(secondGem['imageColor'],(secondGem['x'],secondGem['y']))
            
            #print firstGem['x']
            #print firstGem['y']
            Process+=moverate
            pygame.display.update()
            self.clock.tick(30) 
              
    def DropGem(self):
        Process=0       
        Distance=[]
        count=0
        #Record=[[] for j in range(8)]
        #move=0
        
        #统计没列空缺位置个数
        for j in range(8):
            for i in range(8):
                if self.mainBoard[i][j]['imageColor']==self.trans:
                    count+=1
            Distance.append(count)
            count=0
        print Distance
        #很遗憾，下落的动态效果还是没能做好，还是等到下个版本在更新吧.....
        '''    
        for col in range(8):
            temp={}
            Process=0
            if (Distance[col]!=0):
                while Process<4:
                   
                    process=Process
                    process*=0.01
                    move=int(process*32)
                   
                    move=16
                    for line in range(8):
                        if self.mainBoard[line][col]['imageColor']==self.trans:
                            if line==0:
                                temp={'x':self.mainBoard[line][col]['x'],\
                                      'y':-64+move,\
                                      'imageColor':gemImages[random.randint(0,4)]}
                                self.screen.blit(temp['imageColor'],(temp['x'],temp['y']))
                                self.mainBoard[0][col]['iamgecolor']=temp['imageColor']
                            else:
                                self.mainBoard[line-1][col]['y']+=move
                                self.screen.blit(self.mainBoard[line][col]['imageColor'] ,\
                                     (self.mainBoard[line][col]['x'],self.mainBoard[line][col]['y']))
                    Process+=1
                    pygame.display.update()
                    self.clock.tick(30)                     
                #self.mainBoard[0][col]['imageColor']=temp['imageColor']                
                for i in range(7,0,-1):
                    self.mainBoard[i][col]['imageColor']=self.mainBoard[i-1][col]['imageColor']
                #self.mainBoard[0][col]['imageColor']=temp['imageColor']            
        '''
        #类似于冒泡的方法将空缺位置上移
        for col in range(8):
            while(Distance[col]!=0):
                for line in range(8):
                    if(self.mainBoard[line][col]['imageColor']==self.trans):
                        if(line==0):
                            self.mainBoard[0][col]['imageColor']=gemImages[random.randint(0,4)]
                            Distance[col]=Distance[col]-1
                        else:
                            self.mainBoard[line][col]['imageColor']=self.mainBoard[line-1][col]['imageColor']
                            self.mainBoard[line-1][col]['imageColor']=self.trans
                            
                  
                    
                
    #对选中钻石进行交换                         
    def SwapGem(self,firstGem,secondGem,first,second):
        if firstGem['imageColor']==self.trans or secondGem['imageColor']==self.trans:
            return None
        firstGem['direction']=None
        secondGem['direction']=None
        if first[0]==second[0] and first[1]==second[1]+1:
            firstGem['direction']=LEFT
            secondGem['direction']=RIGHT
        elif first[0]==second[0] and first[1]==second[1]-1:
            firstGem['direction']=RIGHT
            secondGem['direction']=LEFT
        elif first[0]==second[0]+1 and first[1]==second[1]:
            firstGem['direction']=UP
            secondGem['direction']=DOWN
        elif first[0]==second[0]-1 and first[1]==second[1]:
            firstGem['direction']=DOWN
            secondGem['direction']=UP             


        self.mainBoard[first[0]][first[1]]['imageColor']=self.trans
        self.mainBoard[second[0]][second[1]]['imageColor']=self.trans
        self.MoveAction(firstGem,secondGem)
        self.mainBoard[first[0]][first[1]]['imageColor']=secondGem['imageColor']
        self.mainBoard[second[0]][second[1]]['imageColor']=firstGem['imageColor']

  
    def getSwappingGems(self, firstXY, secondXY):
        firstGem = {'imageColor': self.mainBoard[firstXY[0]][firstXY[1]]['imageColor'],
                    'x':self.mainBoard[firstXY[0]][firstXY[1]]['x'] ,
                    'y':self.mainBoard[firstXY[0]][firstXY[1]]['y']}
        secondGem = {'imageColor': self.mainBoard[secondXY[0]][secondXY[1]]['imageColor'],
                     'x': self.mainBoard[secondXY[0]][secondXY[1]]['x'],
                     'y': self.mainBoard[secondXY[0]][secondXY[1]]['y']}
        return firstGem, secondGem
    
    #遍历Board查找匹配位置
    def FindMatchedGems(self):
        board=self.mainBoard
        matchedGem=[]
        for i in range(boardHeight):
            for j in range(boardWidth-2):
                if board[i][j]['imageColor']==self.trans:continue
                elif( board[i][j]['imageColor']==board[i][j+1]['imageColor']==board[i][j+2]['imageColor']):
                    if (i,j) not in matchedGem: matchedGem.append( (i,j) )
                    if (i,j+1) not in matchedGem: matchedGem.append( (i,j+1) )
                    if (i,j+2) not in matchedGem: matchedGem.append( (i,j+2) )
        for j in range(boardWidth):
            for i in range(boardHeight-2):
                if board[i][j]['imageColor']==self.trans:continue
                elif (board[i][j]['imageColor']==board[i+1][j]['imageColor']==board[i+2][j]['imageColor']):
                    if (i,j) not in matchedGem: matchedGem.append( (i,j) )
                    if (i+1,j) not in matchedGem: matchedGem.append( (i+1,j) )
                    if (i+2,j) not in matchedGem: matchedGem.append( (i+2,j) )
        
        return matchedGem
    
    def Run(self):
        firstSelectedGem=None
        lastMouseDownX =None
        lastMouseDownY =None
        isGameOver     =False
        firstGem=None
        secondGem=None
        
        while True:
           clickedSpace = None
           for event in pygame.event.get():
             if event.type==QUIT:
                 pygame.quit()
                 sys.exit()
             if event.type==KEYUP:
                 if event.key==K_ESCAPE:
                     pygame.quit()
                     sys.exit()
                 #reset还没做...
             if event.type==MOUSEBUTTONUP:
                 if isGameOver:
                     return
                 #this is a real click no mouse drag   
                 if event.pos==(lastMouseDownX,lastMouseDownY):   
                     clickedSpace=self.CheckIfInBoard(event.pos)
                     
                 #this has a mouse drag    
                 else:
                     firstSelectedGem=self.CheckIfInBoard((lastMouseDownX,lastMouseDownY))
                     mouseOverSpace=self.CheckIfInBoard(event.pos)
                     if mouseOverSpace and (mouseOverSpace[0]==firstSelectedGem[0]+1\
                                            or mouseOverSpace[0]==firstSelectedGem[0]-1\
                                            or mouseOverSpace[1]==firstSelectedGem[1]+1\
                                            or mouseOverSpace[1]==firstSelectedGem[1]-1):
                         clickedSpace=mouseOverSpace
                     if not firstSelectedGem or not mouseOverSpace:
                         firstSelectedGem=None
                         mouseOverSpace=None
                     
                     
             if event.type==MOUSEBUTTONDOWN:
                 lastMouseDownX, lastMouseDownY=event.pos
           
           if clickedSpace and not firstSelectedGem:
               firstSelectedGem=clickedSpace
               print firstSelectedGem
           elif clickedSpace and firstSelectedGem:
               print firstSelectedGem
               print clickedSpace
               firstGem, secondGem = self.getSwappingGems(firstSelectedGem, clickedSpace)
               
               self.SwapGem(firstGem,secondGem,firstSelectedGem,clickedSpace)
               matchedGems=self.FindMatchedGems()
               print matchedGems
               #无匹配 
               if matchedGems==[]:
                   self.SwapGem(firstGem,secondGem,clickedSpace,firstSelectedGem)
               else:
                   while(matchedGems!=[]):
                       for (i,j) in matchedGems:
                           self.mainBoard[i][j]['imageColor']=self.trans
                       self.DropGem()
                       matchedGems=self.FindMatchedGems()                      
               firstSelectedGem=None
               mouseOverSpace=None            
           #draw mainBoard    
           self.screen.blit(self.bg,(0,0)) 
           for i in range(boardWidth):
              for j in range(boardHeight):
                 self.screen.blit(self.mainBoard[i][j]['imageColor'],(self.mainBoard[i][j]['x'],self.mainBoard[i][j]['y']) )
                
           pygame.display.update()          
           self.clock.tick(30)        
    


mygame=Game()
mygame.Run()
        









        
