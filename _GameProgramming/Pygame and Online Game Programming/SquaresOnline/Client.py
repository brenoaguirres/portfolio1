import pygame
import Player
from Network import Network

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def redrawWindow(window, player1, player2):

    window.fill((255, 255, 255))
    player1.draw(window)
    player2.draw(window)
    pygame.display.update()


def gameLoop():

    run = True
    network = Network()
    player1 = network.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        player2 = network.send(player1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player1.move()
        redrawWindow(win, player1, player2)


gameLoop()

