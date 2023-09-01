import pygame
from network import Network
import pygame
import pickle
from GUI.button import Button

SCRWIDTH = 700
SCRHEIGHT = 700
window = pygame.display.set_mode((SCRWIDTH, SCRHEIGHT))
pygame.display.set_caption("RSPClient")

pygame.font.init()

font = pygame.font.SysFont("comicsans", 90)

buttons = [
    Button("Rock", 50, 500, (0, 0, 255)),
    Button("Scissors", 250, 500, (255, 0, 0)),
    Button("Paper", 450, 500, (0, 255, 0))
           ]


def redraw_window(window, game, p):
    window.fill((128, 128, 128))

    if not game.connected():
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render("Waiting for player...", 1, (255, 0, 0), True)
        text_rect = text.get_rect(center=(SCRWIDTH / 2, SCRHEIGHT / 2))
        window.blit(text, text_rect)
    else:
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Your Move", 1, (0, 255, 255))
        window.blit(text, (80, 200))

        text = font.render("Opponents", 1, (0, 255, 255))
        window.blit(text, (380, 200))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)

        if game.both_went():
            text1 = font.render(move1, 1, (0, 0, 0))
            text2 = font.render(move2, 1, (0, 0, 0))
        else:
            if game.p1Went and p == 0:
                text1 = font.render(move1, 1, (0, 0, 0))
            elif game.p1Went:
                text1 = font.render("Locked In", 1, (0, 0, 0))
            else:
                text1 = font.render("Waiting...", 1, (0, 0, 0))

            if game.p2Went and p == 1:
                text2 = font.render(move1, 1, (0, 0, 0))
            elif game.p2Went:
                text2 = font.render("Locked In", 1, (0, 0, 0))
            else:
                text2 = font.render("Waiting...", 1, (0, 0, 0))

        if p == 1:
            window.blit(text2, (100, 300))
            window.blit(text1, (400, 350))
        else:
            window.blit(text1, (100, 300))
            window.blit(text2, (400, 350))

        for btn in buttons:
            btn.draw(window)

    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    connection = Network()
    player = int(connection.getP())
    print("You are player ", player)

    while run:
        clock.tick(60)

        try:
            game = connection.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.both_went():
            redraw_window(window, game, player)
            pygame.time.delay(500)
            try:
                game = connection.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            if (game.winner() == 1 and player == 1) or (game.winner == 0 and player == 0):
                text = font.render("You Won!", 1, (255, 0, 0))
            elif game.winner() == -1:
                text = font.render("Tie game!", 1, (255, 0, 0))
            else:
                text = font.render("You Lost!", 1, (255, 0, 0))

            text.blit(text, (window.get_width() / 2 - text.get_width() / 2,
                             window.get_height() / 2 - text.get_height() / 2))

            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in buttons:
                    if btn.click(pos) and game.connected():
                        if player == 0:
                            if not game.p1Went:
                                connection.send(btn.text)
                        else:
                            if not game.p2Went:
                                connection.send(btn.text)

        redraw_window(window, game, player)


def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        window.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to play!", 1, (255, 0, 0))
        text_rect = text.get_rect(center=(SCRWIDTH / 2, SCRHEIGHT / 2))
        window.blit(text, text_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()


while True:
    menu_screen()

