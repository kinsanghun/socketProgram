import socket

#create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ("localhost", 5001)
#connect to server
s.connect_ex(address)

#s.send()
print("Time : ", s.recv(1024).decode())

