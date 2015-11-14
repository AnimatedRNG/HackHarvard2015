import socket
import sys
from thread import *

HOST = ''
PORT = 25525


def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')

    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    s.listen(2)
    return s


def acceptCommand(s):
    print('Socket now listening')
    while True:
        conn, addr = s.accept()
        print('Connected with ' + addr[0] + ':' + str(addr[1]))

        while True:
            try:
                res = conn.recv(1024)
            except socket.error as msg:
                yield('Disconnected')
                return
            print('Received ' + str(res))
            yield(res)


def closeSocket(s):
    s.close()


def start():
    s = setupServer()
    start_new_thread(run, (s,))


def run(s):
    command = acceptCommand(s)
    while True:
        command_string = next(command)
        if command_string == 'Disconnected':
            print('Disconnected')
            return
        # do something with the command


if __name__ == "__main__":
    start()
    while 1:
        pass
