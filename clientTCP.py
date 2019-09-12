#!/usr/bin/env python

import socket
import time
import select

def deviation(quantity, mean, times):
	result = 0
	for x in range(0, quantity):
		result += ((times[x] - mean) ** 2)
	return ((result/quantity) ** (1/2))

def connectSocket(ip, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect((ip, port))
	s.setblocking(0)
	return s

def main():
	udp_ip = '192.168.0.113'
	udp_port = 5006

	s = connectSocket(udp_ip, udp_port)

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
	print ("Desvio padrão:", deviation(quantity, mean, times))

	s.close()

main()