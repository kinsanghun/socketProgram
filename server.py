import socket

from TCPServer import TCPServ
import sys
import argparse
import threading
import TCPhandler

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', default="127.0.0.1")
    parser.add_argument('-p', type=int, default=2500)
    args = parser.parse_args()
    connections = []
    BUFSIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((args.s, args.p))
    print("Server Started")
    print("Waiting for client request..")

    while True:
        s.listen(1)
        clientsock, clientAddress = s.accept()
        t = TCPServ(clientAddress, clientsock)
        t.start()

if __name__ == "__main__":
    main()