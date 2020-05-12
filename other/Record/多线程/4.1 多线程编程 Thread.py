# coding:utf-8
# author:stay5sec

# 操作系统调度的最小单元是：进程
# 但是进程调度资源比较大，所以演化出：线程
# 线程依赖于我们的进程

# 对于IO操作来说：多线程和多进程差别不大

# 多线程案例 - 爬虫抓取数据：
# 抓取主页面的同时
# 抓取详情页的内容

import threading
import time

# 通过Thread实例化
def get_a():
    print("get a")
    time.sleep(2)
    print("finish a!")


def get_b():
    print("get b")
    time.sleep(2)
    print("finish b!")


# th1=threading.Thread(target=get_a)
# th2=threading.Thread(target=get_b)
#
# start_time=time.time()
#
# th1.start()
# th2.start()
#
# print(time.time()-start_time)
# exit()

# 我们创建了两个线程，但是程序中还存在一个主线程
# 线程之间是并行运行的，所以主线程立即打印出了结果

# ------------------------------------------------

# # 需求1:当主线程退出当时候，kill子进程
# th1 = threading.Thread(target=get_a)
# th2 = threading.Thread(target=get_b)
#
# # 设置为守护线程
# th1.setDaemon(True)
# th2.setDaemon(True)
#
# start_time = time.time()
#
# th1.start()
# th2.start()
#
# print(time.time() - start_time)

# ------------------------------------------------

# # 需求2：子线程运行完再运行主线程 join方法
# th1 = threading.Thread(target=get_a)
# th2 = threading.Thread(target=get_b)
#
#
# start_time = time.time()
#
# th1.start()
# th2.start()
#
# # 设置阻塞
# th1.join()
# th2.join()
#
# print(time.time() - start_time)

# --------------------继承Thread用类方法--------------------------


class A(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get a")
        time.sleep(2)
        print("finish a!")


class B(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get b")
        time.sleep(3)
        print("finish b!")


start_time = time.time()
th1 = A("a")
th2 = B("b")

th1.start()
th2.start()

th1.join()
th2.join()

print(time.time() - start_time)
