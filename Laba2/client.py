#!/usr/bin/env python3
import socket
import sys

class Client:
    host = None
    port = None
    sock = None

    def __init__(self, host = "127.0.0.1", port = 27015, massage = None):
        self.host = host
        self.port = port
        self.sockInit()
        if(massage != None):
            self.reception()
            self.transmition(massage)
        

    def sockInit(self):
        if self.host == None:
            return
        if self.port == None:
            return
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def reception(self):
        result = self.sock.recv(1024)
        return result.decode('utf8')
    
    def transmition(self, massage):
        self.sock.send(massage.encode('utf8'))


def main():
    port = None
    host = None
    massage = None
    if len(sys.argv) == 4:
        host = str(sys.argv[1])
        port = int(sys.argv[2])
        massage = sys.argv[3]
    else:
        host = input("input host")
        port = int(input("insert Port"))
        massage = input("input massage")
    client = Client(host, port, massage)
    while True:
        print(client.reception())
        client.transmition(input("Input massage :"))

main()