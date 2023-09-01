import random
import math
import pygame
from pygame import mixer

# Initialize pygame module
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)  # '-1' parameter plays on loop

# Caption and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo (1).png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0
speed = 3
minPosition = 0
maxPosition = 736

# Enemy

enemyImg = []  # This means an empty list
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemySpeed = []
enemyMinPosition = []
enemyMaxPosition = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    enemyY_change.append(40)
    enemySpeed.append(2)
    enemyMinPosition.append(0)
    enemyMaxPosition.append(736)

# Bullet
# bullet_isFiring = False // Can't see bullet on screen
# bullet_isFiring = True // Can see bullet on screen
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_isFiring = False

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game Over Text
game_over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def show_game_over():
    over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


# global keyword access generic variable bullet_isFiring
def fire_bullet(x, y):
    global bullet_isFiring
    bullet_isFiring = True
    screen.blit(bulletImg, (x + 16, y + 10))


# Define whether a collision between two objects has ocurred or not
# object1 // enemy
# object2 // bullet
def isCollision(object1_X, object1_Y, object2_X, object2_Y):
    distance = math.sqrt(math.pow((object2_X - object1_X), 2) + math.pow((object2_Y - object1_Y), 2))
    if distance < 27:
        return True


# Game Loop
running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -speed
            if event.key == pygame.K_RIGHT:
                playerX_change = speed
            if event.key == pygame.K_SPACE:
                if bullet_isFiring is False:
                    # Bullet Sound
                    bullet_Sound = mixer.Sound('laser.wav')
                    bullet_Sound.play()

                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    # Player Movement

    if playerX <= minPosition:
        playerX = minPosition
    elif playerX >= maxPosition:
        playerX = maxPosition

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            show_game_over()
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= enemyMinPosition[i]:
            enemyX_change[i] = enemySpeed[i]
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= enemyMaxPosition[i]:
            enemyX_change[i] = -enemySpeed[i]
            enemyY[i] += enemyY_change[i]

        # Collision

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            # Collision Sound
            collision_Sound = mixer.Sound('explosion.wav')
            collision_Sound.play()

            bulletY = 480
            bullet_isFiring = False
            score_value += 50
            # Respawn
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(0, 150)

        # Enemy Spawn
        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bullet_isFiring = False
        bulletY = 480
    if bullet_isFiring is True:
        bulletY -= bulletY_change
        fire_bullet(bulletX, bulletY)

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
