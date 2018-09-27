#!/usr/bin/env python3
import socket
import time
import sys

host = "127.0.0.1"
port = 27015

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
string = ''
argc = len(sys.argv)
if argc > 1:
    host = sys.argv[1]
    for i in sys.argv[2:]:
        string += i + ' '
    s.send(string.encode('utf8'))
while True:
    buf = input()
    s.send(buf.encode('utf8'))
    result = s.recv(1024)
    print('Ответ сервера: ', result.decode('utf8'))
    if buf == "exit":
        break
s.close()

time.sleep(10)

