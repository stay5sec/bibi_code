#!/usr/bin/env python
# coding: utf-8

# GIL：global interpreter lock(base cpython)  
# python中的一个县城对应于C语音中的一个线程  
# GIL使得同一个时刻只有一个线程在一个cpu上执行字节码


import dis


def add(a):
    a += 1
    return a


dis.dis(add)

# 以上为函数变成字节码的流程：为了其安全python给这个流程加个一个锁

# 以上操作让python运行变慢，并且无法将多个线程映射到多个cpu上

# 有了这把锁，就无法利用电脑的多核优势

# ### 一个线程运行也不见得安全


import threading

total = 0


def add():
    global total
    for i in range(1000000):
        total += 1


def desc():
    global total
    for i in range(1000000):
        total -= 1


th1 = threading.Thread(target=add)
th2 = threading.Thread(target=desc)
th1.start()
th2.start()

th1.join()
th2.join()

total


# 这个total在多次运行之后的值是不固定的，也不是为0

# 两个线程在字节码运行的时候会不断释放total这个变量  
# 使得total在add中运行一了一段时间之后又进入到desc

# gil会根据执行的字节码行数以及时间片释放全局变量 


def add2():
    # do something
    # IO操作
    # dosomething
    pass

# gil在遇到IO操作的时候会主动释放全局变量
