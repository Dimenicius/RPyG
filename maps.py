import pygame
import utils
import map_icon

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

        self.left0 = pygame.image.load('sprites/map/cngImgleft0.png')
        self.left1 = pygame.image.load('sprites/map/cngImgleft1.png')
        self.right0 = pygame.image.load('sprites/map/cngImgright0.png')
        self.right1 = pygame.image.load('sprites/map/cngImgright1.png')

        self.X = pygame.image.load('sprites/map/X.png')

        self.cngIMG = pygame.mixer.Sound('sounds/click2.ogg')
        self.create = pygame.mixer.Sound('sounds/create.ogg')
        self.drop = pygame.mixer.Sound('sounds/drop.ogg')
        self.pick = pygame.mixer.Sound('sounds/pick.ogg')

        self.mapPos = [0, 0]
        self.icons = []
        self.cld_icon = None

    def checkEvents(self):
        global mainloop
        self.clock.tick(50)
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    if self.cld_icon is not None:
                        mouse_pos = Utils.getMousePosition(
                            -self.mapPos[0], -self.mapPos[1])

                        if self.icons[self.cld_icon].left.collidepoint(mouse_pos):
                            self.cngIMG.play(0)
                            self.icons[self.cld_icon].changeImg(-1)
                        elif self.icons[self.cld_icon].right.collidepoint(mouse_pos):
                            self.cngIMG.play(0)
                            self.icons[self.cld_icon].changeImg(1)

                    for i in range(len(self.icons)):
                        mouse_pos = [0, 0]
                        mouse_pos[0] = event.pos[0] - self.mapPos[0]
                        mouse_pos[1] = event.pos[1] - self.mapPos[1]

                        if self.icons[i].rect.collidepoint(mouse_pos):
                            self.pick.play(0)
                            # icon_click = True
                            self.cld_icon = i
                            mouse_x, mouse_y = event.pos
                            self.offset_x = self.icons[i].position[0] - mouse_x
                            self.offset_y = self.icons[i].position[1] - mouse_y

                            self.drag_icon = True

                    if not self.drag_icon:
                        mouse_x, mouse_y = event.pos
                        self.offset_x = self.mapPos[0] - mouse_x
                        self.offset_y = self.mapPos[1] - mouse_y
                        self.drag_map = True

                elif event.button == 3:
                    self.create.play(0)
                    icon_position = [
                        event.pos[0] - self.mapPos[0] - 25, event.pos[1] - self.mapPos[1] - 25]
                    self.icons.append(map_icon.Icon(icon_position))
                    self.cld_icon = len(self.icons) - 1

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.drag_map = False
                    if self.drag_icon:
                        self.drop.play(0)
                        self.icons[self.cld_icon].updateRect()
                        self.drag_icon = False

            elif event.type == pygame.MOUSEMOTION:
                if self.drag_map is True:
                    mouse_x, mouse_y = event.pos
                    self.mapPos[0] = mouse_x + self.offset_x
                    self.mapPos[1] = mouse_y + self.offset_y

                    for i in range(2):
                        if self.mapPos[i] > 0:
                            self.mapPos[i] = 0

                    if self.mapPos[0] < 800 - self.background.get_width():
                        self.mapPos[0] = 800 - self.background.get_width()

                    if self.mapPos[1] < 600 - self.background.get_height():
                        self.mapPos[1] = 600 - self.background.get_height()

                elif self.drag_icon is True:
                    for i in range(len(self.icons)):
                        mouse_x, mouse_y = event.pos
                        self.icons[self.cld_icon].position[0] = mouse_x + \
                            self.offset_x
                        self.icons[self.cld_icon].position[1] = mouse_y + \
                            self.offset_y

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False

                if self.cld_icon is not None:
                    if event.key >= 97 and event.key <= 122:
                        if len(self.icons[self.cld_icon].name) <= 20:
                            letter = chr(event.key)
                            if len(self.icons[self.cld_icon].name) == 0:
                                letter = letter.upper()
                            self.icons[self.cld_icon].name = self.icons[self.cld_icon].name + letter

                    elif event.key == pygame.K_SPACE:
                        self.icons[self.cld_icon].name = self.icons[self.cld_icon].name + ' '
                    elif event.key == pygame.K_BACKSPACE:
                        self.icons[self.cld_icon].name = self.icons[self.cld_icon].name[:-1]

            if event.type == pygame.QUIT:
                quit()

    def showIconInfo(self, icon):
        text = self.icon_font.render(
            icon.name, True, (250, 250, 250))
        if len(icon.name) > 0:
            Utils.drawSquare(
                text.get_width() + 10, 30, icon.position[0] + 55 + self.mapPos[0], icon.position[1] + self.mapPos[1], self.screen)

        self.screen.blit(
            text, (icon.position[0] + 60 + self.mapPos[0],
                   icon.position[1] + self.mapPos[1]))

    def modifyIcon(self, icon):
        self.screen.blit(self.left0, (icon.left.x +
                                      self.mapPos[0], icon.left.y + self.mapPos[1]))
        self.screen.blit(self.right0, (icon.right.x +
                                       self.mapPos[0], icon.right.y + self.mapPos[1]))

    def run(self):

        global mainloop
        mainloop = True
        self.drag_map = False
        self.drag_icon = False
        while mainloop:

            self.screen.blit(self.background, self.mapPos)

            for i in range(len(self.icons)):
                self.screen.blit(
                    self.icons[i].imgFile, (self.icons[i].position[0] + self.mapPos[0], self.icons[i].position[1] + self.mapPos[1]))
                self.showIconInfo(self.icons[i])

            if self.cld_icon is not None and self.drag_icon is False and self.drag_map is False:
                self.modifyIcon(self.icons[self.cld_icon])

            self.checkEvents()

            pygame.display.flip()
