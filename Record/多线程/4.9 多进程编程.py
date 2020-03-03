# coding:utf-8
# author:Super

import time

# import os
# pid = os.fork()
# print("abc")
# if pid == 0:
#     print("子进程{}，父进程：{}".format(os.getpid(), os.getppid()))
#
# else:
#     print("我是父进程：{}".format(pid))
# time.sleep(2)
#
# exit()

from concurrent.futures import ProcessPoolExecutor

import multiprocessing


# # multiprocessing中的一个进程
# # multiprocessing.process()
#
# def random_sleep(n):
#     time.sleep(n)
#     print("progress success!")
#     return n
#
#
# if __name__ == "__main__":
#     progress = multiprocessing.Process(target=random_sleep, args=(2,))
#
#     # 多进程多的一个属性
#     print(progress.pid)
#
#     progress.start()
#
#     # start之后就存在了
#     print(progress.pid)
#
#     progress.join()
#
#     print("progress end!")

# # 继承类的方法使用multiprocessing中的多进程

# class RS(multiprocessing.Process):
#     def __init__(self, n):
#         super().__init__()
#         self.n = n
#
#     def run(self) -> None:
#         time.sleep(self.n)
#         print("progress success!")
#         return self.n


# if __name__ == "__main__":
#     progress = RS(2)
#
#     # 多进程多的一个属性
#     print(progress.pid)
#
#     progress.start()
#
#     # start之后就存在了
#     print(progress.pid)
#
#     progress.join()
#
#     print("progress end!")


# 使用multiprocessing的进程池进行编程
def random_sleep(n):
    time.sleep(n)
    print("progress success!")
    return n


# if __name__ == "__main__":
#     pool = multiprocessing.Pool(multiprocessing.cpu_count())
#     result = pool.apply_async(random_sleep, args=(3,))
#
#     pool.close()
#     # 等待任务完成
#     pool.join()
#
#     print(result.get())

# 使用imap方法
if __name__ == "__main__":
    pool = multiprocessing.Pool(multiprocessing.cpu_count())

    # 按照添加的顺序输出
    for r in pool.imap(random_sleep, [1, 4, 2]):
        print(r)

    '''
    progress success!
    1
    progress success!
    progress success!
    4
    2
    '''
