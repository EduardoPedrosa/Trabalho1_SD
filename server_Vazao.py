#!/usr/bin/env python

import socket

IP = '127.0.0.1'
PORT = 5007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #UDP
s.bind((IP, PORT))
s.listen(1)

conn, addr = s.accept()

while True:
	data = conn.recv(1024)

conn.close()
