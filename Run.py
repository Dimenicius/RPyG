# -*-coding:UTF-8-*-

import pygame
import menu
import chrmod
import utils
import player
import lobby
import maps

Utils = utils.Utils()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()


def playIntro():

    img1 = pygame.image.load('sprites/intro/HT_faixa.jpg')
    img2 = pygame.image.load('sprites/intro/HT_clean.jpg')
    img3 = pygame.image.load('sprites/intro/tape.jpg')
    img4 = pygame.image.load('sprites/intro/tape_title.jpg')

    for i in range(127):
        screen.fill((0, 0, 0))
        img1.set_alpha(i * 2)
        screen.blit(img1, (0, 0))
        pygame.display.flip()

    img1.set_alpha(255)
    for i in range(127):
        screen.blit(img1, (0, 0))
        img2.set_alpha(i * 2)
        screen.blit(img2, (0, 0))
        pygame.display.flip()

    img2.set_alpha(255)
    for i in range(100):
        if i > 10 and i < 15:
            screen.blit(img3, (0, 0))
        elif i > 45 and i < 65:
            screen.blit(img3, (0, 0))
        elif i > 90:
            screen.blit(img3, (0, 0))
        else:
            screen.blit(img2, (0, 0))
        pygame.display.flip()

    for i in range(100):
        screen.blit(img3, (0, 0))
        pygame.display.flip()

    for i in range(127):
        screen.blit(img3, (0, 0))
        img4.set_alpha(i * 2)
        screen.blit(img4, (0, 0))
        pygame.display.flip()

    for i in range(100):
        screen.blit(img4, (0, 0))
        pygame.display.flip()

    for i in range(255):
        screen.fill((0, 0, 0))
        img4.set_alpha(255 - (i * 2))
        screen.blit(img4, (0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    # Creating the screen
    clock = pygame.time.Clock()
    clock.tick(50)

    # screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN, 32)
    screen = pygame.display.set_mode((800, 600), 0, 32)

    icon = pygame.image.load('sprites/icon.jpeg')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('RPyG - A Role Playing Game in Python')

    # playIntro()

    # pygame.mixer.music.load('sounds/12.ogg')
    # pygame.mixer.music.play(0)

    active_char = None
    mapa = None
    while True:

        if Utils.getList('databases/players') is not None and Utils.findActive(Utils.getList('databases/players')) is not None:
            active_char, char_list = Utils.findActive(
                Utils.getList('databases/players'))
            GM = menu.Menu(screen, char_list)
        else:
            GM = menu.Menu(screen)

        choice = GM.run()

        if choice == 0:
            points = 5
            CM = chrmod.CharModification(
                screen, points, [5, 5, 5, 5, 5, 5, 5])
            CM.run()
        elif choice == 1:
            if not Utils.getList('databases/players') == []:
                if active_char is None:
                    CM = chrmod.CharModification(
                        screen, 0, [0, 0, 0, 0, 0, 0, 0], Utils.getList('databases/players'), charmod=player.Player(0))
                else:
                    CM = chrmod.CharModification(
                        screen, 0, [0, 0, 0, 0, 0, 0, 0], Utils.getList('databases/players'), active_char, charmod=player.Player(active_char))
                CM.run()
        elif choice == 2:
            LB = lobby.Lobby(screen, active_char)
            LB.run()
        elif choice == 3:
            # CM = chrmod.CharModification(
            #     screen, 0, [0, 0, 0, 0, 0, 0, 0], Utils.getList('databases/players'), active_char, 1)
            # CM.run()
            LB = lobby.Lobby(screen, active_char, True)
            LB.run()

        elif choice == 'QUIT':
            quit()
