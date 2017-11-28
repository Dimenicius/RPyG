import pygame
import skills
import utils
import items
import player as playerObj

Utils = utils.Utils()


class CharModification():
    def __init__(self, screen, points=0, stats=None, charlist=None, active_char=None, modify=0, Master=False, active_chars=None, charmod=None, ShowInv=False):
        bg_color = (0, 0, 0)
        font = 'font/BEBAS.ttf'
        font_size = 20
        font_name_size = 25
        font_color = (255, 255, 255)

        self.screen = screen
        self.imgFiles = Utils.getFiles('sprites/chars/')

        self.cld_icon = None

        self.charlist = charlist
        self.active_chars = active_chars

        self.master = Master

        self.modify = modify

        self.skillImg = []
        self.invItems = []
        self.equipslots_rects = []

        self.surf_width = 350
        self.surf_height = 550

        self.scr_width, self.scr_height = self.screen.get_size()

        self.bg_color = bg_color
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(font, font_size)
        self.name_font = pygame.font.Font(font, font_name_size)
        self.font_color = font_color

        self.smallFont = pygame.font.Font('font/Amiko-Regular.ttf', 10)
        self.smallTitle = pygame.font.Font('font/Amiko-Bold.ttf', 12)
        self.activePlayer = None
        self.items = []
        self.attribs = []
        self.pointsleft = points

        self.skillTab_show = 0

        self.showInv = ShowInv

        if self.charlist:
            if self.modify:
                self.showSkills = True
            else:
                self.showSkills = False
        elif self.showInv:
            self.showSkills = False
        else:
            self.showSkills = True

        self.skillsObj = skills.Skills()

        self.skills = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

        if self.active_chars:

            if active_char is None:
                self.currchar = 0
            else:
                self.currchar = active_char

            self.activePlayer = active_chars[0]

            self.reloadPlayer()

        else:
            if charlist is None and self.modify == 0:
                self.name = ''
                self.stat = stats
                self.skillsleft = 3
                self.img = self.imgFiles[0]
                self.equips = ['empty', 'empty', 'empty', 'empty', 'empty']

                self.playermoney = 0
                self.exp = 0
                if Utils.getLastID('databases/inventorys'):
                    self.invID = int(Utils.getLastID(
                        'databases/inventorys')) + 1
                else:
                    self.invID = 0

            else:

                if active_char is None:
                    self.currchar = 0
                else:
                    self.currchar = active_char

                self.activePlayer = charmod  # playerObj.Player(self.currchar)

                self.reloadPlayer()

        self.reloadStats()
        self.reloadSkills()
        if self.activePlayer:
            self.reloadInv()

        self.imgIndex = self.imgFiles.index(self.img)
        self.loadImages()

        self.createStatNames()

    def getInv(self, Inv_ID):
        result = Utils.getByID('databases/inventorys',
                               Utils.getIDPos('databases/inventorys', Inv_ID))

        return(eval(result[1]))

    def reloadStats(self):
        self.initStats = []
        if self.master:
            for i in range(len(self.stat)):
                self.initStats.append(0)
        else:
            for i in range(len(self.stat)):
                self.initStats.append(int(self.stat[i]))

    def reloadSkills(self):
        self.initSkills = []
        if self.master:
            for i in range(len(self.skills)):
                self.initSkills.append([])
                for j in range(len(self.skills[i])):
                    self.initSkills[i].append(0)
        else:
            for i in range(len(self.skills)):
                self.initSkills.append([])
                for j in range(len(self.skills[i])):
                    self.initSkills[i].append(self.skills[i][j])

    def resolvePlayer(self):
        self.activePlayer.name = self.name
        self.activePlayer.stat = self.stat
        self.activePlayer.skills = self.skills

        self.activePlayer.statLeft = self.pointsleft
        self.activePlayer.skillLeft = self.skillsleft

        self.activePlayer.img = self.img
        self.activePlayer.equips = self.equips

        self.activePlayer.money = self.playermoney

    def reloadInv(self):
        self.invItems = []
        self.invID = self.activePlayer.IID
        self.inventory = self.getInv(self.invID)

        for index, item in enumerate(self.inventory):
            position = [index % 4 * 65 + 75, int(index / 4) * 65 + 145]
            self.invItems.append(items.Item(item, position))

    def reloadPlayer(self):
        self.name = self.activePlayer.name
        self.stat = self.activePlayer.stat
        self.skills = self.activePlayer.skills
        if self.master:
            self.pointsleft_temp = int(self.activePlayer.statLeft)
            self.skillsleft_temp = int(self.activePlayer.skillLeft)
            self.pointsleft = 100
            self.skillsleft = 100
        else:
            self.pointsleft = int(self.activePlayer.statLeft)
            self.skillsleft = int(self.activePlayer.skillLeft)
        self.img = self.activePlayer.img
        self.equips = self.activePlayer.equips

        self.playermoney = self.activePlayer.money
        self.exp = self.activePlayer.exp

        self.char_img = pygame.image.load('sprites/chars/' + self.img)

        self.reloadStats()
        self.reloadSkills()

    def createStatNames(self):
        items = ('Strength:', 'Polymorph:', 'Endurance:',
                 'Charisma:', 'Inteligence:', 'Agility:', 'Love:')

        for index, item in enumerate(items):
            label = self.font.render(item, 1, self.font_color)

            width = label.get_rect().width - 20
            height = label.get_rect().height + 12

            posx = (self.surf_width / 4) - (width / 2) + 25

            t_h = len(items) * height
            posy = (self.surf_height / 2) - (t_h / 2) + (index * height) + 55

            self.items.append(
                [item, label, (width, height), (posx, posy)])

    def loadImages(self):
        self.background = pygame.image.load(
            'sprites/create_char/background.png')
        self.accept0 = pygame.image.load(
            'sprites/create_char/finish_button0.png')
        self.accept1 = pygame.image.load(
            'sprites/create_char/finish_button1.png')
        self.cancel0 = pygame.image.load(
            'sprites/create_char/cancel_button0.png')
        self.cancel1 = pygame.image.load(
            'sprites/create_char/cancel_button1.png')

        self.stat_min = pygame.image.load(
            'sprites/create_char/min_button.png')
        self.stat_max = pygame.image.load(
            'sprites/create_char/max_button.png')

        self.stat_min1 = pygame.image.load(
            'sprites/create_char/min_button1.png')
        self.stat_max1 = pygame.image.load(
            'sprites/create_char/max_button1.png')

        self.left0 = pygame.image.load(
            'sprites/create_char/arrow_left0.png')
        self.left1 = pygame.image.load(
            'sprites/create_char/arrow_left1.png')
        self.right0 = pygame.image.load(
            'sprites/create_char/arrow_right0.png')
        self.right1 = pygame.image.load(
            'sprites/create_char/arrow_right1.png')

        self.char_img = pygame.image.load('sprites/chars/' + self.img)

        self.cngChar_left0 = pygame.image.load(
            'sprites/create_char/cngChar_left0.png')
        self.cngChar_left1 = pygame.image.load(
            'sprites/create_char/cngChar_left1.png')
        self.cngChar_right0 = pygame.image.load(
            'sprites/create_char/cngChar_right0.png')
        self.cngChar_right1 = pygame.image.load(
            'sprites/create_char/cngChar_right1.png')

        self.brain0 = pygame.image.load(
            'sprites/create_char/icons/brain_0.png')
        self.brain1 = pygame.image.load(
            'sprites/create_char/icons/brain_1.png')
        self.brain2 = pygame.image.load(
            'sprites/create_char/icons/brain_2.png')

        self.equip0 = pygame.image.load(
            'sprites/create_char/icons/equip_0.png')
        self.equip1 = pygame.image.load(
            'sprites/create_char/icons/equip_1.png')
        self.equip2 = pygame.image.load(
            'sprites/create_char/icons/equip_2.png')

        self.inv0 = pygame.image.load(
            'sprites/create_char/icons/inv0.png')
        self.inv1 = pygame.image.load(
            'sprites/create_char/icons/inv1.png')
        self.inv2 = pygame.image.load(
            'sprites/create_char/icons/inv2.png')

        self.idcard0 = pygame.image.load(
            'sprites/create_char/icons/id-card0.png')
        self.idcard1 = pygame.image.load(
            'sprites/create_char/icons/id-card1.png')
        self.idcard2 = pygame.image.load(
            'sprites/create_char/icons/id-card2.png')

        self.money = pygame.image.load(
            'sprites/create_char/icons/money.png')

        self.emptySlot = ['pendant.png', 'hand.png',
                          'hand.png', 'armor.png', 'boot.png']

        self.refreshEquipsIMG()
        self.equip_change = pygame.image.load(
            'sprites/create_char/equip_change.png')

        self.S_img = pygame.image.load(
            'sprites/create_char/icons/biceps.png')
        self.P_img = pygame.image.load(
            'sprites/create_char/icons/binoculars.png')
        self.E_img = pygame.image.load(
            'sprites/create_char/icons/mailed-fist.png')
        self.C_img = pygame.image.load(
            'sprites/create_char/icons/baby-face.png')
        self.I_img = pygame.image.load(
            'sprites/create_char/icons/fairy-wand.png')
        self.A_img = pygame.image.load(
            'sprites/create_char/icons/jump-across.png')
        self.L_img = pygame.image.load(
            'sprites/create_char/icons/heart-wings.png')

        self.activeSkillTab = []
        self.activeSkillTab.append(pygame.image.load(
            'sprites/create_char/icons/biceps1.png'))
        self.activeSkillTab.append(pygame.image.load(
            'sprites/create_char/icons/binoculars1.png'))
        self.activeSkillTab.append(pygame.image.load(
            'sprites/create_char/icons/mailed-fist1.png'))
        self.activeSkillTab.append(pygame.image.load(
            'sprites/create_char/icons/baby-face1.png'))
        self.activeSkillTab.append(pygame.image.load(
            'sprites/create_char/icons/fairy-wand1.png'))
        self.activeSkillTab.append(pygame.image.load(
            'sprites/create_char/icons/jump-across1.png'))
        self.activeSkillTab.append(pygame.image.load(
            'sprites/create_char/icons/heart-wings1.png'))

        self.arrow_up = pygame.image.load(
            'sprites/create_char/icons/arrow_up.png')
        self.arrow_down = pygame.image.load(
            'sprites/create_char/icons/arrow_down.png')
        self.arrow_up1 = pygame.image.load(
            'sprites/create_char/icons/arrow_up1.png')
        self.arrow_down1 = pygame.image.load(
            'sprites/create_char/icons/arrow_down1.png')

    def refreshEquipsIMG(self):
        self.equipIMG = []
        for i in range(len(self.equips)):
            self.equipIMG.append('')

        for i in range(len(self.equips)):
            if self.equips[i] == 'empty':
                self.equipIMG[i] = pygame.image.load(
                    'sprites/create_char/icons/' + self.emptySlot[i])
            else:

                item = Utils.getByID(
                    'databases/items', Utils.getIDPos('databases/items', self.equips[i]))
                self.equipIMG[i] = pygame.image.load(
                    'sprites/items/' + item[6])

    def changeImgButtons(self):

        left_pos = (500, 400)
        right_pos = (670, 400)

        if not self.showSkills:
            if self.charlist is None or self.modify == 1:
                next_img = pygame.Rect(right_pos[0], right_pos[1], 40, 40)
                prev_img = pygame.Rect(left_pos[0], left_pos[1], 40, 40)

                mouse_pos = Utils.getMousePosition(0, 0)
                if next_img.collidepoint(mouse_pos):
                    self.screen.blit(self.cngChar_right1, right_pos)
                else:
                    self.screen.blit(self.cngChar_right0, right_pos)

                if prev_img.collidepoint(mouse_pos):
                    self.screen.blit(self.cngChar_left1, left_pos)
                else:
                    self.screen.blit(self.cngChar_left0, left_pos)
            else:
                next_img = pygame.Rect(
                    self.scr_width, self.scr_height, 40, 40)
                prev_img = pygame.Rect(
                    self.scr_width, self.scr_height, 40, 40)
        else:
            next_img = pygame.Rect(
                self.scr_width, self.scr_height, 40, 40)
            prev_img = pygame.Rect(
                self.scr_width, self.scr_height, 40, 40)

        return (next_img, prev_img)

    def changeImg(self, qty):
        self.imgIndex += qty

        if self.imgIndex == len(self.imgFiles):
            self.imgIndex = 0
        elif self.imgIndex < 0:
            self.imgIndex = len(self.imgFiles) - 1

        self.reloadCharImg(self.imgIndex)

    def reloadCharImg(self, index):
        self.img = self.imgFiles[index]
        self.char_img = pygame.image.load('sprites/chars/' + self.img)

    def reloadCharImg_name(self, name):
        self.char_img = pygame.image.load('sprites/chars/' + name)

    def statValues(self):
        # Draw stats
        if self.charlist and self.modify == 0:
            self.stat = self.activePlayer.stat

        for index, item in enumerate(self.stat):
            label = self.font.render(str(item), 1, self.font_color)

            width = label.get_rect().width
            height = label.get_rect().height + 12

            posx = (self.surf_width / 4) - (width / 2) + 185
            # t_h: total height of text block
            t_h = len(self.stat) * height
            posy = (self.surf_height / 2) - \
                (t_h / 2) + (index * height) + 55

            self.attribs.append(
                [item, label, (width, height), (posx, posy)])

    def drawButtons(self, button):
        for index, values in enumerate(self.attribs):
            name, label, (width, height), (posx, posy) = values
            self.screen.blit(label, (posx, posy))

            # Draw buttons
            for i in range(2):
                if i == 0:

                    if int(name) > int(self.initStats[index]):
                        if self.charlist is None or self.modify == 1:
                            self.drawStatButton(
                                button, 225 + i * 75, posy + 5, i)
                        else:
                            self.drawStatButton(
                                button, self.scr_width, self.scr_height, i)
                    else:
                        self.drawStatButton(
                            button, self.scr_width, self.scr_height, i)
                elif self.pointsleft > 0:
                    self.drawStatButton(button, 225 + i * 75, posy + 5, i)
                else:
                    self.drawStatButton(
                        button, self.scr_width, self.scr_height, i)

    def drawStatButton(self, button, pos_x, pos_y, b_type):
        button.append(pygame.Rect(pos_x, pos_y, 20, 20))
        mouse_pos = Utils.getMousePosition(0, 0)

        if b_type == 1:
            if button[len(button) - 1].collidepoint(mouse_pos):
                self.screen.blit(self.stat_max1, (pos_x - 5, pos_y - 5))
            else:
                self.screen.blit(self.stat_max, (pos_x - 5, pos_y - 5))
        else:
            if button[len(button) - 1].collidepoint(mouse_pos):
                self.screen.blit(self.stat_min1, (pos_x - 5, pos_y - 5))
            else:
                self.screen.blit(self.stat_min, (pos_x - 5, pos_y - 5))

    def drawStats(self):
        # Draw stat names
        for name, label, (width, height), (posx, posy) in self.items:
            self.screen.blit(label, (posx, posy))

    def drawConfirmation(self):
        # Draw confirmation buttons
        if self.charlist or self.modify == 1 or self.master:
            accept = pygame.Rect(485, 485, 240, 40)
        elif self.pointsleft == 0 and len(self.name) > 0 and self.skillsleft == 0:
            accept = pygame.Rect(485, 485, 240, 40)
        else:
            accept = pygame.Rect(
                self.scr_width, self.scr_height, 60, 20)

        cancel = pygame.Rect(80, 485, 240, 40)

        return(accept, cancel)

    def drawTexts(self):

        if self.showInv or self.modify == 1:
            pass
        else:
            # Draw  points left
            text = self.font.render(
                'Name:', True, (250, 250, 250))
            self.screen.blit(text, (55, 90))

            # Draw name
            Utils.drawSquare(220, 40, 115, 85, self.screen)

            if not self.charlist:
                text = self.name_font.render(
                    self.name, True, (250, 250, 250))
            else:
                text = self.name_font.render(
                    self.activePlayer.name, True, (250, 250, 250))

            if not self.charlist and not self.showInv:
                self.drawCursor(text.get_rect().width, self.screen)

            self.screen.blit(text, (120, 85))

        # Draw  points left
        if not self.showInv:
            text = self.name_font.render(
                'Stats     left: ' + str(self.pointsleft), True, (250, 250, 250))
            self.screen.blit(text, (115, 135))

    def drawSkills(self, activeTab, button):
        if self.charlist:
            if not self.modify:
                self.skills = self.activePlayer.skills

        pos_y = 175
        pos_x = 465

        Utils.drawSquare(45, 40, pos_x, pos_y + 43 *
                         activeTab, self.screen)
        Utils.drawSquare(230, 298, pos_x + 45, pos_y, self.screen)

        self.drawIcons()

        self.screen.blit(
            self.activeSkillTab[activeTab], (pos_x, pos_y + 43 * activeTab))

        for i in range(5):
            self.screen.blit(
                self.skillsObj.skillImg[activeTab][i], (pos_x + 50, pos_y + 5 + (i * 59)))

            if (int(self.stat[activeTab]) - 5) / 2 > i:
                color = (250, 0, 0)
                if not self.charlist or self.modify:
                    if self.skillsleft > 0:
                        self.skillArrows(button, pos_x + 255,
                                         pos_y + 5 + (i * 59), activeTab, i, 1)
                    else:
                        self.skillArrows(button, self.scr_width,
                                         self.scr_height, activeTab, i, 1)
                    if int(self.skills[activeTab][i]) > int(self.initSkills[activeTab][i]):
                        self.skillArrows(button, pos_x + 255,
                                         pos_y + 33 + (i * 59), activeTab, i, 0)
                    else:
                        self.skillArrows(button, self.scr_width,
                                         self.scr_height, activeTab, i, 0)

            else:
                color = (100, 100, 100)
                Utils.drawSquare(50, 50, pos_x + 50, pos_y +
                                 5 + (i * 59), self.screen)

            text = self.name_font.render(
                str(self.skills[activeTab][i]), True, color)
            self.screen.blit(text, (pos_x + 90, pos_y + 30 + (i * 59)))

            # SKILL TEXTS
            self.skillTexts(activeTab, i, pos_x, pos_y)

        text = self.name_font.render(
            'Skill     points: ' + str(self.skillsleft), True, (250, 250, 250))
        self.screen.blit(text, (515, 135))

    def drawIcons(self):
        self.tabs = []
        self.skillTabButton(465, 150 + 25, self.S_img)
        self.skillTabButton(465, 193 + 25, self.P_img)
        self.skillTabButton(465, 236 + 25, self.E_img)
        self.skillTabButton(465, 279 + 25, self.C_img)
        self.skillTabButton(465, 322 + 25, self.I_img)
        self.skillTabButton(465, 365 + 25, self.A_img)
        self.skillTabButton(465, 408 + 25, self.L_img)

    def skillTabButton(self, pos_x, pos_y, image):
        self.screen.blit(image, (pos_x, pos_y))
        self.tabs.append(pygame.Rect(pos_x, pos_y, 40, 40))

    def skillArrows(self, button, pos_x, pos_y, activeTab, i, arrow_type):
        button.append(pygame.Rect(pos_x, pos_y, 22, 25))

        mouse_pos = Utils.getMousePosition(0, 0)

        if self.skillsleft > 0:
            if button[len(button) - 1].collidepoint(mouse_pos):
                self.skillUp(pos_x, pos_y, arrow_type, True)
            else:
                self.skillUp(pos_x, pos_y, arrow_type)
        if int(self.skills[activeTab][i]) > 0:
            if button[len(button) - 1].collidepoint(mouse_pos):
                self.skillUp(pos_x, pos_y, arrow_type, True)
            else:
                self.skillUp(pos_x, pos_y, arrow_type)

    def skillUp(self, pos_x, pos_y, arrow_type, on=False):
        if arrow_type == 1:
            if on:
                self.screen.blit(self.arrow_up1, (pos_x, pos_y))
            else:
                self.screen.blit(self.arrow_up, (pos_x, pos_y))
        else:
            if on:
                self.screen.blit(self.arrow_down1, (pos_x, pos_y))
            else:
                self.screen.blit(self.arrow_down, (pos_x, pos_y))

    def skillTexts(self, activeTab, i, pos_x, pos_y):
        for j in range(4):
            if j == 3:
                color = (250, 210, 0)
            else:
                color = (250, 250, 250)

            if j == 0:
                text = self.smallTitle.render(
                    self.skillsObj.skillDesc[activeTab][i][j], True, (68, 152, 231))
            else:
                text = self.smallFont.render(
                    self.skillsObj.skillDesc[activeTab][i][j], True, color)

            self.screen.blit(
                text, (pos_x + 105, pos_y + 5 + (i * 59) + j * 14))

    def drawVisual(self):
        self.charvisual = pygame.Surface((200, 300), pygame.SRCALPHA, 32)
        self.charvisual.fill((0, 0, 0, 100))

        self.charvisual.blit(self.char_img, (0, 0))

        self.screen.blit(self.charvisual, (505, 145))

        self.equipslots_rects = []

        if self.modify:
            self.drawItemSlot(250, 160, self.equipIMG[0])  # amulet

            self.drawItemSlot(250, 240, self.equipIMG[1])

            self.drawItemSlot(50, 240, pygame.transform.flip(
                self.equipIMG[2], True, False))  # hands

            self.drawItemSlot(50, 320, self.equipIMG[3])  # armor
            self.drawItemSlot(250, 320, self.equipIMG[4])

        if self.drag_item is True and self.invItems[self.cld_icon].type == '0':
            self.equipColliders = self.equipCollider()

        # for item in self.equipslots_rects:
        #     pygame.draw.rect(self.screen, (255, 255, 255), item)

    def equipCollider(self):
        colliders = []

        if self.invItems[self.cld_icon].slot == '0':
            colliders.append(pygame.Rect(675, 185, 60, 60))
        elif self.invItems[self.cld_icon].slot == '1' or self.invItems[self.cld_icon].slot == '2':
            colliders.append(pygame.Rect(675, 265, 60, 60))
            colliders.append(pygame.Rect(475, 265, 60, 60))
        elif self.invItems[self.cld_icon].slot == '3':
            colliders.append(pygame.Rect(475, 345, 60, 60))
        elif self.invItems[self.cld_icon].slot == '4':
            colliders.append(pygame.Rect(675, 345, 60, 60))

        for i in range(len(colliders)):
            self.screen.blit(self.equip_change,
                             (colliders[i].left, colliders[i].top))
        return(colliders)

    def drawItemSlot(self, pos_x, pos_y, image):
        Utils.drawSquare(60, 60, pos_x + 425, pos_y + 25, self.screen)
        self.screen.blit(image, (pos_x + 425, pos_y + 25))
        self.equipslots_rects.append(
            pygame.Rect(pos_x + 425, pos_y + 25, 60, 60))

    def manageSkill(self, stat, atribute):
        op = stat % 2
        attrib = int(stat / 2)
        if op == 0:
            self.skills[atribute][attrib] += 1
            self.skillsleft -= 1
        else:
            self.skills[atribute][attrib] -= 1
            self.skillsleft += 1

    def drawCursor(self, pos_x, surface):
        if len(self.name) <= 10:
            self.sqrSurf = pygame.Surface((3, 30))
            self.sqrSurf.fill((255, 255, 255))
            surface.blit(self.sqrSurf, (120 + pos_x, 88))

    def rightTabs(self):

        left_pos = (520, 70)
        right_pos = (630, 70)

        mouse_pos = Utils.getMousePosition(0, 0)

        visual = pygame.Rect(right_pos[0], right_pos[1], 80, 50)
        skills = pygame.Rect(left_pos[0], left_pos[1], 80, 50)
        if self.showSkills:
            self.screen.blit(self.brain0, left_pos)
            if visual.collidepoint(mouse_pos):
                self.screen.blit(self.equip2, right_pos)
            else:
                self.screen.blit(self.equip1, right_pos)
        else:
            self.screen.blit(self.equip0, right_pos)
            if skills.collidepoint(mouse_pos):
                self.screen.blit(self.brain2, left_pos)
            else:
                self.screen.blit(self.brain1, left_pos)

        return (skills, visual)

    def leftTabs(self):
        if self.modify:
            left_pos = (120, 70)
            right_pos = (230, 70)

            mouse_pos = Utils.getMousePosition(0, 0)

            inv = pygame.Rect(right_pos[0], right_pos[1], 80, 50)
            idcard = pygame.Rect(left_pos[0], left_pos[1], 80, 50)

            if self.showInv:
                self.screen.blit(self.inv0, right_pos)
                if idcard.collidepoint(mouse_pos):
                    self.screen.blit(self.idcard2, left_pos)
                else:
                    self.screen.blit(self.idcard1, left_pos)
            else:
                self.screen.blit(self.idcard0, left_pos)
                if inv.collidepoint(mouse_pos):
                    self.screen.blit(self.inv2, right_pos)
                else:
                    self.screen.blit(self.inv1, right_pos)

        else:
            idcard = pygame.Rect(self.scr_width, self.scr_height, 80, 50)
            inv = pygame.Rect(self.scr_width, self.scr_height, 80, 50)

        return (idcard, inv)

    def changeButtons(self):

        left_pos = (10, 250)
        right_pos = (755, 250)

        mouse_pos = Utils.getMousePosition(0, 0)
        # Draw change char buttons
        if self.modify:
            prev_char = pygame.Rect(
                self.scr_width, self.scr_height, 40, 50)
            next_char = pygame.Rect(
                self.scr_width, self.scr_height, 40, 50)
        elif self.charlist:
            if self.currchar < len(self.charlist) - 1:
                next_char = pygame.Rect(right_pos[0], right_pos[1], 40, 50)
                if next_char.collidepoint(mouse_pos):
                    self.screen.blit(self.right1, right_pos)
                else:
                    self.screen.blit(self.right0, right_pos)

            else:
                next_char = pygame.Rect(
                    self.scr_width, self.scr_height, 40, 50)

            if self.currchar == 0:
                prev_char = pygame.Rect(
                    self.scr_width, self.scr_height, 40, 50)
            else:
                prev_char = pygame.Rect(left_pos[0], left_pos[1], 40, 50)
                if prev_char.collidepoint(mouse_pos):
                    self.screen.blit(self.left1, left_pos)
                else:
                    self.screen.blit(self.left0, left_pos)

        elif self.active_chars:

            if self.currchar < len(self.active_chars) - 1:
                next_char = pygame.Rect(right_pos[0], right_pos[1], 40, 50)
                if next_char.collidepoint(mouse_pos):
                    self.screen.blit(self.right1, right_pos)
                else:
                    self.screen.blit(self.right0, right_pos)
            else:
                next_char = pygame.Rect(
                    self.scr_width, self.scr_height, 40, 50)

            if self.currchar == 0:
                prev_char = pygame.Rect(
                    self.scr_width, self.scr_height, 40, 50)
            else:
                prev_char = pygame.Rect(left_pos[0], left_pos[1], 40, 50)
                if prev_char.collidepoint(mouse_pos):
                    self.screen.blit(self.left1, left_pos)
                else:
                    self.screen.blit(self.left0, left_pos)

        else:
            prev_char = pygame.Rect(
                self.scr_width, self.scr_height, 40, 50)
            next_char = pygame.Rect(
                self.scr_width, self.scr_height, 40, 50)

        return (prev_char, next_char)

    def checkEvents(self, button, accept, cancel, prev_char, next_char, skills, visual, prev_img, next_img, idcard, inv):
        global mainloop

        # Limit frame speed to 50 FPS
        self.clock.tick(50)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = Utils.getMousePosition(0, 0)

                if prev_char.collidepoint(mouse_pos):
                    self.currchar = self.currchar - 1
                    if self.active_chars:
                        self.activePlayer = self.active_chars[
                            self.currchar % (len(self.active_chars))]
                    else:
                        self.activePlayer = playerObj.Player(self.currchar)

                    self.reloadPlayer()

                    self.equips = self.activePlayer.equips
                    self.reloadCharImg_name(self.activePlayer.img)
                    self.refreshEquipsIMG()

                elif next_char.collidepoint(mouse_pos):
                    self.currchar = self.currchar + 1
                    if self.active_chars:
                        self.activePlayer = self.active_chars[
                            self.currchar % (len(self.active_chars))]
                    else:
                        self.activePlayer = playerObj.Player(self.currchar)

                    self.reloadPlayer()

                    self.equips = self.activePlayer.equips
                    self.reloadCharImg_name(self.activePlayer.img)
                    self.refreshEquipsIMG()

                elif skills.collidepoint(mouse_pos):
                    self.showSkills = True
                    break
                elif visual.collidepoint(mouse_pos):
                    self.showSkills = False
                    break
                elif inv.collidepoint(mouse_pos):
                    self.showInv = True
                    break
                elif idcard.collidepoint(mouse_pos):
                    self.showInv = False
                    break
                elif next_img.collidepoint(mouse_pos):
                    self.changeImg(1)
                elif prev_img.collidepoint(mouse_pos):
                    self.changeImg(-1)

                for i in range(len(button)):
                    if button[i].collidepoint(mouse_pos):
                        self.activateButton(i)

                for index, item in enumerate(self.invItems):
                    if item.rect.collidepoint(mouse_pos) and self.drag_item is False:
                        self.item_lastpos = list(
                            self.invItems[index].position)

                        self.cld_icon = index
                        mouse_x, mouse_y = event.pos
                        self.offset_x = self.invItems[index].position[0] - mouse_x
                        self.offset_y = self.invItems[index].position[1] - mouse_y

                        self.drag_item = True

                if cancel.collidepoint(mouse_pos):
                    if self.modify is True or self.master is True:
                        self.cancel = True
                    mainloop = False
                    return(True)

                if accept.collidepoint(mouse_pos):
                    if self.charlist and self.modify == 0:
                        self.resetList(self.currchar)
                    elif self.master:
                        self.pointsleft = self.pointsleft_temp
                        self.skillsleft = self.skillsleft_temp
                        return(True)
                    else:
                        self.accept()
                        return(True)
                    mainloop = False

                if self.showSkills:
                    for i in range(len(self.tabs)):
                        if self.tabs[i].collidepoint(mouse_pos):
                            self.skillTab_show = i

                    for i in range(len(self.skill_buttons)):
                        if self.skill_buttons[i].collidepoint(mouse_pos):
                            self.manageSkill(i, self.skillTab_show)

                for equip_index, equip_slot in enumerate(self.equipslots_rects):
                    if equip_slot.collidepoint(event.pos) and self.unequip is False:
                        self.item_lastpos = list(
                            self.invItems[index].position)

                        self.cld_icon = equip_index
                        mouse_x, mouse_y = event.pos
                        self.offset_x = equip_slot.left - mouse_x
                        self.offset_y = equip_slot.top - mouse_y

                        self.unequip_pos_x = mouse_x + self.offset_x
                        self.unequip_pos_y = mouse_y + self.offset_y

                        self.unequip = True

            elif event.type == pygame.MOUSEMOTION:
                if self.drag_item is True:
                    mouse_x, mouse_y = event.pos
                    self.invItems[self.cld_icon].position[0] = mouse_x + \
                        self.offset_x
                    self.invItems[self.cld_icon].position[1] = mouse_y + \
                        self.offset_y
                    self.invItems[self.cld_icon].updateRect()
                elif self.unequip is True:
                    mouse_x, mouse_y = Utils.getMousePosition(0, 0)
                    self.unequip_pos_x = mouse_x + self.offset_x
                    self.unequip_pos_y = mouse_y + self.offset_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if self.drag_item is True:
                    success = False
                    for collider in self.equipColliders:
                        if collider.collidepoint(event.pos):
                            equip_in = self.invItems[self.cld_icon]
                            if equip_in.slot == '1':
                                if event.pos[0] > 600:
                                    self.equipManager(equip_in, 1)
                                else:
                                    self.equipManager(equip_in, 2)
                            else:
                                self.equipManager(equip_in)

                            self.reloadPlayer()
                            self.accept()
                            self.reloadInv()
                            self.refreshEquipsIMG()
                            success = True

                    if not success:
                        self.invItems[self.cld_icon].position = self.item_lastpos
                        self.invItems[self.cld_icon].updateRect()

                    self.drag_item = False

                elif self.unequip is True:
                    if self.inv_rect.collidepoint(event.pos):
                        item = items.Item(
                            self.activePlayer.equips[self.cld_icon], (0, 0))
                        if item.slot == '2':
                            self.activePlayer.equips[1] = 'empty'
                            self.activePlayer.equips[2] = 'empty'
                        else:
                            self.activePlayer.equips[self.cld_icon] = 'empty'

                        self.invItems.append(item)

                        self.reloadPlayer()
                        self.accept()
                        self.reloadInv()
                        self.refreshEquipsIMG()

                    self.unequip = False

            elif event.type == pygame.KEYDOWN:
                if not self.showInv:
                    if event.key >= 97 and event.key <= 122:
                        if len(self.name) <= 10:
                            letter = chr(event.key)
                            if len(self.name) == 0:
                                letter = letter.upper()
                            self.name = self.name + letter

                    elif event.key == pygame.K_SPACE:
                        self.name = self.name + ' '
                    elif event.key == pygame.K_BACKSPACE:
                        self.name = self.name[:-1]
                    elif event.key == pygame.K_ESCAPE:
                        exit()

            if event.type == pygame.QUIT:
                exit()

        return(False)

    def equipManager(self, equip_in=None, slot=1):
        if equip_in.slot == '2':

            if self.activePlayer.equips[1] is not 'empty':
                temp_equip = items.Item(self.activePlayer.equips[1], (0, 0))
            elif self.activePlayer.equips[2] is not 'empty':
                temp_equip = items.Item(self.activePlayer.equips[2], (0, 0))
            else:
                temp_equip = items.Item('0000', (0, 0))

            if temp_equip.slot == '2':

                self.appendItem(self.activePlayer.equips[1])
                self.activePlayer.equips[1] = equip_in.id
                self.activePlayer.equips[2] = equip_in.id
                self.invItems.pop(self.invItems.index(
                    self.invItems[self.cld_icon]))
            else:
                self.appendItem(self.activePlayer.equips[1])
                self.appendItem(self.activePlayer.equips[2])
                self.activePlayer.equips[1] = equip_in.id
                self.activePlayer.equips[2] = equip_in.id
                self.invItems.pop(self.invItems.index(
                    self.invItems[self.cld_icon]))
        elif equip_in.slot == '1':
            if self.activePlayer.equips[slot] is not 'empty':
                temp_equip = items.Item(self.activePlayer.equips[slot], (0, 0))

                if temp_equip.slot == '2':
                    self.appendItem(self.activePlayer.equips[1])
                    self.activePlayer.equips[slot] = equip_in.id
                    if slot == 1:
                        self.activePlayer.equips[2] = 'empty'
                    else:
                        self.activePlayer.equips[1] = 'empty'
                    self.invItems.pop(self.invItems.index(
                        self.invItems[self.cld_icon]))
                else:
                    self.appendItem(self.activePlayer.equips[slot])
                    self.activePlayer.equips[slot] = equip_in.id
                    self.invItems.pop(self.invItems.index(
                        self.invItems[self.cld_icon]))
            else:
                self.appendItem(self.activePlayer.equips[slot])
                self.activePlayer.equips[slot] = equip_in.id
                self.invItems.pop(self.invItems.index(
                    self.invItems[self.cld_icon]))
        else:
            self.appendItem(self.activePlayer.equips[int(equip_in.slot)])
            self.activePlayer.equips[int(equip_in.slot)] = equip_in.id
            self.invItems.pop(self.invItems.index(
                self.invItems[self.cld_icon]))

    def appendItem(self, UID, position=(0, 0)):
        if UID is not 'empty':
            item = items.Item(UID, position)
            if item.name is not 'empty':
                self.invItems.append(item)

    def accept(self):
        s = self.name + ';' + str(int(self.stat[0]) * 20) + ';' + str(int(self.stat[3]) * 20) + ';' + str(self.stat) + ';' + str(self.skills) + ';' + \
            str(self.pointsleft) + ';' + \
            str(self.skillsleft) + ';' + self.img + ';' + \
            str(self.equips) + ';' + str(self.invID) + ';' + \
            str(self.playermoney) + ';' + str(self.exp) + ';1'
        inv = str(self.invID) + ';[]\n'

        if self.modify:
            inv = str(self.invID) + ';['
            for index, item in enumerate(self.invItems):
                if index == len(self.invItems) - 1:
                    inv = inv + "'" + str(self.invItems[index].id) + "']"
                else:
                    inv = inv + "'" + str(self.invItems[index].id) + "',"

            self.refreshList(self.currchar, s)
            self.refreshInv(inv)
        else:
            self.resetInv()
            self.resetList()
            Utils.addToFile(s, 'databases/players')
            Utils.addToFile(inv, 'databases/inventorys')

    def resetInv(self):
        playersList = Utils.getList('databases/inventorys')
        result = []
        for item in playersList:
            result.append(item)

        f = open("databases/inventorys", "w")
        for item in result:
            f.write(item[0] + ';' + item[1])

            f.write('\n')
        f.close()

    def activateButton(self, stat):
        attrib = stat // 2
        op = stat % 2
        if op == 0:
            self.stat[attrib] = int(self.stat[attrib]) - 1
            self.pointsleft += 1
        else:
            self.stat[attrib] = int(self.stat[attrib]) + 1
            self.pointsleft -= 1

    def refreshInv(self, inv_string=None):
        invList = Utils.getList('databases/inventorys')
        result = []

        for item in invList:
            if item[0] == self.invID:
                string = inv_string
            else:
                string = str(item[0]) + ';' + str(item[1])

            result.append(string)

        f = open("databases/inventorys", "w")
        for item in range(len(result)):
            f.write(result[item])
            f.write('\n')
        f.close()

        return(result)

    def refreshList(self, chosen=None, char_string=None):
        playersList = Utils.getList('databases/players')
        result = []
        for index, item in enumerate(playersList):
            string = ''
            for attrib in range(len(item)):
                if attrib == 0:
                    string = item[attrib]
                elif attrib == len(item) - 1:
                    if chosen == index:
                        string = char_string
                    else:
                        string = string + ';0'
                else:
                    string = string + ';' + str(item[attrib])
            result.append(string)

        f = open("databases/players", "w")
        for item in range(len(result)):
            f.write(result[item])
            f.write('\n')
        f.close()

        return(result)

    def resetList(self, chosen=None):
        playersList = Utils.getList('databases/players')
        result = []
        for index, item in enumerate(playersList):
            string = ''
            for attrib in range(len(item)):
                if attrib == 0:
                    string = item[attrib]
                elif attrib == len(item) - 1:
                    if chosen == index:
                        string = string + ';1'
                    else:
                        string = string + ';0'
                else:
                    string = string + ';' + str(item[attrib])
            result.append(string)

        f = open("databases/players", "w")
        for item in range(len(result)):
            f.write(result[item])
            f.write('\n')
        f.close()

        return(result)

    def drawInventory(self):
        Utils.drawSquare(275, 275, 65, 135, self.screen)
        Utils.drawSquare(225, 40, 115, 425, self.screen)
        self.screen.blit(self.money, (60, 420))
        text = self.name_font.render(
            str(self.playermoney), True, (250, 250, 250))
        self.screen.blit(text, (120, 427))

        for i in range(4):
            for j in range(4):
                Utils.drawSquare(60, 60, j * 65 + 75, i *
                                 65 + 145, self.screen)

        for item in self.invItems:
            if self.drag_item is True:

                if item is self.invItems[self.cld_icon] and self.cld_icon is not None:
                    self.screen.blit(item.imgFile, self.item_lastpos)
                else:
                    self.screen.blit(item.imgFile, item.position)
            else:
                self.screen.blit(item.imgFile, item.position)

    def drawDragged(self):
        if self.drag_item is True:
            self.screen.blit(
                self.invItems[self.cld_icon].imgFile, self.invItems[self.cld_icon].position)

    def run(self):
        button = []
        self.skill_buttons = []
        self.cancel = False
        self.drag_item = False
        self.unequip = False
        global mainloop
        mainloop = True
        accept = 0
        while mainloop:

            del button[:]
            del self.skill_buttons[:]
            del self.attribs[:]

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background, (0, 0))

            # Redraw the background

            if self.showInv:
                self.drawInventory()
            else:
                # Stats surface
                Utils.drawSquare(295, 290, 55, 175, self.screen)
                self.statValues()
                self.drawButtons(button)
                self.drawStats()

            accept, cancel = self.drawConfirmation()

            self.drawTexts()

            mouse_pos = Utils.getMousePosition(0, 0)

            if cancel.collidepoint(mouse_pos):
                self.screen.blit(self.cancel1, (0, 0))
            else:
                self.screen.blit(self.cancel0, (0, 0))

            mouse_pos = Utils.getMousePosition(-425, -25)

            if accept.collidepoint(mouse_pos):
                self.screen.blit(self.accept1, (0, 0))
            elif self.modify == 1 or self.master:
                self.screen.blit(self.accept0, (0, 0))
            else:
                if not self.name == '' and self.pointsleft == 0 and self.skillsleft == 0:
                    self.screen.blit(self.accept0, (0, 0))

            if self.showSkills:
                self.drawSkills(self.skillTab_show, self.skill_buttons)
            else:
                self.drawVisual()

            skills, visual = self.rightTabs()
            idcard, inv = self.leftTabs()

            prev_char, next_char = self.changeButtons()
            prev_img, next_img = self.changeImgButtons()

            done = self.checkEvents(button, accept, cancel, prev_char,
                                    next_char, skills, visual, prev_img, next_img, idcard, inv)

            self.drawDragged()

            if self.unequip is True:
                self.inv_rect = pygame.Rect(65, 135, 275, 275)
                self.screen.blit(
                    self.equipIMG[self.cld_icon], (self.unequip_pos_x, self.unequip_pos_y))

            if done:
                if self.cancel and self.master is False:
                    return(self.activePlayer)
                elif self.modify:
                    self.resolvePlayer()
                    return(self.activePlayer)
                else:
                    return(self.active_chars)

            pygame.display.flip()
