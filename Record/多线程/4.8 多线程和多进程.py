# coding:utf-8
# author:Super

from concurrent.futures import ThreadPoolExecutor, as_completed
import time
# 导入进程模块
from concurrent.futures import ProcessPoolExecutor

# 有了多线程为啥还出现了多进程
'''
1，消耗CPU的操作，可以使用多进程并行运算
2，对于IO操作，瓶颈不在于CPU，进程切换性能代价高于线程，所以建议使用多线程
'''


# 耗费CPU的计算操作（科学计算/图像算法/挖矿）

# 斐波拉切
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# if __name__ == "__main__":
#
#     with ThreadPoolExecutor(3) as exe:
#         all_task = [exe.submit(fib, (num)) for num in range(25, 30)]
#
#         st = time.time()
#
#         for f in as_completed(all_task):
#             data = f.result()
#             print("exe result:{}".format(data))
#
#         print("time cost:{}".format(time.time()-st))

# ===============第2种写法===================

# if __name__ == "__main__":
#
#     # 使用多线程跑对于代码
#     with ThreadPoolExecutor(3) as exe:
#
#         st = time.time()
#
#         for data in exe.map(fib, range(25, 35)):
#             print("exe result:{}".format(data))
#
#         print("多线程耗时:{}".format(time.time() - st))
#         print("分割线".center(40, "-"))
#
#     # 对于计算而言：运行下来多进程快很多
#     with ProcessPoolExecutor(3) as exe:
#
#         st = time.time()
#
#         for data in exe.map(fib, range(25, 35)):
#             print("exe result:{}".format(data))
#
#         print("多进程耗时:{}".format(time.time() - st))


# 模拟IO操作


def random_sleep(n):
    time.sleep(n)
    return n


if __name__ == "__main__":

    # 对于IO而言：运行下来多线程切换快一些
    # 对于操作系统，开60个线程是比较轻松：多线程更加稳定
    with ThreadPoolExecutor(3) as exe:
        st = time.time()
        for data in exe.map(random_sleep, [3]*10):
            print("exe result:{}".format(data))
        print("多线程耗时:{}".format(time.time() - st))
        print("分割线".center(40, "-"))

    # 使用进线程跑对于代码
    with ProcessPoolExecutor(3) as exe:
        st = time.time()
        for data in exe.map(random_sleep, [3]*10):
            print("exe result:{}".format(data))
        print("多进程耗时:{}".format(time.time() - st))