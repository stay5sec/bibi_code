# coding:utf-8
# author:stay5sec
import pandas as pd
from collections import *

# desk path：/Users/super/Desktop/

num = 63

print(num >> 1)

print(num << 1)

num2 = bin(num)

num20 = num2 + "0"

print(int(num20, 2))

exit()


def dec2bin(num):
    l = []
    if num < 0:
        return '-' + dec2bin(abs(num))
    while True:
        num, remainder = divmod(num, 2)
        l.append(str(remainder))
        if num == 0:
            return ''.join(l[::-1])


num = dec2bin(63)

print(int(num, 2))
