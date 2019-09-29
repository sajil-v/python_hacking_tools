#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *

ip_addr = input ("Enter IP Address : ")
port_start = int(input ("Enter starting Port Number : "))
port_end = int(input ("Enter Ending Port Number : "))

print ("Scanning IP : " + ip_addr)

for port in range(port_start,port_end):
    #print ("Scanning Port : " + str(port))
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(5)
    if(s.connect_ex((ip_addr, port)) == 0):
        print ("Connection Opened at " + str(port))
    s.close()

print("Scanning Done !!!")