# coding:utf-8
# author:stay5sec

import threading
import time

# 抓取url同时可以把抓取到的url下方到另一个爬虫中去，
# 假设抓取url一次，一个url列表中含有三个详情页

url_list = []


# 抓取列表
def get_a():
    global url_list

    # 往列表中添加元素
    for i in range(3):
        url_list.append(i)
    time.sleep(2)
    print("finish url!")


# 抓取详情
def get_b():
    global url_list

    # 提取list中的元素
    if url_list:
        i = url_list.pop()
    time.sleep(3)
    print("finish {}!".format(i))


start_time = time.time()

# url线程开启一个
th1 = threading.Thread(target=get_a)

# [主]线程必须先开启
th1.start()

th2 = 0
# 遍历三个子线程，并且开启
for i in range(3):
    th2 = threading.Thread(target=get_b)
    th2.start()

# 阻碍所有线程
th1.join()
th2.join()

print(time.time() - start_time)

# ======== 最后消耗的时间大约为3秒 =============

# 当我们使用共享变量这种方法时
# 会引用list这种可变的数据格式
# 导致多线程运作是线程不安全的

# 共享变量不推荐用于多线程操作