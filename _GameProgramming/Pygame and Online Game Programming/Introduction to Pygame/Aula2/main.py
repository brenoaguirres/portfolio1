import pygame
from sys import exit

pygame.init()  # initialize pygame.

# create a display surface, usually called screen
SCRWIDTH = 800
SCRHEIGHT = 400
screen = pygame.display.set_mode((SCRWIDTH, SCRHEIGHT))  # (w, h) tuple
pygame.display.set_caption("Runner")  # sets window name

clock = pygame.time.Clock()  # will help us with time and framerate stuff

# --- REGULAR SURFACE TYPES ---
# flat color
test_surface = pygame.Surface((100, 200))  # w, h
test_surface.fill("Red")  # rgb -  gives color to surface obj
# image
background = pygame.image.load('graphics/Sky.png')
ground = pygame.image.load('graphics/ground.png')
# text
# ---> 1) Create font asset; 2) Write on surface; 3) Blit to Screen surf.;
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)  # params -> font type (None), font size
text_surface = test_font.render("Runner", False, "Black")  # params -> text, AntiAliasing, color

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

        # update logic

        # render elements
        screen.blit(background, (0, 0))
        screen.blit(ground, (0, 300))
        screen.blit(test_surface, (200, 200))  # block image transfer (blit) or put a reg. surface on the displ. surface
        #                                   params - surf, (x,y)
        screen.blit(text_surface, (350, 50))

        # update everything
        pygame.display.update()
        clock.tick(60)  # while loop shouldn't run faster than 60 times per second.


game_loop()

