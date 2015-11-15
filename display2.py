import pygame
import node
import icons
from pygame.locals import *

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Renderer2:

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
        
        self.currentGesture = node.read_from_file()
        self.currentNode = (1, 1)
        self.oldNodes = []
        
        self.cachedIcons = {}
        
        self.select('r_')

        clock = pygame.time.Clock()

        fullscreenFlags = flags#^FULLSCREEN
        self.screen = pygame.display.set_mode((self.width, self.height), fullscreenFlags, bits)
        self.cacheIcons(self.currentGesture)

    def start(self):
        self.loop()

    def loop(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT and not self.loading:
                    done = True
            self.render()

    def select(self, direction):
        new_node = self.currentNode
        new_node = self.nodeInDirection(new_node, direction)
        
        if new_node == None:
            return;
        
        self.oldNodes.append(self.currentNode)
        self.currentNode = new_node;
        
        # Turn on flag for animation here
        
        self.currentGesture = self.currentGesture[direction]
        
        if not isinstance(self.currentGesture, dict):
            pass
            # We've gotta launch the application and reset the state

    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg.image, self.bg.rect)
        self.drawCircles()
        self.drawIcons()
        pygame.display.flip()

    
    def cacheIcons(self, rules):
        collapsed_possibilities = node.get_child_collapsed_possibilities(rules)
        for key, child in collapsed_possibilities.iteritems():
            for iconName in child:
                iconHash = str(hash(iconName))[:8]
                #icons.loadFile(iconName, iconHash)
                icons.loadFile("C:\\Program Files (x86)\\Audacity\\audacity.exe", iconHash)
                self.cachedIcons[iconName] = icons.imageFromFile(iconHash, 64, 64)


    def drawIcons(self): 
        collapsed_possibilities = node.get_child_collapsed_possibilities(self.currentGesture)
        for key, child in collapsed_possibilities.iteritems():
            print("Key: " + key)
            iconLocation = self.nodeInDirection(self.currentNode, key)
            
            cachedIconList = []
            for cachedIconName in child:
                cachedIconList.append(self.cachedIcons[cachedIconName])
            
            joined = icons.joinImages(cachedIconList, 64, 64)
            print("Planning to draw icon at " + str(iconLocation))
            self.screen.blit(joined, self.dotDict[iconLocation])


    def drawCircles(self):
        dot = pygame.transform.scale(pygame.image.load("circle.bmp"), (64, 64))
        highlighted_dot = pygame.transform.scale(pygame.image.load("highlighted_circle.bmp"), (64, 64))
        currently_selected_dot = pygame.transform.scale(pygame.image.load("currently_selected_circle.bmp"), (64, 64))
        for currDot in self.dotDict:
            if currDot == self.currentNode:
                self.screen.blit(currently_selected_dot, self.dotDict[currDot])
            elif currDot in self.oldNodes:
                self.screen.blit(highlighted_dot, self.dotDict[currDot])
            else:
                self.screen.blit(dot, self.dotDict[currDot])

    def nodeInDirection(self, pos, direction):
        if direction == 'r_':
            new_node = (self.currentNode[0] + 1, self.currentNode[1])
        elif direction == 'ur':
            new_node = (self.currentNode[0] + 1, self.currentNode[1] - 1)
        elif direction == 'u_':
            new_node = (self.currentNode[0], self.currentNode[1] - 1)
        elif direction == 'ul':
            new_node = (self.currentNode[0] - 1, self.currentNode[1] - 1)
        elif direction == 'l_':
            new_node = (self.currentNode[0] - 1, self.currentNode[1])
        elif direction == 'dl':
            new_node = (self.currentNode[0] - 1, self.currentNode[1] + 1)
        elif direction == 'd_':
            new_node = (self.currentNode[0], self.currentNode[1] + 1)
        elif direction == 'dr':
            new_node = (self.currentNode[0] + 1, self.currentNode[1] + 1)
        
        for e in new_node:
            if e < 0 or e > 2:
                return None;
        return new_node
        
        
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
    renderer = Renderer2()
    renderer.start()