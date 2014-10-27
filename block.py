import pygame

class Block:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32

    def render(self,window):
        pygame.draw.rect(window,(227,220,118),(self.x,self.y,self.width,self.height))
        
