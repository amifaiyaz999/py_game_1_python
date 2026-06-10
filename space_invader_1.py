import math 
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_WIDTH = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_STARTS_Y_MIN = 50
ENEMY_START_Y_MAX = 320
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 4
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

background = pygame.image.load('#image')
pygame.display.set_caption("space invader")
icon = pygame.image.load('#image')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('#image')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0
playerY_change = 0

#enemy
enemyImg = []#list to store enemy images
enemyX = [ ]#list to store enemy X positions
enemyY = [] #list to store enemy Y position
enemyX_change = []
enemyY_change = []
num_of_enemy = 6
for _ in range(num_of_enemy):
    enemyImg.append(pygame.image.load('#image'))#load enemy image
    enemyX.append(random.randint(0,SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_STARTS_Y_MIN,ENEMY_START_Y_MAX))#y random position
    enemyX_change(ENEMY_SPEED_X)#set initial x movement speed
    enemyY_change.append(ENEMY_SPEED_Y )#set initial x movement speed

#BULLET

bulletImg= pygame.image.load("#image")
bulletX = 0 #current position of x
bulletY = PLAYER_START_Y #current y position
bulletX_change = 0#change in  bulllet x position(not used currently)
bulletY_change = BULLET_SPEED_Y # change in bullets's y position
bullet_state = 'ready'#state of bullet("ready" or "fire")