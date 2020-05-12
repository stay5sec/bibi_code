# coding:utf-8
# author:stay5sec

# requests -> urlib -> socket

# 运用场景：
# 1，数据库链接
# 2，进程之间的通信
# 3，网络之间的请求

# socket是操作系统提供的底层协议

import socket

from urllib.parse import urlparse


def get_url(url):
    # 通过socket请求html
    url = urlparse(url)

    # 提取主域名/路径
    host = url.netloc
    path = url.path

    if path == "":
        path = "/"

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect连接（host，端口）http都是80端口
    client.connect((host, 80))

    # 分别放入请求方式、host
    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(
        path, host).encode("utf8"))


    # 建立存储空间
    data = b""

    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break

    # 输出数据
    data = data.decode("utf8")
    print(data.split("\r\n\r\n")[1])
    client.close()


if __name__ == "__main__":
    get_url("http://www.baidu.com")

