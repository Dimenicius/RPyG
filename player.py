# name;hp;mp;[s,p,e,c,i,a,l];[[s,k,i,l,l],[s,k,i,l,l],[s,k,i,l,l],[s,k,i,l,l],[s,k,i,l,l]];statLeft;skillLeft;img.png;[e,q,u,i,p];InventoryID;chosen
import utils
import skills
import pygame

Utils = utils.Utils()
Skills = skills.Skills()


class Player:
    def __init__(self, ID):
        charlist = Utils.getList('databases/players')
        char = charlist[ID]

        self.id = ID
        self.type = 'player'
        self.name = char[0]
        self.maxHP = char[1]
        self.maxMP = char[2]
        self.curHP = int(char[1])
        self.curMP = int(char[2])
        self.stat = eval(char[3])
        self.skills = eval(char[4])
        self.statLeft = char[5]
        self.skillLeft = char[6]
        self.img = char[7]
        self.equips = eval(char[8])
        self.IID = char[9]
        self.money = char[10]
        self.exp = char[11]

        self.invList = Utils.getList('databases/inventorys')
        self.invent = self.getInfo(self.IID)

        self.itemList = Utils.getList('databases/items')

        self.equipsNames = []

        for i in range(len(self.equips)):
            for item in self.itemList:
                if self.equips[i] == item[0]:
                    self.equipsNames.append(item[1])

        self.getImgFile()

    def setPos(self, pos_x, pos_y):
        self.pos = (pos_x, pos_y)

    def getImgFile(self):
        self.imgFile = pygame.image.load('sprites/chars/' + self.img)

    def __str__(self):
        s = ('\n' + self.name + '\nHP:' + str(self.curHP) + '/' + str(self.maxHP) +
             '\tMP:' + str(self.curMP) + '/' + str(self.maxMP) + '\n\nStats:' +
             '\nSTR:' + str(self.stat[0]) + '\tPOL:' + str(self.stat[1]) +
             '\nEND:' + str(self.stat[2]) + '\tCHA:' + str(self.stat[3]) +
             '\nINT:' + str(self.stat[4]) + '\tAGI:' + str(self.stat[5]) +
             '\nLOV:' + str(self.stat[6]) + '\n\nStats left:' + str(self.statLeft) +
             '\nSkills left:' + str(self.skillLeft) + '\n\nImg_File:' + self.img +
             '\nInventory ID: [' + self.IID + ']\n\nEquips:\n' + str(self.equipsNames))
        return s

    def getInfo(self, UID):
        for item in self.invList:
            if str(item[0]) == str(UID):
                return(item)
        return(None)

    def action(self, action, target=None, skill=None):
        if action == 'Attack':
            if target.isAlive():
                target.curHP = int(target.curHP) - 20
                return(True)
        else:
            if target is not None:
                if target.isAlive():
                    Skills.activate(skill[0], skill[1], target, self)
                    return(True)
            else:
                Skills.activate(skill[0], skill[1], target, self)
                return(True)
        return(False)

    def isAlive(self):
        if self.curHP > 0:
            return(True)
        else:
            return(False)

    def activeSkills(self):
        active_skills = []
        for i in range(len(self.skills)):
            for j in range(len(self.skills[i])):
                if int(self.skills[i][j]) > 0:
                    active_skills.append((i, j))
        return(active_skills)
