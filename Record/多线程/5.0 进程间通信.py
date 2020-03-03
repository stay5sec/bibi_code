# coding:utf-8
# author:Super

# 多进程编程中不能再使用线程中的queue
'''from queue import Queue'''

import time
from multiprocessing import Process, Queue, Pool

'''参数共享的方式'''
# def pro(queue):
#     queue.put("a")
#     time.sleep(2)
#
#
# def con(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
#
# if __name__ == "__main__":
#     queue = Queue()
#     my_producer = Process(target=pro, args=(queue,))
#     my_consumer = Process(target=con, args=(queue,))
#
#     my_producer.start()
#     my_consumer.start()
#
#     my_producer.join()
#     my_consumer.join()

'''共享全局变量'''
#
# def pro(a):
#     a += 1
#     time.sleep(2)
#
#
# def con(a):
#     time.sleep(2)
#     print(a)
#
#
# if __name__ == "__main__":
#     a = 1
#     my_producer = Process(target=pro, args=(a,))
#     my_consumer = Process(target=con, args=(a,))
#
#     my_producer.start()
#     my_consumer.start()
#
#     my_producer.join()
#     my_consumer.join()
#
# # 输出结果仍然是1：多进程中不能使用共享全局变量

'''multiprocessing中的queue不能用于pool进程池通信'''

# def pro(queue):
#     queue.put("a")
#     time.sleep(2)
#
#
# def con(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)


# if __name__ == "__main__":
#     queue = Queue()
#
#     pool = Pool(2)
#
#     pool.apply_async(pro, args=(queue,))
#     pool.apply_async(con, args=(queue,))
#
#     pool.close()
#     pool.join()
#
#     # 输出为空，多进程这个queue通信失效了

'''使用manager中的queue进行通信'''

# from multiprocessing import Manager
#
# if __name__ == "__main__":
#     queue = Manager().Queue()
#
#     pool = Pool(2)
#
#     pool.apply_async(pro, args=(queue,))
#     pool.apply_async(con, args=(queue,))
#
#     pool.close()
#     pool.join()
#
#     # 输出结果为“a”


'''通过pipe进行进程间的通信'''

# from multiprocessing import Pipe
#
# def pro(pipe):
#     pipe.send("a")
#
# def con(pipe):
#     print(pipe.recv())
#
# if __name__ == "__main__":
#     rece, send = Pipe()
#
#     # Pipe的参数传入函数
#     my_producer = Process(target=pro, args=(send,))
#     my_consumer = Process(target=con, args=(rece,))
#
#     my_producer.start()
#     my_consumer.start()
#
#     my_producer.join()
#     my_consumer.join()
#
#     # Pipe的性能，是高于queue的

'''使用全局变量进行进程通信'''

from multiprocessing import Manager


def add_data(dict1, k, v):
    dict1[k] = v


if __name__ == "__main__":
    pro_dict = Manager().dict()

    one = Process(target=add_data, args=(pro_dict, "a", 1))
    two = Process(target=add_data, args=(pro_dict, "b", 2))

    one.start()
    two.start()

    one.join()
    two.join()

    print(pro_dict)
