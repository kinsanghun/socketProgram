import threading
import socket

class TCPServ(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.clientAddress =clientAddress
        print("New connection added: ", clientAddress)

    def run(self):
        print("Connection From: ", self.clientAddress)
        msg = ""
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg == "quit":
                break
            print("From Client: ", msg)
            self.csocket.send(bytes(msg, "UTF-8"))
        print("Client at ", self.clientAddress, " disconnected...")