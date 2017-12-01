import pygame
from PodSixNet.Connection import ConnectionListener


class MyNetworkListener(ConnectionListener):

    def Network(self, data):
        print ('network data:', data)

    def Network_connected(self, data):
        print ("connected to the server")

    def Network_error(self, data):
        print ("error:", data['error'][1])

    def Network_disconnected(self, data):
        print ("disconnected from the server")

    def Network_myaction(data):
        print ("myaction:", data)


class Game():
    def __init__(self, screen):

        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height

    def checkEvents(self):
        global mainloop

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print('Mouse01')

    def run(self):
        clock = pygame.time.Clock()
        clock.tick(10)
        while True:
            global mainloop
            mainloop = True

            while mainloop:

                self.checkEvents()

                pygame.display.flip()
                connection.Pump()


pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

if __name__ == "__main__":
    # Creating the screen
    clock = pygame.time.Clock()
    clock.tick(10)

    # screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN, 32)
    screen = pygame.display.set_mode((800, 600), 0, 32)

    pygame.display.set_caption('Doomlike')

    Game = Game(screen)
    Game.run()
