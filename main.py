import pygame
import math
import random
#pygame
pygame.init()
#creat screen
screen = pygame.display.set_mode((800,600))

#Background
background =pygame.image.load('assets/cam.png')

#icon
pygame.display.set_caption("space for fight") #name
icon = pygame.image.load('assets/swords.png')
pygame.display.set_icon(icon)

#enemy
enemyImg = pygame.image.load('assets/spaceNLO.png')
enemyX = random.randint(0, 700)
enemyY = random.randint(50, 150)
enemyX_change = 1
enemyY_change = 40


# Bullet
# Fire - the bullet is currently moving

bulletImg = pygame.image.load('assets/push.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 3
bullet_state = 'ready'

#player
playerImg = pygame.image.load('assets/space.png')
playerX = 370
playerY = 480
playerX_change = 0

score=0

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x,y):
    screen.blit(enemyImg,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x + 16,y + 10))


def isCollision (enemyX , enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27 :
        return True
    else:
        return False


# game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(120)
    # RGB - red , green, blue
    screen.fill((255, 255, 255))
    # Background image
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if u go left or right keybourd

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # Get the current x cordinate fo the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)





        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1
    # For space dont go out window
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # enemy move
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 1
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -1
        enemyY += enemyY_change

     # Bullet move
    if bulletY <=0 :
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 700)
        enemyY = random.randint(50, 150)


    player(playerX,playerY)
    enemy(enemyX,enemyY)

    pygame.display.update()

if enemyX==380 and enemyY==480:
    running = False


