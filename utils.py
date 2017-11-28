import pygame
import os


class Utils():
    def getMousePosition(self, x_var, y_var):
        mouse_pos = pygame.mouse.get_pos()
        mouse_posx = mouse_pos[0] + x_var
        mouse_posy = mouse_pos[1] + y_var
        mouse_pos = (mouse_posx, mouse_posy)
        return (mouse_pos)

    def drawSquare(self, size_x, size_y, pos_x, pos_y, surface, img=None):
        self.sqrSurf = pygame.Surface((size_x, size_y), pygame.SRCALPHA, 32)
        self.sqrSurf.fill((0, 0, 0, 100))
        if img:
            self.sqrSurf.blit(img, (0, 0))
        surface.blit(self.sqrSurf, (pos_x, pos_y))
        return(self.sqrSurf)

    def getFiles(self, path):
        files = os.listdir(path)
        files.sort()
        return(files)

    def getFileID(self, files, name):
        index = files.index(name)
        return(index)

    def getList(self, file_name):
        List = []
        f = open(file_name, "r")
        for line in f:
            if line[0] != "\n" and line[0] != "":
                List.append(line.rstrip().split(';'))
        f.close()
        return (List)

    def getLastID(self, file_name):
        items = self.getList(file_name)
        if items:
            return(items[len(items) - 1][0])
        else:
            return(None)

    def getIDPos(self, file_name, ID):
        items = self.getList(file_name)
        for index, item in enumerate(items):
            if ID == item[0]:
                return (index)
        return(None)

    def getByID(self, file_name, ID):
        items = self.getList(file_name)
        return(items[ID])

    def addToFile(self, newline, file_name):
        # opens file with name of "test.txt"
        f = open(file_name, "a")
        f.write(newline)
        f.close()

    def findActive(self, lista):
        for index, item in enumerate(lista):
            if item[len(item) - 1] == '1':
                return(index, item)
        return(None)
