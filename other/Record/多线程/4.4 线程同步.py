# coding:utf-8
# author:stay5sec

import dis

# # 示范案例
# def add(a):
#     a += 1
#
#
# def desc(a):
#     a -= 1
#
#
# print(dis.dis(add))
# print("分割".center(40, "-"))
# print(dis.dis(desc))

# add
'''
1，load a    a=0
2, load 1   1
3, +    1
4, 赋值给a    a=1
'''

# desc
'''
1，load a    a=0
2, load 1   1
3, -   -1
4, 赋值给a    a=-1
'''

# 当线程同步时，上述情景互相切换
# 前3部都没有什么问题，在第四部的时候
# 最后a=1还是a=-1，都是随机的，倒是数据结果不一致
# 案例：电商的减库存问题，多线程同时卖出东西

# ----------------------------------------------

# 同步锁Lock
import threading
from threading import Lock
import time

total = 0
lock = Lock()


def add2():
    global total

    # 声明一把锁
    global lock

    for i in range(1000000):
        # 获取锁
        lock.acquire()
        total += 1
        # 不释放就会卡住
        lock.release()


def desc2():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


start_time = time.time()
th1 = threading.Thread(target=add2)
th2 = threading.Thread(target=desc2)
th1.start()
th2.start()

th1.join()
th2.join()

print(total)

print("run time:", time.time() - start_time)

# 1，用锁会影响性能
# 2，锁会引起死锁（当出现两个acquire）

'''
A(a,b)
acquire(a)
acquire(b)

B(a,b)
acquire(a)
acquire(b)

'''


# 函数套用也会形成死锁，案例无需运行


def C(lock):
    lock.acquire()
    D(lock)
    lock.release()


def D(lock):
    lock.acquire()
    print("C has D")
    lock.release()

# 这之后运行C函数也会造成死锁，只要同时出现两个acquire

# ----------------------------------------------

# 可重入锁：RLock

# 同一个线程里可以连续调用多次acquire
# 一定要注意acquire和release次数一致

