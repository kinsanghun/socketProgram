import socket
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', default="127.0.0.1")
parser.add_argument('-p', type=int, default=2500)
args = parser.parse_args()

address = (args.s, args.p)
BUFSIZE = 1024

#create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
err = s.connect_ex(address)

if not err:
    while True:
        msg = input("Message to Send : ")
        if not msg:
            continue
        if msg == 'q':
            break
        s.send(msg.encode())
        data = s.recv(BUFSIZE)
        print(f"Received message {data.decode()}")
    s.close()
else:
    print("ERROR CODE : ", err)
