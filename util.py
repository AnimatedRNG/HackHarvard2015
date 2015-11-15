SW_HIDE             =   0
SW_SHOWNORMAL       =   1
SW_NORMAL           =   1
SW_SHOWMINIMIZED    =   2
SW_SHOWMAXIMIZED    =   3
SW_MAXIMIZE         =   3
SW_SHOWNOACTIVATE   =   4
SW_SHOW             =   5
SW_MINIMIZE         =   6
SW_SHOWMINNOACTIVE  =   7
SW_SHOWNA           =   8
SW_RESTORE          =   9
SW_SHOWDEFAULT      =   10
SW_FORCEMINIMIZE    =   11
SW_MAX              =   11

from ctypes import windll
import pygame

def show():
    windll.user32.ShowWindow(pygame.display.get_wm_info()['window'], SW_SHOW)

def hide():
    windll.user32.ShowWindow(pygame.display.get_wm_info()['window'], SW_HIDE)
