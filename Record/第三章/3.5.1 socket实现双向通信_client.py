# coding:utf-8
# author:stay5sec

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect连接（ip地址，端口）
client.connect(('127.0.0.1', 8000))

# 发送数据
client.send("five_sec".encode("utf8"))

# 获取从客户端发生的数据(一次获得1k数据)
data = client.recv(1024)

# 接收回来的是字符数据，需要转译
print(data.decode("utf8"))

client.close()
