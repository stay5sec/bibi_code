# coding:utf-8
# author:stay5sec


import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind内需要传递tuple（ip地址，端口）
server.bind(('0.0.0.0', 8000))

# 时刻监听
server.listen()

# 接收请求
sock, addr = server.accept()

# 获取从客户端发生的数据(一次获得1k数据)
data = sock.recv(1024)

# 接收回来的是字符数据，需要转译
print(data.decode("utf8"))

# 接收完了之后再返回信息
sock.send("has receive {}!".format(data.decode("utf8")).encode("utf8"))

# 首先需要将字节码【编译】成数据
# 然后将合并数据再【解码】为字节码

server.close()
sock.close()
