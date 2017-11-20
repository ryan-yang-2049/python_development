#!/usr/bin/env python3
#coding:utf-8

import socketserver
import os

class MyTCP(socketserver.BaseRequestHandler):
	def handle(self):
		while True:
			self.data = self.request.recv(1024).strip()
			if self.data == 'quit' or not self.data:
				break
			
			cmd=os.popen(self.data).read()
			if cmd == '':
				cmd = self.data + ':Command not found'
			self.request.sendall(cmd)



if __name__ == '__main__':
	HOST,PORT = '101.132.161.180',50007
	server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCP)
	server.serve_forver()

