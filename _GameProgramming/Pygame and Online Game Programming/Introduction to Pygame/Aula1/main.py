import pygame
from sys import exit

pygame.init()  # initialize pygame.

# create a display surface, usually called screen
SCRWIDTH = 800
SCRHEIGHT = 400
screen = pygame.display.set_mode((SCRWIDTH, SCRHEIGHT))  # (w, h) tuple
pygame.display.set_caption("Runner")  # sets window name

clock = pygame.time.Clock()  # will help us with time and framerate stuff

# game loop that keeps running forever
def game_loop():
    run = True

    # receive input
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # x button of the window
                run = False
                pygame.quit()
                exit()  # closes any kind of code when its called, avoiding pygame...update() to be called.

    # update everything
    pygame.display.update()
    # render elements

    clock.tick(60)  # while loop shouldn't run faster than 60 times per second.


game_loop()

