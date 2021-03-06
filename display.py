import pygame
from pygame.locals import *

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Renderer:

    def __init__(self):
        pygame.init()
        self.loading = True
        SW,SH = 1280, 720
        self.screen = pygame.display.set_mode((SW,SH))
        self.dotDict = {(0,0): (400,120),
        				(1,0): (600,120),
        				(2,0): (800,120),
        				(0,1): (400,320),
        				(1,1): (600,320),
        				(2,1): (800,320),
        				(0,2): (400,520),
        				(1,2): (600,520),
        				(2,2): (800,520)}

        self.bg = Background("bg.jpg", [0,0])

        self.width, self.height = self.screen.get_width(), self.screen.get_height()
        flags = self.screen.get_flags()
        bits = self.screen.get_bitsize()

        pygame.display.quit()
        pygame.display.init()
        self.loading = False

        clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((self.width, self.height), flags^FULLSCREEN, bits)

    def start(self):
        self.loop()

    def loop(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT and not self.loading:
                    done = True
            self.render()

    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg.image, self.bg.rect)
        self.drawCircles()
        pygame.display.flip()

    def drawCircles(self):
    	dot = pygame.image.load("circle.bmp")
    	dot = pygame.transform.scale(dot, (64,64))
    	for currDot in self.dotDict:
    		self.screen.blit(dot, self.dotDict[currDot])

class Rectangle:

	def __init__(self, xcoor, ycoor, height, width, direction):
		self.x = xcoor
		self.y = ycoor
		self.height = height
		self.width = width
		self.direction = direction

	def increment(self):
		if self.direction == HORIZONTAL:
			self.width += 1
		elif self.direction == VERTICAL:
			self.height += 1
		else: #direction == diagonal
			pass

	def reset(self):
		if self.direction == HORIZONTAL:
			self.width = 1
		elif self.direction == VERTICAL:
			self.height = 1
		else: #direction == diagonal
			pass

	def slidingRect(self, startNode, endNode):
		
        x_coor = self.dotDict[startNode][0]
        y_coor = self.dotDict[startNode][1]
        end_x = self.dotDict[endNode][0]
        end_y = self.dotDict[endNode][1]
    	final_width = (end_x - x_coor)
    	final_height = (end_y - y_coor)

    	if self.myX <= (end_x - x_coor):
    		pygame.draw.rect(self.screen, (255,0,0), (x_coor+32,y_coor+14, self.myX,40), 0)

if __name__ == '__main__':
    renderer = Renderer()
    renderer.start()
