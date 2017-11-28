import pygame
import utils

Utils = utils.Utils()


class Icon():
    def __init__(self, position):
        self.imgIndex = 0
        self.img = '000.png'
        self.name = ''
        self.imgFiles = Utils.getFiles('sprites/map/icons/')
        self.getImgFile()
        self.position = position
        self.updateRect()

    def getImgFile(self):
        self.imgFile = pygame.image.load(
            'sprites/map/icons/' + self.imgFiles[self.imgIndex])

    def updateRect(self):
        self.rect = pygame.Rect(self.position[0], self.position[1], 50, 50)
        self.left = pygame.Rect(
            self.position[0] - 20, self.position[1] + 30, 40, 40)
        self.right = pygame.Rect(
            self.position[0] + 30, self.position[1] + 30, 40, 40)

    def changeImg(self, qty):
        self.imgIndex += qty

        if self.imgIndex == len(self.imgFiles):
            self.imgIndex = 0
        elif self.imgIndex < 0:
            self.imgIndex = len(self.imgFiles) - 1

        self.getImgFile()
