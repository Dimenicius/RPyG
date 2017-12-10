# -*-coding:UTF-8-*-
import pygame
import os
import utils
# os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
Utils = utils.Utils()


class Splash():
    def __init__(self, screen):
        font = 'font/BEBAS.ttf'
        font_size = 35

        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height

        self.background = pygame.image.load('sprites/splash.png')

        self.font = pygame.font.Font(font, font_size)
        self.items = ['PLAY     GAME', 'ADMIN     TOOLS']
        self.createButtons()

    def createButtons(self):
        self.menu_Items = []
        self.mo_menu_Items = []
        for index, item in enumerate(self.items):
            text = self.font.render(item, True, (250, 250, 250))
            mo_text = self.font.render(item, True, (23, 92, 207))

            t_w = text.get_rect().width
            t_h = text.get_rect().height
            pos_y = 330
            pos_x = index * (self.scr_width / 2) + \
                ((self.scr_width / 2) - t_w) / 2

            self.menu_Items.append([text, pos_x, pos_y, t_w, t_h])
            self.mo_menu_Items.append([mo_text, pos_x, pos_y, t_w, t_h])

    def printButtons(self, mouse_pos):

        button = []
        for index, data in enumerate(self.menu_Items):
            text, pos_x, pos_y, width, height = data

            button.append(pygame.Rect(
                pos_x, pos_y, width, height))

            if not button[index].collidepoint(mouse_pos):
                self.screen.blit(self.menu_Items[index][0], (pos_x, pos_y))
            else:
                self.screen.blit(self.mo_menu_Items[index][0], (pos_x, pos_y))

    def activate(self, mouse_pos):
        button = []
        for index, data in enumerate(self.menu_Items):
            text, pos_x, pos_y, width, height = data

            button.append(pygame.Rect(
                pos_x, pos_y, width, height))

            if button[index].collidepoint(mouse_pos):
                self.start(index)

    def start(self, index):
        if index == 0:
            os.system('python2 Run.py &')
        elif index == 1:
            os.system('python2 tools.py &')


if __name__ == "__main__":
    # Creating the screen
    clock = pygame.time.Clock()
    clock.tick(50)

    # screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN, 32)
    screen = pygame.display.set_mode((500, 400), pygame.NOFRAME, 32)

    icon = pygame.image.load('sprites/icon.jpeg')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('RPyG - A Role Playing Game in Python')

    # playIntro()

    # pygame.mixer.music.load('sounds/12.ogg')
    # pygame.mixer.music.play(0)
    splash = Splash(screen)
    mouse_pos = (0, 0)
    splash.running = True
    while splash.running:
        screen.blit(splash.background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = Utils.getMousePosition(0, 0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                splash.activate(mouse_pos)
        splash.printButtons(mouse_pos)
        pygame.display.flip()
