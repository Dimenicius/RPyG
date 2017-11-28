import pygame
import random
import utils
import chrmod
import skills

players = []
Utils = utils.Utils()
Skills = skills.Skills()


class Battle():
    def __init__(self, screen, enemys, chars):

        font = 'font/BEBAS.ttf'
        font_size = 20
        font_info = 15
        font_color = (255, 255, 255)

        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height

        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(font, font_size)
        self.info_font = pygame.font.Font(font, font_info)
        self.font_color = font_color

        self.background = pygame.image.load('sprites/battle/background.png')

        self.enemys = enemys

        self.chars = chars

        self.chosenSkill = None

        self.all = self.enemys + self.chars

        self.enemyRects = []

    def loadImages(self):
        self.attackImg = pygame.image.load('sprites/battle/attack.png')
        self.skillsImg = pygame.image.load('sprites/battle/skills.png')
        self.inventoryImg = pygame.image.load('sprites/battle/inventory.png')
        self.fleeImg = pygame.image.load('sprites/battle/flee.png')
        self.cancel = pygame.image.load('sprites/battle/cancel.png')

        self.attack = pygame.image.load('sprites/battle/attackIMG.png')
        self.skills = pygame.image.load('sprites/battle/skillsIMG.png')
        self.inventory = pygame.image.load('sprites/battle/inventoryIMG.png')
        self.flee = pygame.image.load('sprites/battle/fleeIMG.png')

    def drawImgRect(self, image, pos_x, pos_y, rectList):
        return(pygame.Rect(pos_x + 50, pos_y + 50, image.get_rect().width - 100, image.get_rect().height - 100))

    def drawColliders(self, creatures, folder_name, chars=0):
        rectList = []
        for index, item in enumerate(creatures):

            pos_y = (100 * index) + 50 * (3 - len(creatures))
            if chars == 0:
                if index % 2 == 0:
                    pos_x = 500
                else:
                    pos_x = 600
            else:
                if index % 2 == 0:
                    pos_x = 150
                else:
                    pos_x = 50

            creatures[index].setPos(pos_x, pos_y)

            self.screen.blit(creatures[index].imgFile, creatures[index].pos)

            if self.all[self.currTurn] == creatures[index]:
                self.drawTurnArrow(pos_x + 75, pos_y)

            rectList.append(self.drawImgRect(
                creatures[index].imgFile, pos_x, pos_y, rectList))

        return(rectList)

    def charInfo(self, char):
        Utils.drawSquare(300, 50, 250, 10, self.screen)
        self.drawInfo(char.name, 250, 15, 300)
        self.drawInfo('HP: ' + str(char.curHP) + ' / ' + str(char.maxHP) + '          MP: ' +
                      str(char.maxMP) + ' / ' + str(char.curMP), 250, 35, 300)

    def drawTurnArrow(self, pos_x, pos_y):
        imagem = pygame.image.load('sprites/battle/turnArrow.png')
        self.screen.blit(imagem, (pos_x, pos_y))

    def checkEvents(self, attack, skills, inventory, flee, charsCollider, enemysCollider, cancel):
        global mainloop

        # Limit frame speed to 50 FPS
        self.clock.tick(50)
        global players

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = Utils.getMousePosition(0, 0)

                if self.chooseTarget == 0:
                    if attack.collidepoint(mouse_pos):
                        self.action = 'Attack'
                        self.chooseTarget = 1
                    elif skills.collidepoint(mouse_pos):
                        self.choosing_skill = True
                    elif inventory.collidepoint(mouse_pos):
                        if self.all[self.currTurn].type is 'player':
                            CM = chrmod.CharModification(
                                self.screen, 0, [0, 0, 0, 0, 0, 0, 0], Utils.getList('databases/players'), self.all[self.currTurn].id, 1, charmod=self.all[self.currTurn])
                            self.all[self.currTurn] = CM.run()

                        else:
                            print('Enemy has no inventory!')

                    elif flee.collidepoint(mouse_pos):
                        print('Flee')
                        mainloop = False
                        break
                else:
                    if cancel.collidepoint(mouse_pos):
                        self.chooseTarget = 0
                        self.choosing_skill = False

                    for i in range(len(charsCollider)):
                        if charsCollider[i].collidepoint(mouse_pos):
                            done = None
                            if self.chosenSkill or self.action == 'Attack':
                                done = self.all[self.currTurn].action(
                                    self.action, self.chars[i], self.chosenSkill)

                            if done:
                                self.passTurn()
                            else:
                                self.chooseTarget = 0
                                self.choosing_skill = False

                    active_skills = self.all[self.currTurn].activeSkills()

                    if self.choosing_skill:
                        for rect in range(len(self.skillRects)):
                            if self.skillRects[rect].collidepoint(mouse_pos):
                                if Skills.skillTarget[active_skills[rect]
                                                      [0]][active_skills[rect][1]]:
                                    self.chosenSkill = active_skills[rect]
                                    self.chooseTarget = 1
                                    self.action = 'Skills'
                                    self.choosing_skill = False

                                else:
                                    self.chosenSkill = active_skills[rect]
                                    self.action = 'Skills'

                                    done = self.all[self.currTurn].action(
                                        self.action, None, self.chosenSkill)

                                    self.passTurn()

                    for i in range(len(enemysCollider)):
                        if enemysCollider[i].collidepoint(mouse_pos):
                            done = None
                            if self.chosenSkill or self.action == 'Attack':
                                done = self.all[self.currTurn].action(
                                    self.action, self.enemys[i], self.chosenSkill)

                            if done:
                                self.passTurn()
                            else:
                                self.chooseTarget = 0
                                self.choosing_skill = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

            elif event.type == pygame.QUIT:
                exit()

    def passTurn(self):
        self.TurnCounter += 1
        self.chooseTarget = 0
        self.choosing_skill = False
        self.chosenSkill = None
        self.currTurn = self.TurnCounter % len(self.all)

    def turnRoll(self):  # Sorteia ordem de turnos
        random.shuffle(self.all)
        return(self.all)

    def drawActionButtons(self):
        sqr_size = 130
        y_pos = 435

        if self.chooseTarget == 0:
            attack = pygame.Rect(125, y_pos, sqr_size, sqr_size)
            skills = pygame.Rect(265, y_pos, sqr_size, sqr_size)
            inventory = pygame.Rect(405, y_pos, sqr_size, sqr_size)
            flee = pygame.Rect(545, y_pos, sqr_size, sqr_size)

            cancel = pygame.Rect(
                self.scr_width, self.scr_height, sqr_size, sqr_size)

            Utils.drawSquare(sqr_size, sqr_size, 125, y_pos, self.screen)
            Utils.drawSquare(sqr_size, sqr_size, 265, y_pos, self.screen)
            Utils.drawSquare(sqr_size, sqr_size, 405, y_pos, self.screen)
            Utils.drawSquare(sqr_size, sqr_size, 545, y_pos, self.screen)

            self.drawText('Attack', 125, 525)
            self.drawText('Skills', 265, 525)
            self.drawText('Inventory', 405, 525)
            self.drawText('Flee', 545, 525)

            self.screen.blit(self.attack, (attack.left, attack.top))
            self.screen.blit(self.skills, (skills.left, skills.top))
            self.screen.blit(self.inventory, (inventory.left, inventory.top))
            self.screen.blit(self.flee, (flee.left, flee.top))
        else:
            attack = pygame.Rect(
                self.scr_width, self.scr_height, sqr_size, sqr_size)
            skills = pygame.Rect(
                self.scr_width, self.scr_height, sqr_size, sqr_size)
            inventory = pygame.Rect(
                self.scr_width, self.scr_height, sqr_size, sqr_size)
            flee = pygame.Rect(
                self.scr_width, self.scr_height, sqr_size, sqr_size)

            sqr_size = 260
            sqr_x = (self.scr_width / 2 - sqr_size / 2)
            cancel = pygame.Rect(sqr_x, y_pos + 75, sqr_size, 75)
            Utils.drawSquare(sqr_size, 75,
                             sqr_x, y_pos + 75, self.screen)

            self.drawText('Cancel', 340, 530)

        return(attack, skills, inventory, flee, cancel)

    def drawSkills(self):
        self.skillRects = []
        sqr_size = (len(self.all[self.currTurn].activeSkills()) * 60) + 10
        sqr_x = (self.scr_width / 2 - sqr_size / 2)
        Utils.drawSquare(sqr_size, 70, sqr_x, 420, self.screen)

        for index, activeSkill in enumerate(self.all[self.currTurn].activeSkills()):
            pos_x = (sqr_x + 60 * index) + 10
            self.skillRects.append(pygame.Rect(pos_x, 430, 60, 60))
            self.screen.blit(
                Skills.skillImg[activeSkill[0]][activeSkill[1]], (pos_x, 430))

        self.action = 'Skills'

    def chooseSkill(self):
        self.action = 'Skill'

        self.drawSkills()

        self.chooseTarget = 1

    def drawText(self, text, pos_x, pos_y, center_to=130):
        text = self.font.render(text, True, (250, 250, 250))

        t_w = text.get_rect().width
        text_x = (center_to / 2) - (t_w / 2)

        self.screen.blit(text, (pos_x + text_x, pos_y))

    def drawInfo(self, text, pos_x, pos_y, center_to=130):
        text = self.info_font.render(text, True, (250, 250, 250))

        t_w = text.get_rect().width
        text_x = (center_to / 2) - (t_w / 2)

        self.screen.blit(text, (pos_x + text_x, pos_y))

    def checkMouse(self, attack, skills, inventory, flee, charsCollider, enemysCollider, cancel):
        mouse_pos = Utils.getMousePosition(0, 0)
        if attack.collidepoint(mouse_pos):
            self.screen.blit(self.attackImg, (attack.left, attack.top))
        elif skills.collidepoint(mouse_pos):
            self.screen.blit(self.skillsImg, (skills.left, skills.top))
        elif inventory.collidepoint(mouse_pos):
            self.screen.blit(self.inventoryImg,
                             (inventory.left, inventory.top))
        elif flee.collidepoint(mouse_pos):
            self.screen.blit(self.fleeImg, (flee.left, flee.top))
        elif cancel.collidepoint(mouse_pos):
            self.screen.blit(self.cancel, (cancel.left, cancel.top))

        char_info = 0

        for i in range(len(charsCollider)):
            if charsCollider[i].collidepoint(mouse_pos):
                self.charInfo(self.chars[i])
                char_info = 1
                break

        for i in range(len(enemysCollider)):
            if enemysCollider[i].collidepoint(mouse_pos):
                self.charInfo(self.enemys[i])
                char_info = 1
                break

        if char_info == 0:
            self.charInfo(self.all[self.currTurn])

    def run(self):
        global mainloop
        mainloop = True
        self.loadImages()
        self.turnRoll()

        self.choosing_skill = False
        self.chooseTarget = 0
        self.TurnCounter = 0

        while mainloop:
            self.currTurn = self.TurnCounter % len(self.all)
            while self.all[self.currTurn].isAlive() is False:
                self.passTurn()

            self.screen.blit(self.background, (0, 0))

            charsCollider = self.drawColliders(self.chars, 'sprites/chars/', 1)
            enemysCollider = self.drawColliders(self.enemys, 'sprites/enemys/')

            attack, skills, inventory, flee, cancel = self.drawActionButtons()

            if self.choosing_skill:
                self.chooseSkill()

            self.checkMouse(attack, skills, inventory, flee,
                            charsCollider, enemysCollider, cancel)

            # Check Events and Refresh screen
            self.checkEvents(attack, skills, inventory, flee,
                             charsCollider, enemysCollider, cancel)

            pygame.display.flip()
