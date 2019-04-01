#!/usr/bin/env python

import socket

tcp_ip = '127.0.0.1'
tcp_port = 5006

s = socket.socket(socket.AF_INET,
				socket.SOCK_STREAM)
s.connect((tcp_ip, tcp_port))

while True:
	message = raw_input("Digite Sua Mensagem: ")
	s.send(message)

	data = s.recv(1024) #Tamanho do buffer.
	print "Mensagem recebida: ", data

s.close()
