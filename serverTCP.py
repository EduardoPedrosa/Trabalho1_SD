#!/usr/bin/env python

import socket

IP = '127.0.0.1'
PORT = 5006

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
s.bind((IP, PORT))


while True:
    message, addr = s.recvfrom(1024)
    s.sendto(message, addr)

s.close()