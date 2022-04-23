from socket import *

#create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "localhost"
port = 5001
BUFSIZE = 1024

s.bind(address)
s.listen(5)

# Bind Error를 막기 위함?
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

while True:
    client, addr = s.accept()
    print("Connection requested from ", addr)
    client.send("Hello, How are you?".encode())
    client.close()
