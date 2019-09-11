#!/usr/bin/env python

import socket
import time

tcp_ip = '127.0.0.1'
tcp_port = 5006

s = socket.socket(socket.AF_INET,
				socket.SOCK_STREAM)
s.connect((tcp_ip, tcp_port))

begin = time.time()
s.send("a".encode())
data = s.recv(1024) #Tamanho do buffer.
end = time.time()
print ("Tempo gasto: ", (end-begin)/1000000)

s.close()
