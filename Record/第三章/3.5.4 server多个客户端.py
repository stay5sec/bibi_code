# coding:utf-8
# author:stay5sec
import threading
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind内需要传递tuple（ip地址，端口）
server.bind(('0.0.0.0', 8000))

# 时刻监听
server.listen()


def handle_sock(sock, addr):
    # 获取从客户端发生的数据(一次获得1k数据)
    data = sock.recv(1024)

    # 接收回来的是字符数据，需要转译

    data = data.decode("utf8")

    print(data)

    if data == 'C: bye':
        return 1

    s_data = input()

    # 输入信息进行返回
    sock.send("S: {}".format(s_data).encode("utf8"))


while True:
    # 接收请求
    sock, addr = server.accept()

    client_thread = threading.Thread(target=handle_sock,
                                     args=(sock, addr))

    client_thread.start()

# server.close()
# sock.close()
