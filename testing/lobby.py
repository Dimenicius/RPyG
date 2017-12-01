import pygame
from game_server import MyServer


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
        myserver = MyServer()
        while True:
            global mainloop
            mainloop = True

            while mainloop:

                self.checkEvents()

                pygame.display.flip()
                myserver.Pump()


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
