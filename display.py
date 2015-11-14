import pygame

class Renderer:

    def __init__():
        pygame.init()
        self.screen = pygame.display.get_surface()

        self.width, self.height = screen.get_width(), screen.get_height()
        flags = screen.get_flags()
        bits = screen.get_bitsize()

        pygame.display.quit()
        pygame.display.init()

        self.screen = pygame.display.set_mode((self.w, self.h), flags^FULLSCREEN, bits)


    def loop():
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
        render()


    def render():
        screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    renderer = Renderer()
