import pygame
import utils
Utils = utils.Utils()


class Map():
    def __init__(self, screen):

        font = 'font/BEBAS.ttf'
        font_size = 35
        # font_color = (255, 255, 255)

        self.screen = screen
        self.surface = pygame.Surface((400, 250), pygame.SRCALPHA, 32)
        self.charsurface = pygame.Surface((130, 260))
        self.scr_width = self.surface.get_rect().width
        self.scr_height = self.surface.get_rect().height

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(font, font_size)
        self.icon_font = pygame.font.Font(font, 20)

        self.background = pygame.image.load('sprites/map/map.jpg')

        self.mapPos = [0, 0]
        self.icons = []
        self.cld_icon = None

    def checkEvents(self):
        global mainloop
        self.clock.tick(50)
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    pass

            elif event.type == pygame.MOUSEMOTION:
                pass

    def run(self):

        global mainloop
        mainloop = True
        while mainloop:

            self.screen.blit(self.background, (0, 0))

            self.checkEvents()

            pygame.display.flip()
