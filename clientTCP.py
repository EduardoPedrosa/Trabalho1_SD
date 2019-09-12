#!/usr/bin/env python

import socket
import time

tcp_ip = '127.0.0.1'
tcp_port = 5006

s = socket.socket(socket.AF_INET,
				socket.SOCK_DGRAM)
s.connect((tcp_ip, tcp_port))

times = []
total = 0
quantity = 20

for x in range(0, quantity):
	begin = time.time()
	s.send("a".encode())
	data = s.recv(1024) #Tamanho do buffer.
	end = time.time()
	parcialTime = (end-begin)/1000000
	print ("Atraso:", parcialTime, "ms")
	times.append(parcialTime)		
	total += parcialTime
	time.sleep(1)	

mean = total/quantity
print ("Média:", mean)
result = 0
for x in range(0, quantity):
	result += ((times[x] - mean) ** 2)
deviation = ((result/quantity) ** (1/2))
print ("Desvio padrão:", deviation)

s.close()
