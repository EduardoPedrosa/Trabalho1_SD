#!/usr/bin/env python

import socket
import threading

def createTCPSocket(ip, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #UDP
	s.bind((ip, port))
	s.listen(1)
	return s

def receiveMessages(conn):
	while(True):
		data = conn.recv(1024)
		if(not data):
			break
	conn.close()


def main():
	IP = '127.0.0.1'
	PORT = 5007

	s = createTCPSocket(IP, PORT)

	while True:
		conn, addr = s.accept()
		receiveMessagesThread = threading.Thread(target=receiveMessages, args=(conn,))
		receiveMessagesThread.start()



main()