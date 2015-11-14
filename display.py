import pygame
from pygame.locals import *

class Renderer:

    def __init__(self):
        pygame.init()
        SW,SH = 1280, 720
        self.screen = pygame.display.set_mode((SW,SH))

        self.width, self.height = self.screen.get_width(), self.screen.get_height()
        flags = self.screen.get_flags()
        bits = self.screen.get_bitsize()

        pygame.display.quit()
        pygame.display.init()

        self.screen = pygame.display.set_mode((self.width, self.height), flags^FULLSCREEN, bits)


    def loop(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                render()


    def render(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    renderer = Renderer()
