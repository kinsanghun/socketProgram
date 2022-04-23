import threading
import TCPServer

class Handler(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.BUFSIZE = 2014

        print("How Connection added ", clientAddress)

    def handler(self, c, a):
        while True:
            data = c.recv(2014)
            print("data : ", repr(data))
            if not data: break
            print("Received message : ", data.decode())
            c.send(data)

    def run(self):
        print("Connection From ", client,)