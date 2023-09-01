import pygame
from sys import exit

pygame.init()

SCRWIDTH = 800
SCRHEIGHT = 400
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

screen = pygame.display.set_mode((SCRWIDTH, SCRHEIGHT))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

background = pygame.image.load('graphics/Sky.png').convert_alpha()  # convert image to a pygame object
ground = pygame.image.load('graphics/ground.png').convert_alpha()
text_surface = test_font.render("Runner", False, "Black")
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600
snail_speed = 2


def game_loop():
    run = True

    global snail_x_pos
    global snail_speed

    # receive input
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()

        # update logic
        if snail_x_pos > -50:
            snail_x_pos -= snail_speed
        else:
            snail_x_pos = 820

        # render elements
        screen.blit(background, (0, 0))
        screen.blit(ground, (0, 300))
        screen.blit(text_surface, (350, 50))
        screen.blit(snail_surface, (snail_x_pos, 265))

        # update everything
        pygame.display.update()
        clock.tick(60)


game_loop()

