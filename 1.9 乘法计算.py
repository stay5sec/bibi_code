# coding:utf-8
# author:Super
import random

# print(random.randint(1, 9))
# exit()

# count = 1
# str = ""
# for i in range(36):
#     a = random.randint(1, 9)
#     b = random.randint(1, 9)
#     if count == 4:
#         str += "{} x {} =    \n".format(a, b)
#         count = 1
#     else:
#         str += "{} x {} =     ".format(a, b)
#         count += 1
#
# print(str)
# exit()

# # 第一种情况：去除完全一样的
# set1 = set()
# while True:
#     a = random.randint(1, 9)
#     b = random.randint(1, 9)
#
#     str = "{} x {}".format(a, b)
#
#     set1.add(str)
#
#     if len(set1) > 4:
#         print(set1)
#         break
# exit()

# 第二种情况：去除对称的
# a = "4 x 8"
# a = a[::-1]
#
# print(a)
# exit()

# set1 = set()
# while True:
#     a = random.randint(1, 9)
#     b = random.randint(1, 9)
#
#     str = "{} x {}".format(a, b)
#
#     if str[::-1] not in set1:
#         set1.add(str)
#
#     if len(set1) > 8:
#         break
#
# print(set1)
# exit()

# # 优化输出
# set1 = set()
# while True:
#     a = random.randint(1, 9)
#     b = random.randint(1, 9)
#
#     str = "{} x {}".format(a, b)
#
#     if str[::-1] not in set1:
#         set1.add(str)
#
#     if len(set1) > 35:
#         break
#
# count = 1
# str = ""
# for i in set1:
#     if count % 4 == 0:
#         str += "{} =    \n".format(i)
#     else:
#         str += "{} =     ".format(i)
#     count += 1
#
# print(str)
# exit()

# 封装函数

def cal(n, st=1):
    set1 = set()
    while True:
        a = random.randint(st, 9)
        b = random.randint(st, 9)

        str = "{} x {}".format(a, b)

        if str[::-1] not in set1:
            set1.add(str)

        if len(set1) > n - 1:
            break

    count = 1
    str = ""
    for i in set1:
        if count % 4 == 0:
            str += "{} =    \n".format(i)
        else:
            str += "{} =     ".format(i)
        count += 1

    print(str)


cal(5, 1)

print("分割线".center(40, "-"))

cal(36, 2)
