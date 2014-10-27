import pygame

class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.velocity = 0
        self.falling = True
        self.onGround = False

    def update(self,gravity,blockList):
            
        if(self.velocity<0 ):
            self.falling = True
        collision = False
        blockx = 0
        blocky = 0
        for block in blockList:
            collision = self.detectCollisions(self.x,self.y,self.width,self.height,block.x,block.y,block.width,block.height)
            if(collision == True):
                blockx = block.x
                blocky = block.y
                break
            if(self.velocity == 0 and collision == False):
                self.falling = True
                self.onGround = False
        

        if(collision == True):
            
            if (self.falling == True):
                if(self.velocity<=0):
                    self.falling = False
                    self.onGround = True
                    self.y = blocky - self.height
                   
                self.velocity = 0

        if(self.onGround == False):
            
            self.velocity += gravity
        self.y -= self.velocity
        
        

    def jump(self):
        if(self.onGround == False):
            return
        elif(self.onGround == True):
            
            if( self.velocity ==0):

                self.velocity = 8
                self.onGround = False 
   

    def render(self,window):
        pygame.draw.rect(window,(255,150,1),(self.x,self.y,self.width,self.height))
 
    def detectCollisions(self,x1,y1,w1,h1,x2,y2,w2,h2):
        if((w1 + w2)/2 >= x2-x1 and x2 >= x1 and (h1 + h2)/2 >= y2-y1 and y2 >= y1):
            return True
        if((w1 + w2)/2 >= x2-x1 and x2 >= x1 and (h1 + h2)/2 >= y1-y2 and y1 >= y2):
            return True

        if((w1 + w2)/2 >= x1-x2 and x1 >= x2 and (h1 + h2)/2 >= y1-y2 and y1 >= y2):
            return True

        if((w1 + w2)/2 >= x1-x2 and x1 >= x2 and (h1 + h2)/2 >= y2-y1 and y2 >= y1):
            return True

        else:
            return False
