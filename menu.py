import pygame
import utils

Utils = utils.Utils()


class Menu():
    def __init__(self, screen, active_char=None):

        font = 'font/BEBAS.ttf'
        font_size = 35
        font_name_size = 40
        font_color = (255, 255, 255)

        self.screen = screen
        self.surface = pygame.Surface((400, 250), pygame.SRCALPHA, 32)
        self.charsurface = pygame.Surface((130, 260))
        self.scr_width = self.surface.get_rect().width
        self.scr_height = self.surface.get_rect().height

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(font, font_size)

        self.activename_font = pygame.font.Font(font, 20)

        self.mo_sound = pygame.mixer.Sound('sounds/mouse_over.ogg')
        self.mouse_click = pygame.mixer.Sound('sounds/click.ogg')

        self.name_font = pygame.font.Font(font, font_name_size)
        self.font_color = font_color
        self.active_font = pygame.font.Font(font, 18)
        self.items = []
        self.buttons = ['New     Char', 'Change     Char',
                        'Join      Game', 'Host      Game']

        self.background = pygame.image.load('sprites/menu_BG.jpg')
        self.active_char = active_char

        for index, item in enumerate(self.buttons):
            label = self.font.render(item, 1, font_color)
            mo_label = self.font.render(item, 1, (23, 92, 207))

            width = label.get_rect().width
            height = label.get_rect().height

            posx = (self.scr_width / 2) - (width / 2)
            # t_h: total height of text block
            t_h = len(self.buttons) * height
            posy = (self.scr_height / 2) - (t_h / 2) + (index * height) - 5

            self.items.append(
                [item, label, (width, height), (posx, posy), mo_label])

    def checkEvents(self, button, posx, posy):
        global mainloop
        self.clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = Utils.getMousePosition(-posx, -posy)

                for i in range(len(button)):
                    if button[i].collidepoint(mouse_pos):
                        self.mouse_click.play(0)

                        mainloop = False
                        return (i)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

            if event.type == pygame.QUIT:
                quit()

    def printActive(self, text, pos_x, pos_y):
        text = self.active_font.render(text, True, (250, 250, 250))
        self.charsurface.blit(text, (pos_x, pos_y))

    def activeChar(self):
        self.name_bg = pygame.Surface((110, 30), pygame.SRCALPHA, 32)
        self.name_bg.fill((0, 0, 0, 150))

        self.activeface = pygame.image.load(
            'sprites/char_face/' + self.active_char[7])

        self.charsurface.blit(self.activeface, (10, 10))
        self.charsurface.blit(self.name_bg, (10, 90))

        # Name
        text = self.activename_font.render(
            self.active_char[0], True, (250, 250, 250))
        self.charsurface.blit(text, (15, 90))

        active_stats = eval(self.active_char[3])

        for i in range(len(active_stats)):
            active_stats[i] = str(active_stats[i])
        # Stats
        s = ('HP:     ' + self.active_char[1])
        self.printActive(s, 10, 120)
        s = ('MP:     ' + self.active_char[2])
        self.printActive(s, 10, 140)
        s = (': ' + active_stats[0])
        self.printActive(s, 35, 170)
        s = (': ' + active_stats[1])
        self.printActive(s, 35, 190)
        s = (': ' + active_stats[2])
        self.printActive(s, 35, 210)
        s = (': ' + active_stats[3])
        self.printActive(s, 35, 230)
        s = (': ' + active_stats[4])
        self.printActive(s, 95, 180)
        s = (': ' + active_stats[5])
        self.printActive(s, 95, 200)
        s = (': ' + active_stats[6])
        self.printActive(s, 95, 220)

        self.screen.blit(self.charsurface, (20, 200))

    def run(self):
        global mainloop
        mainloop = True
        last_button = None
        pygame.mixer.music.load('sounds/menu.ogg')
        pygame.mixer.music.play(-1)
        while mainloop:
            self.screen.blit(self.background, (0, 0))
            self.surface.fill((0, 0, 0, 150))

            self.charsurface.fill((0, 0, 0, 150))

            self.charsurface = self.charsurface.convert_alpha()

            button = []
            i = 0

            position_x = self.scr_width / 2
            position_y = self.scr_height / 2 + 200

            mouse_pos = Utils.getMousePosition(-position_x, -position_y)
            # Draw buttons
            for name, label, (width, height), (posx, posy), mo_label in self.items:
                button.append(pygame.Rect(
                    posx, posy + (5 * i), width, height))

                if button[i].collidepoint(mouse_pos):
                    if not last_button == i:
                        last_button = i
                        self.mo_sound.play(0)
                    self.surface.blit(mo_label, (posx, posy + (5 * i)))
                else:
                    self.surface.blit(label, (posx, posy + (5 * i)))
                i += 1

            self.surface = self.surface.convert_alpha()

            self.screen.blit(self.surface, (position_x, position_y))

            choice = self.checkEvents(button, position_x, position_y)

            if self.active_char:
                self.activeChar()

            if choice is not None:

                return (choice)

            pygame.display.flip()
