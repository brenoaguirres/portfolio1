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
snail_speed = 2
snail_rectangle = snail_surface.get_rect(midbottom=(600, 300))

# --- RECTANGLES ---
# for rectangles you can you tuple values (x,y) alligning to:
#   topleft, midtop, topright, midleft, center, midright, bottomleft, midbottom, bottomright
# for individual values you can allign to:
# x,y (topleft), top, left, (centerx, centery), right, bottom
# other properties: size, width, height
player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()

# pygame.Rect(left, top, width, height)
player_rectangle = player_surface.get_rect(midbottom=(80, 300))  # takes a surface and draw a rect around it



def game_loop():
    run = True

    global snail_speed

    # receive input
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()

        # update logic
        if snail_rectangle.right >= 0:
            snail_rectangle.x -= snail_speed
        else:
            snail_rectangle.left = 800

        player_rectangle.left += 2

        # render elements
        screen.blit(background, (0, 0))
        screen.blit(ground, (0, 300))
        screen.blit(text_surface, (350, 50))
        screen.blit(snail_surface, snail_rectangle)
        screen.blit(player_surface, player_rectangle)

        # update everything
        pygame.display.update()
        clock.tick(60)


game_loop()

