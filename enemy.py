# name;hp;mp;[s,p,e,c,i,a,l];[[s,k,i,l,l],[s,k,i,l,l],[s,k,i,l,l],[s,k,i,l,l],[s,k,i,l,l]];statLeft;skillLeft;img.png;[e,q,u,i,p];InventoryID;chosen
import utils
import pygame
import skills

Utils = utils.Utils()
Skills = skills.Skills()

# Name;life;mana;stats;skills;equips;img;loot


class Enemy:
    def __init__(self, ID):
        enemylist = Utils.getList('databases/enemys')
        enemy = enemylist[ID]

        self.id = ID
        self.type = 'enemy'
        self.name = enemy[0]
        self.maxHP = enemy[1]
        self.maxMP = enemy[2]
        self.curHP = int(enemy[1])
        self.curMP = int(enemy[2])
        self.stat = eval(enemy[3])
        self.skills = eval(enemy[4])
        self.img = enemy[5]
        self.equips = enemy[6]
        self.lootID = enemy[7]

        self.lootList = Utils.getList('databases/loots')
        self.loot = self.getInfo(self.lootID)

        self.itemList = Utils.getList('databases/items')
        self.getImgFile()
        self.equipsNames = []

        for i in range(len(self.equips)):
            for item in self.itemList:
                if self.equips[i] == item[0]:
                    self.equipsNames.append(item[1])

    def __str__(self):
        s = ('\n' + self.name + '\nHP:' + str(self.curHP) + '/' + str(self.maxHP) +
             '\tMP:' + str(self.curMP) + '/' + str(self.maxMP) + '\n\nStats:' +
             '\nSTR:' + str(self.stat[0]) + '\tPOL:' + str(self.stat[1]) +
             '\nEND:' + str(self.stat[2]) + '\tCHA:' + str(self.stat[3]) +
             '\nINT:' + str(self.stat[4]) + '\tAGI:' + str(self.stat[5]) +
             '\nLOV:' + str(self.stat[6]) + '\n\nImg_File:' + self.img +
             '\nLoot ID: [' + self.lootID + ']\n\nEquips:\n' + str(self.equipsNames))
        return s

    def setPos(self, pos_x, pos_y):
        self.pos = (pos_x, pos_y)

    def getImgFile(self):
        self.imgFile = pygame.image.load('sprites/enemys/' + self.img)

    def getInfo(self, UID):
        for item in self.lootList:
            if str(item[0]) == str(UID):
                return(item)
        return(None)

    def action(self, action, target=None, skill=None):
        if action == 'Attack':
            if target.isAlive():
                target.curHP = int(target.curHP) - 20
                return(True)
        else:
            if target:
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
