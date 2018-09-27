#!/usr/bin/env python3
import socket

host = "127.0.0.1"
port = 27015

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)
sock, addr = s.accept()
print("client connected with address " + addr[0])
sock.send(b"Work Start")
file = open('server.py', 'a')
while True:
  buf = sock.recv(1024)
  buf = buf.rstrip()
  if buf.decode('utf8') == "exit":
    sock.send(b"bye")
    break
  elif buf:
    sock.send(buf[::-1])
    file.write(buf.decode('utf8'))
    print(buf.decode('utf8'))
sock.close()
