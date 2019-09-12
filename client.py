#!/usr/bin/env python

import socket
import time
import select

def deviation(quantity, mean, times):
	result = 0
	for x in range(0, quantity):
		result += ((times[x] - mean) ** 2)
	return ((result/quantity) ** (1/2))

def createSocketUDP():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.settimeout(0.030)
	return s

def createSocketTCP(ip, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	return s

def main():
	ip = '192.168.103.20'
	udp_port = 5006
	tcp_port = 5007

	s = createSocketUDP()

	times = []
	total = 0
	quantityOfTries = 20
	quantityOfSuccess = 0

	for x in range(0, quantityOfTries):
		begin = time.time()
		s.sendto(str(x).encode(), (ip, udp_port))
		try:
			while(True):
				data, addr = s.recvfrom(1024) #Tamanho do buffer.
				if(int(data.decode()) == x):			
					break	
			end = time.time()
			parcialTime = (end-begin) * 1000
			print ("Atraso:", parcialTime, "ms")
			times.append(parcialTime)
			quantityOfSuccess += 1		
			total += parcialTime
		except socket.timeout:
			print('timeout') 
		
		time.sleep(0.5)	
	s.close()
	
	print("Calculando vazão...")	

	word = 			"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	
	s = createSocketTCP(ip, tcp_port)	
	begin = time.time()
	for x in range(0, 10240):
		s.send(word.encode())
	end = time.time()
	throughput = 10 / (end-begin)

	if(quantityOfSuccess != 0):
		mean = total/quantityOfSuccess
		print ("Média:", mean,"ms")
		print ("Desvio padrão:", deviation(quantityOfSuccess, mean, times), "ms")
	print ("Número de pacotes perdidos:", quantityOfTries - quantityOfSuccess)
	print ("Vazão", throughput)

main()
