# coding:utf-8
# author:stay5sec
import pandas as pd
from collections import *

# desk path：/Users/super/Desktop/

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

from collections import UserList


list1=[[1,2,3],[2,3,4]]
df=pd.DataFrame(list1)
print(len(df))
exit()

print(list1.pop())
print(list1)
exit()


# import collections
#
# print(dir(collections))
#
# exit()


class A:
    def max(self, list1):
        return max(list1)


a = A()
print(a.max([1, 2, 3]))

exit()
a = [1, 2, 3]

a.append(4)

print(a)

exit()

s_data = input()

if s_data == "abc":
    print("test success!")
else:
    print(111)
exit()
a = ["a1", "a2"]
b = ["b1", "b2"]

a.extend(b)

a = list
