import SocketServer
import sys
import pygame
from pygame.locals import *
from display2 import Renderer2
from thread import *
import time
from ctypes import windll
import util

HOST = 'localhost'
PORT = 25525
LISTEN = 1000

renderer = None

def setupServer():
    """s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')

    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()`

    s.listen(LISTEN)"""
    print("Setting up TCP server")
    s = SocketServer.ThreadingTCPServer((HOST, PORT), TCPHandler)
    s.serve_forever()

class TCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):

        print("Connection established")
        while True:
            self.data = self.request.recv(1024).strip()
            print("Received: " + str(self.data))
            start_new_thread(commandReceived, (self.data,))


def start():
    setupServer()


def launchClient():
    import subprocess
    subprocess.call("bin/client.exe")


def commandReceived(command_string):
    if command_string == 'Disconnected':
        print('Disconnected')
        return
    if command_string == 'op':
        print('Show window!')
        util.show()
    elif command_string == 'cl':
        print('Attempting to minimize window')
        util.hide()
        renderer.resetAll()
    else:
        renderer.select(command_string)


if __name__ == "__main__":
    start_new_thread(start, ())
    time.sleep(1)
    start_new_thread(launchClient, ())
    renderer = Renderer2()
    renderer.start()
