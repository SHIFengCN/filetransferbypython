#!/usr/bin/env python  
# -*- coding: utf-8 -*-

""" 
@version: v1.0 
@author: SHIFengCN 
@license: Apache Licence  
@contact: shifree@gmail.com
@site: https://github.com/shifengcn 
@software: PyCharm 
@file: server.py 
@time: 2018/3/29 0029 14:06 
"""
import socket,subprocess,os
sk=socket.socket()
addr=('127.0.0.1',8801)
sk.bind(addr)
sk.listen(3)
while True:
	print('wait')
	conn,addr=sk.accept()
	while True:
		try:
			data=conn.recv(1024)
			if not data:break
			print(str(data,'utf8'))
			if str(data,'utf8')=='post':
				print('is post')
				conn.sendall(bytes('ready',encoding='utf8'))
				filename,filelength=str(conn.recv(1024),'utf8').split('|')
				print(filename,filelength)

				# readlenth=0
				data=bytes()
				while len(data)!=int(filelength):
					data+=conn.recv(1024)
					print(len(data))
				BASE_DIR=os.path.dirname(os.path.abspath(__file__))
				print(BASE_DIR)
				filepath=os.path.join(BASE_DIR,filename)
				print(filepath)
				outfile=open(filepath,mode="wb")
				outfile.write(data)
				outfile.close()





		except Exception:
			break
	#conn.close()




print('server_ok')