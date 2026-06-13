import math 
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
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
    enemyY.append(random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))#y random position
    enemyX_change(ENEMY_SPEED_X)#set initial x movement speed
    enemyY_change.append(ENEMY_SPEED_Y )#set initial x movement speed

#BULLET

bulletImg= pygame.image.load("#image")
bulletX = 0 #current position of x
bulletY = PLAYER_START_Y #current y position
bulletX_change = 0#change in  bulllet x position(not used currently)
bulletY_change = BULLET_SPEED_Y # change in bullets's y position
bullet_state = 'ready'#state of bullet("ready" or "fire")




# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    # Display the current score on the screen.
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    # Display the game over text
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    # Draw the player on the screen
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    # Draw an enemy on the screen
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    # Fire a bullet from the player's position
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    # Check if there is a collision between the enemy and a bullet
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE


running = True
while running:
    screen.fill(0,0,0)#fill screem with black(background)
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #exit game loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state =="ready":
                bulletX == playerX
                fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT , pygame.K_RIGHT]:
            playerX_chnage = 0



    playerX += playerX_change
    playerX = max(0,min(playerX,SCREEN_WIDTH-64))



    for i in range(num_of_enemy):
        if enemyY[i]>340:
            for j in range(num_of_enemy):
                enemyY[j] =2000

            game_over_text()

            break

        enemyX[i]+=enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i]>=  SCREEN_WIDTH - 64:
            enemyX_change[i] *= -1
            enemyY[i]+= enemyY_change[i]





        if isCollision(enemyX[i],enemy[i],bulletX,bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = 'ready'
            score_value +=1
            enemyX[i] = random.randint(0,SCREEN_WIDTH - 64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN , ENEMY_START_Y_MAX)
        enemy(enemyX[i],enemyY[i],i)
    if bulletY <=0: #if bullet f
        bulletY = PLAYER_START_Y
        bullet_state = 'ready'
    elif bullet_state =="fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    player(playerX,playerY) #draw player

    show_score(textX,textY) #draw score
    pygame.display.update() #update the display