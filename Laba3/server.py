#!/usr/bin/env python3
import socket
import sys
import re

class Server:
	host = None
	port = None
	sock = None
	conn = None
	addr = None

	def __init__(self, host = "127.0.0.1", port = 27015, massage = "Server Work\nHello"):
		self.host = host
		self.port = port
		self.sockInit()
		self.transmit(massage)
		
	
	def sockInit(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((self.host, self.port))
		self.sock.listen(5)
		self.conn, self.addr = self.sock.accept()
		print("client connected with address " + self.addr[0])

	def transmit(self, massage):
		if isinstance(massage, str):
			massage = massage[::-1]
		else:
			massage = str(massage)
		self.conn.send(massage.encode("utf8"))
	
	def reception(self):
		result = self.conn.recv(1024)
		return result.decode("utf8")

	def socClose(self):
		self.sock.close()
def main():
	print("Server")
	if len(sys.argv) == 4:
		host = sys.argv[1]
		port = int(sys.argv[2])
		massage = sys.argv[3]
		server = Server(host, port, massage)
	else:
		server = Server()
	pattern = (r'^[0-9]{1,19}[+,-,/,*][0-9]{1,19}')
	while True:
		rec = server.reception()
		expression = re.compile(pattern)
		if(expression.findall(rec)):
			rec = eval(rec)
		print(rec)
		server.transmit(rec)
	sock.close()

main()
