# coding:utf-8
# author:stay5sec

import threading
import time
from queue import Queue


# 抓取url同时可以把抓取到的url下方到另一个爬虫中去，
# 假设抓取url一次，一个url列表中含有三个详情页

# 抓取列表
def get_a(queue):
    # 添加元素
    for i in range(10):
        queue.put(i)
    time.sleep(2)
    print("主程序运行完毕!")


# 抓取详情
def get_b(queue):
    i = queue.get()
    time.sleep(3)
    print("完成线程 {}!".format(i))


if __name__ == "__main__":

    queue = Queue(maxsize=1000)

    start_time = time.time()

    # url线程开启一个
    th1 = threading.Thread(target=get_a, args=(queue,))

    # [主]线程必须先开启
    th1.start()

    th2 = 0
    # 遍历三个子线程，并且开启
    for i in range(8):
        th2 = threading.Thread(target=get_b, args=(queue,))
        th2.start()

    # 阻碍所有线程
    th1.join()
    th2.join()

    print(time.time() - start_time)
