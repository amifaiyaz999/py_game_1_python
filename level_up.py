import pygame
import random

SCREEN_WIDTH , SCREEN_HEIGHT  = 600 , 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72
pygame.init()
bg= pygame.image.load('#image dite hobe')
background_image = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
font = pygame.font.SysFont("Times New ROman,FONT_SIZE")
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super() .__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(pygame.Color('dodgerblue'))
        pygame.draw.rect = self.image.get_rect()
        def move(self,x_change , y_change):
            self.rect.x =  max(min(self.rect.x + x_change,SCREEN_WIDTH - self.rect.width),0) 
            self.rect.y= max(min(self.rect.x + x_change,SCREEN_HEIGHT - self.rect.height),0)

screen = pygame.display.set_mode((SCREEN_WIDTH))
             