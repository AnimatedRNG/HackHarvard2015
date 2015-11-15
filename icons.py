import pygame

import win32ui
import win32gui
import win32con
import win32api

from math import log
import os

def loadFile(filename, final_name):
    ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)
    ico_y = win32api.GetSystemMetrics(win32con.SM_CYICON)

    print('Looking for ' + filename)
    large, small = win32gui.ExtractIconEx(filename, 0)
    win32gui.DestroyIcon(small[0])

    hdc = win32ui.CreateDCFromHandle( win32gui.GetDC(0) )
    hbmp = win32ui.CreateBitmap()
    hbmp.CreateCompatibleBitmap( hdc, ico_x, ico_x )
    hdc = hdc.CreateCompatibleDC()

    hdc.SelectObject( hbmp )
    hdc.DrawIcon( (0,0), large[0] )
    hbmp.SaveBitmapFile( hdc, "cache/" +  final_name + ".bmp")


def imageFromFile(final_name, width, height):
    img = pygame.image.load("cache/" + final_name + ".bmp")
    pygame.transform.scale(img, (width, height))
    return img


# Shrinks mutliple spries togehter
def joinImages(images, width, height):
    order = int(log(len(images)) / log(2)) + 1
    img_surface = pygame.Surface((int(width), int(height)))
    dx, dy = width / order, height / order
    index = 0
    for x in range(0, width, dx):
        for y in range(0, height, dy):
            if (index < len(images)):
                shrunk_image = pygame.Surface((images[index].get_rect().width, images[index].get_rect().height))
                shrunk_image.blit(images[index], (0, 0))
                pygame.transform.scale(shrunk_image, (width, height))
                img_surface.blit(shrunk_image, (x, y))
            index += 1
    return img_surface

if __name__ == '__main__':
    loadFile("C:\\Program Files (x86)\\Audacity\\audacity.exe", "audacity_icon")
    loadFile("C:\\Program Files (x86)\\BioShock Infinite\\Launcher.exe", "bioshock_infinite")

    images = [imageFromFile('audacity_icon', 32, 32), imageFromFile('bioshock_infinite', 32, 32)]

    image = joinImages(images, 64, 64)
    pygame.image.save(image, "joined.bmp")
