import pygame
from player import *
from block import *

pygame.init()

window = pygame.display.set_mode((768,600))
pygame.display.set_caption('Platformer')

gravity = -0.5

black = (0,0,0)
blue  = (50,0,150)

player = Player(20,120)
#800/32 = 25
#600/32 = 18.75
level1 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0],
    [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1] 
    

    ]

clock = pygame.time.Clock()
blockList = []
for y in range(0,len(level1)):
    for x in range (0,len(level1[y])):
        if (level1[y][x]== 1):
            blockList.append(Block(x*32,y*32))

moveX = 0
moveY = 0


            
gameLoop = True
while gameLoop:

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            gameLoop = False
            
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_RIGHT):
                moveX = 5
            elif (event.key == pygame.K_LEFT):
                moveX = -5
            elif (event.key == pygame.K_UP):
                player.jump()
            
            
                
        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_RIGHT):
                moveX = 0
            elif (event.key == pygame.K_LEFT):
                moveX = 0
            
                
                
          


    window.fill((0,170,8))
    for block in blockList:
        block.render(window)

    player.x += moveX
    player.update(gravity,blockList)
    
    player.render(window)
    
    clock.tick(40)
    pygame.display.flip()

pygame.quit()
