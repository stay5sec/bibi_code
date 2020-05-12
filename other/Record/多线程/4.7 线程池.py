# coding:utf-8
# author:stay5sec

from concurrent.futures import ThreadPoolExecutor, as_completed

# 是否存在一个包可以让我们管理线程更加容易？

# semaphore和线程池功能区别
'''
1，获取某一个线程的状态或者任务状态，以及返回值
2,futures可以让多线程和多进程编码接口一致
'''

import time


def get_a(st):
    time.sleep(st)
    print("finish {} sec!".format(st))
    return "result"


# # =================单次提交===========================

# 实例化的参数：表示同时可运行的线程数量
exe = ThreadPoolExecutor(2)

# # 通过submit函数提交执行的函数到线程池
# task1 = exe.submit(get_a, (3))
# task2 = exe.submit(get_a, (2))
#
# # 第一次执行的时候没有执行完，所有输出False
# print(task1.done())
#
# # 可以用cancel取消未执行的任务,也返回True or False
# print(task2.cancel())
#
# time.sleep(4)
# # 延迟过后执行完毕，所有输出True，用于判断
# print(task1.done())
#
# # rusult可以获取task的执行结果
# print(task1.result())

# ======================多次提交===================

urls = [3, 2, 4]

# all_task = [exe.submit(get_a, (url)) for url in urls]
#
# for f in as_completed(all_task):
#     data = f.result()
#     print(data)

# ======================多次提交 2===================

for data in exe.map(get_a, urls):
    print(data)
