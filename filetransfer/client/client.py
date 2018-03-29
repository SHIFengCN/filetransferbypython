#!/usr/bin/env python  
# -*- coding: utf-8 -*-

""" 
@version: v1.0 
@author: SHIFengCN 
@license: Apache Licence  
@contact: shifree@gmail.com
@site: https://github.com/shifengcn 
@software: PyCharm 
@file: client.py 
@time: 2018/3/29 0029 14:17 
"""

import socket,os
sk_client=socket.socket()
addr=('127.0.0.1',8801)
sk_client.connect(addr)
while True:
	inp=input(">>>")
	if inp=="exit":break
	#sk_client.sendall(bytes(inp,'utf8'))
	sk_client.sendall(bytes(inp,'utf8'))

	ret=sk_client.recv(1024)
	print(str(ret,"utf8"))
	if str(ret,"utf8")=='ready':
		filelength=os.stat("11.jpg").st_size
		print("filelenth=",str(filelength))
		sendlength=0
		upfile=open(r"C:\Users\shifeng\Desktop\11.jpg",'rb')
		#print(upfile)
		sk_client.sendall(bytes("11.jpg|"+str(filelength),'utf8'))
		while sendlength!=filelength:
			data=upfile.read(1024)
			sk_client.sendall(data)
			sendlength+=len(data)
		upfile.close()

sk_client.close()