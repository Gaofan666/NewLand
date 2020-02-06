"""
客户端
"""

from socket import *
from time import sleep
 

c = socket()   # 创建套接字
ADDR = ('127.0.0.1',8888)   # 服务端地址

c.connect(ADDR) # 连接服务端

while True:
	data = input('请输入内容：')
	if not data:
		print('程序将在3秒后退出')
		sleep(3)
		break
	c.send(data.encode())
	data_ = c.recv(1024).decode()
	print('Server:',data_)

c.close()
