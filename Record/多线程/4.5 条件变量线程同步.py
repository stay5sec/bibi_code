# coding:utf-8
# author:stay5sec

import threading
from threading import Lock,Condition

# 4，使用Condition同步对话
class A(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="A")
        self.cond = cond

    def run(self):
        # 必须使用with语句
        with self.cond:
            # 被接收者需要先等待请求
            self.cond.wait()
            print("A：yes!")
            print("-" * 30)
            # 当接收者完事之后需要通知发起者
            self.cond.notify()

            self.cond.wait()
            print("A：yes2!")
            self.cond.notify()


class B(threading.Thread):
    def __init__(self,cond):
        super().__init__(name="B")
        self.cond=cond

    def run(self):
        with self.cond:
            print("B：are you A")
            # 发起者完事之后需要通知接收者
            self.cond.notify()
            # 当B问完之后需要等待A的通知
            self.cond.wait()


            print("B：are you sure")
            self.cond.notify()
            self.cond.wait()


cond = Condition()
# 继承对象的方式启动多线程
th1 = A(cond)
th2 = B(cond)

# 先启动A，再启动B（如果先启动B，由于A没有启动，会永久处于等待状态）
th1.start()
th2.start()

th1.join()
th2.join()

# 这时候会按照对话的形式把结果输出
'''
B：are you A
A：yes!
------------------------------
B：are you sure
A：yes2!
'''

# 也可以使用self.acquire启动多线程，但是需要用self.release掉
# cond.notify和wait方法只能在with语句之下执行
# condition有两层锁，底层锁会在线程调用了wait方法时释放
# 另外一把锁会在每次调用wait的时候分配一把锁，放在cond等待队列中，等到notify方法唤醒

exit()



# 3，使用lock同步对话，添加语句
class A(threading.Thread):
    def __init__(self, lock):
        super().__init__(name="A")
        self.lock = lock

    def run(self):
        self.lock.acquire()
        print("A：yes!")
        print("-" * 30)
        self.lock.release()

        self.lock.acquire()
        print("A：yes2!")
        self.lock.release()


class B(threading.Thread):
    def __init__(self,lock):
        super().__init__(name="B")
        self.lock=lock

    def run(self):
        self.lock.acquire()
        print("B：are you A")
        self.lock.release()

        self.lock.acquire()
        print("B：are you sure")
        self.lock.release()


lock = Lock()
# 继承对象的方式启动多线程
th1 = A(lock)
th2 = B(lock)

# 先启动B，再启动A
th2.start()
th1.start()

th1.join()
th2.join()

# 这时候会一次性把A或者B中的结果输出出来
'''
B：are you A
B：are you sure
A：yes!
------------------------------
A：yes2!
'''

exit()


# 2，使用lock同步对话
class A(threading.Thread):
    def __init__(self, lock):
        super().__init__(name="A")
        self.lock = lock

    def run(self):
        self.lock.acquire()
        print("A：yes!")
        self.lock.release()


class B(threading.Thread):
    def __init__(self,lock):
        super().__init__(name="B")
        self.lock=lock

    def run(self):
        self.lock.acquire()
        print("B：are you A")
        self.lock.release()


lock = Lock()
# 继承对象的方式启动多线程
th1 = A(lock)
th2 = B(lock)

# 先启动B，再启动A
th2.start()
th1.start()

th1.join()
th2.join()

# 第一次对象运行正常

exit()


# 1，最原始的状态
class A(threading.Thread):
    def __init__(self):
        super().__init__(name="A")

    def run(self):
        print("yes!")


class B(threading.Thread):
    def __init__(self):
        super().__init__(name="B")

    def run(self):
        print("are you A")
