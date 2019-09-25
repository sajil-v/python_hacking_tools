#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

ip_addr = "192.168.0.4"

for port in range (1,101):
    try:
        s = socket.socket()
        s.connect((ip_addr,port))
        s.send(b'Test, Data')
        data = s.recv(1024)
        s.close()
        print("Connected To Port : " + str(port))
        print("Received", repr(data))    
    except:
        pass
     