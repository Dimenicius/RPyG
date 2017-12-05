from PodSixNet.Connection import ConnectionListener, connection
from time import sleep

import pygame
import utils
import enemy
import random
import chrmod
import battle as battleObj
import player as playerObj
import maps

Utils = utils.Utils()


# Clients


class Lobby(ConnectionListener):
    def __init__(self, screen, active_char, master=False):

        font = 'font/BEBAS.ttf'
        font_size = 20

        self.master = master

        self.screen = screen
        self.active_char = active_char

        self.mo_sound = pygame.mixer.Sound('sounds/mouse_over.ogg')
        self.mouse_click = pygame.mixer.Sound('sounds/click.ogg')

        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(font, font_size)

        self.chars = []
        self.enemys = []
        self.players = []

        self.last_mouseover = None

        self.mapa = None

        self.background = pygame.image.load('sprites/lobby/lobby_bg.png')

        self.Ximg = pygame.image.load('sprites/lobby/X.png')

        self.inventory = pygame.image.load('sprites/lobby/inventory.png')
        self.player = pygame.image.load('sprites/lobby/player.png')
        self.store = pygame.image.load('sprites/lobby/store.png')
        self.worldmap = pygame.image.load('sprites/lobby/worldmap.png')

        self.battle = pygame.image.load('sprites/lobby/battle.png')
        self.reward = pygame.image.load('sprites/lobby/reward.png')

        self.mouse_over = pygame.image.load('sprites/lobby/mouse_over.png')

        self.Connect()

    # Network Functions
    def Network_addplayer(self, data):
        player_id = data["char"]
        self.players.append(playerObj.Player(player_id))
        print('Jogador ' + str(player_id) + ' conectado')

    def Network_startbattle(self, data):

        self.BATTLE = battleObj.Battle(
            self.screen, self.enemys, self.players, self.master)

        self.enemys = []
        self.battleManager = False
        self.Battle = True

    def Network_addenemy(self, data):
        sortNum = data['enemy']
        temp = enemy.Enemy(sortNum)
        self.enemys.append(temp)

    def Network_isPlayer(self, data):

        if self.master:
            self.Send({"action": "isPlayer", "response": False,
                       "channel": data["channel"]})
        else:
            self.Send({"action": "isPlayer", "response": True,
                       "channel": data["channel"]})

    def Network_yourTurn(self, data):
        print(data)
        self.myTurn = data["isTrue"]
        self.currTurn = data["currTurn"]

    # Draw functions

    def drawButton(self, pos_x, pos_y, img=None, txt=None, size_x=130, size_y=130, txt_pos=90, sqr=True):
        rect = pygame.Rect(pos_x, pos_y, size_x, size_y)
        if sqr:
            Utils.drawSquare(size_x, size_y, pos_x, pos_y, self.screen)
        if img:
            self.screen.blit(img, (pos_x, pos_y))

        if txt:
            self.drawText(txt, pos_x, pos_y + txt_pos)
        return (rect)

    def drawText(self, text, pos_x, pos_y, center_to=130):
        text = self.font.render(text, True, (250, 250, 250))

        t_w = text.get_rect().width
        text_x = (center_to / 2) - (t_w / 2)

        self.screen.blit(text, (pos_x + text_x, pos_y))

    def drawCharButtons(self):
        if self.master:
            player = self.drawButton(
                self.scr_width, self.scr_height, self.player, 'Player')
            invent = self.drawButton(
                self.scr_width, self.scr_height, self.inventory, 'Inventory')
        else:
            player = self.drawButton(10, 280, self.player, 'Player')
            invent = self.drawButton(10, 420, self.inventory, 'Inventory')
        worldmap = self.drawButton(660, 280, self.worldmap, 'Map')
        store = self.drawButton(660, 420, self.store, 'Store')

        return(player, invent, store, worldmap)

    def drawMasterButtons(self):
        if self.master:
            player = self.drawButton(195, 10, self.player, 'Chars')
            battle = self.drawButton(335, 10, self.battle, 'Battle')
            reward = self.drawButton(475, 10, self.reward, 'Reward')
        else:
            player = self.drawButton(
                self.scr_width, self.scr_height, self.player, 'Chars')
            battle = self.drawButton(
                self.scr_width, self.scr_height, self.battle, 'Battle')
            reward = self.drawButton(
                self.scr_width, self.scr_height, self.reward, 'Reward')

        return(player, battle, reward)

    def enemyIMGs(self, e1=None, e2=None, e3=None):
        if e1:
            enemyIMG1 = pygame.image.load('sprites/enemy_face/' + e1)
        else:
            enemyIMG1 = None
        if e2:
            enemyIMG2 = pygame.image.load('sprites/enemy_face/' + e2)
        else:
            enemyIMG2 = None
        if e3:
            enemyIMG3 = pygame.image.load('sprites/enemy_face/' + e3)
        else:
            enemyIMG3 = None

        return(enemyIMG1, enemyIMG2, enemyIMG3)

    def drawBattleEnemys(self):

        if len(self.enemys) > 0:
            img1 = self.enemys[0].img
        else:
            img1 = None

        if len(self.enemys) > 1:
            img2 = self.enemys[1].img
        else:
            img2 = None

        if len(self.enemys) > 2:
            img3 = self.enemys[2].img
        else:
            img3 = None

        img1, img2, img3 = self.enemyIMGs(img1, img2, img3)

        Utils.drawSquare(100, 100, 230, 160, self.screen, img1)
        Utils.drawSquare(100, 100, 350, 160, self.screen, img2)
        Utils.drawSquare(100, 100, 470, 160, self.screen, img3)

        slots = []
        X = []
        if len(self.enemys) > 0:
            X.append(self.drawButton(
                305, 150, self.Ximg, None, 30, 30, 0, False))
        else:
            slots.append(pygame.Rect(230, 160, 100, 100))
        if len(self.enemys) > 1:
            X.append(self.drawButton(
                425, 150, self.Ximg, None, 30, 30, 0, False))
        else:
            slots.append(pygame.Rect(350, 160, 100, 100))
        if len(self.enemys) > 2:
            X.append(self.drawButton(
                545, 150, self.Ximg, None, 30, 30, 0, False))
        else:
            slots.append(pygame.Rect(470, 160, 100, 100))

        return (X, slots)

    def drawBattleManager(self):
        if self.battleManager:
            Utils.drawSquare(400, 200, 200, 150, self.screen)
            X, slots = self.drawBattleEnemys()
            battle_cancel = self.drawButton(
                250, 280, None, 'Cancel', 130, 50, 10)
            if len(self.enemys) > 0:
                battle_confirm = self.drawButton(
                    420, 280, None, 'Confirm', 130, 50, 10)
            else:
                battle_confirm = pygame.Rect(
                    self.scr_width, self.scr_height, 10, 10)
        else:
            X = []
            slots = []
            battle_cancel = pygame.Rect(
                self.scr_width, self.scr_height, 10, 10)

            battle_confirm = pygame.Rect(
                self.scr_width, self.scr_height, 10, 10)

        return(battle_cancel, battle_confirm, X, slots)

    def drawChars(self):
        for index, char in enumerate(self.players):
            self.players[index].setPos((300 - 100 * index), (200 + 75 * index))
            self.screen.blit(
                self.players[index].imgFile, self.players[index].pos)

    # Input functions
    def mouseCheck(self, player, invent, store, gm_player, battle, reward, worldmap):
        mouse_pos = Utils.getMousePosition(0, 0)
        if player.collidepoint(mouse_pos):
            self.screen.blit(
                self.mouse_over, (player.left, player.top))
            return(player)
        elif store.collidepoint(mouse_pos):
            self.screen.blit(
                self.mouse_over, (store.left, store.top))
            return(store)
        elif invent.collidepoint(mouse_pos):
            self.screen.blit(
                self.mouse_over, (invent.left, invent.top))
            return(invent)
        elif gm_player.collidepoint(mouse_pos):
            self.screen.blit(
                self.mouse_over, (gm_player.left, gm_player.top))
            return(gm_player)
        elif battle.collidepoint(mouse_pos):
            self.screen.blit(
                self.mouse_over, (battle.left, battle.top))
            return(battle)
        elif reward.collidepoint(mouse_pos):
            self.screen.blit(
                self.mouse_over, (reward.left, reward.top))
            return(reward)
        elif worldmap.collidepoint(mouse_pos):
            self.screen.blit(
                self.mouse_over, (worldmap.left, worldmap.top))
            return(worldmap)
        else:
            return(None)

    def checkEvents(self, player, invent, store, gm_player, battle, reward, worldmap, battle_cancel, battle_confirm, X, slots):
        global mainloop

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = Utils.getMousePosition(0, 0)

                for i in range(len(X)):
                    if X[i].collidepoint(mouse_pos):
                        self.enemys.pop(i)

                for i in range(len(slots)):
                    if slots[i].collidepoint(mouse_pos):
                        enemy_list = Utils.getList('databases/enemys')

                        self.Send(
                            {"action": "addenemy", "enemy": random.randint(0, len(enemy_list) - 1)})

                        self.mo_sound.play()

                if invent.collidepoint(mouse_pos):
                    self.mouse_click.play()
                    CM = chrmod.CharModification(
                        self.screen, 0, [0, 0, 0, 0, 0, 0, 0], active_char=self.players[0].id, modify=1, charmod=self.players[0], ShowInv=True)
                    self.players[0] = CM.run()
                elif player.collidepoint(mouse_pos):
                    self.mouse_click.play()
                    CM = chrmod.CharModification(
                        self.screen, 0, [0, 0, 0, 0, 0, 0, 0], Utils.getList('databases/players'), self.active_char, 1, charmod=self.players[0])
                    self.players[0] = CM.run()
                    self.players[0].getImgFile()
                elif battle.collidepoint(mouse_pos):
                    self.mouse_click.play()
                    if self.battleManager:
                        self.battleManager = False
                    else:
                        self.battleManager = True
                elif battle_cancel.collidepoint(mouse_pos):
                    self.mouse_click.play()
                    self.enemys = []
                    self.battleManager = False
                elif battle_confirm.collidepoint(mouse_pos):
                    self.mouse_click.play()

                    self.Send({"action": "startbattle", 'data': True})

                    # BATTLE = battleObj.Battle(
                    #     self.screen, self.enemys, self.players)
                    #
                    # self.enemys = []
                    # self.battleManager = False

                    # BATTLE.run()
                elif reward.collidepoint(mouse_pos):
                    self.mouse_click.play()
                elif worldmap.collidepoint(mouse_pos):
                    self.mouse_click.play()
                    if not self.mapa:
                        self.mapa = maps.Map(self.screen)
                    self.mapa.run()
                elif store.collidepoint(mouse_pos):
                    self.mouse_click.play()

                elif gm_player.collidepoint(mouse_pos):
                    self.mouse_click.play()

                    CM = chrmod.CharModification(
                        self.screen, 0, [0, 0, 0, 0, 0, 0, 0], active_chars=self.players, Master=True)
                    result = CM.run()

                    if result:
                        self.players = result
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

            if event.type == pygame.QUIT:
                quit()

    # Main Function
    def run(self):

        global mainloop
        mainloop = True

        self.Battle = False

        self.battleManager = False
        pygame.mixer.music.load('sounds/lobby.ogg')
        # pygame.mixer.music.play(-1)

        if not self.master:
            self.chars.append(self.active_char)
            self.Send({"action": "addplayer", "char": self.active_char})

        while mainloop:

            connection.Pump()
            self.Pump()

            if self.Battle is False:
                self.screen.blit(self.background, (0, 0))
                self.drawChars()

                player, invent, store, worldmap = self.drawCharButtons()

                gm_player, battle, reward = self.drawMasterButtons()

                battle_cancel, battle_confirm, X, slots = self.drawBattleManager()

                mouse_over = self.mouseCheck(player, invent, store, gm_player,
                                             battle, reward, worldmap)

                if not self.last_mouseover == mouse_over and mouse_over is not None:
                    self.last_mouseover = mouse_over
                    self.mo_sound.play()

                self.checkEvents(player, invent, store, gm_player,
                                 battle, reward, worldmap, battle_cancel, battle_confirm, X, slots)

                pygame.display.flip()
            else:
                sentData = self.BATTLE.run(self.myTurn, self.currTurn)
                if sentData is not None:
                    self.Send(sentData)
