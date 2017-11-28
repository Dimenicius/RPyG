import utils
import pygame

Utils = utils.Utils()
Item_slot = ['Jewel', '1Hand Item', '2Hand Item', 'Armor', 'Boots']
# Name;type;slot;description;value;image


class Item():
    def __init__(self, UID, position):
        self.itemlist = Utils.getList('databases/items')
        self.item = self.getItemInfo(UID)
        self.position = position

        self.id = UID

        if self.item is not None:
            self.name = self.item[1]
            self.type = self.item[2]
            self.slot = self.item[3]
            self.desc = self.item[4]
            self.value = self.item[5]
            self.img = self.item[6]
            self.getImgFile()
            self.updateRect()

    def updateRect(self):
        self.rect = pygame.Rect(self.position[0], self.position[1], 50, 50)

    def getImgFile(self):
        self.imgFile = pygame.image.load('sprites/items/' + self.img)

    def __str__(self):
        s = ('Item:' + self.name + '\t\tType:' + self.type +
             '\nSlot:' + Item_slot[int(self.slot)] + '\t\tDesc:' + self.desc +
             '\nValue:$' + self.value + '\t\tImg_File:' + self.img)
        return(s)

    def getItemInfo(self, UID):
        for item in self.itemlist:
            if str(item[0]) == str(UID):
                return(item)
        return(None)
