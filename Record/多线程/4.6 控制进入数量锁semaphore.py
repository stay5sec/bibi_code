# coding:utf-8
# author:stay5sec

# Semaphore 是用于控制进入数量的锁
# 文件读写：写一般只是用一个线程，读可以允许多个

import threading
import time


# 更新第二版
class A(threading.Thread):
    def __init__(self, a, sem):
        super().__init__()
        self.a = a

        # 传入第二个参数
        self.sem = sem

    def run(self) -> None:
        time.sleep(2)
        print("print A")
        self.sem.release()


class B(threading.Thread):
    # 继承父类的参数
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self) -> None:
        for i in range(20):
            # 对应线程里的acquire，需要在运行端release
            self.sem.acquire()

            a_thread = A("run {}".format(i), self.sem)
            a_thread.start()


if __name__ == "__main__":
    start_time = time.time()

    sem = threading.Semaphore(3)

    b = B(sem)
    b.start()

    print(time.time() - start_time)

'''
可以防止20个线程一次进入，可以3个3个进入
semaphore内部使用condition来完成功能
'''

exit()

# # 原始第一版
# class A(threading.Thread):
#     def __init__(self, a):
#         super().__init__()
#         self.a = a
#
#     def run(self) -> None:
#         time.sleep(2)
#         print("print A")
#
#
# class B(threading.Thread):
#     def run(self) -> None:
#         for i in range(20):
#             a_thread = A("run {}".format(i))
#             a_thread.start()
#
#
# if __name__ == "__main__":
#
#     start_time=time.time()
#
#     b = B()
#     b.start()
#
#     print(time.time()-start_time)
