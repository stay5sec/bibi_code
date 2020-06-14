# coding:utf-8
# author:stay5sec
import pandas as pd
from collections import defaultdict, Counter

# desk path：/Users/super/Desktop/
print("\n")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

list1 = ["a", "b", "c", "a", "a", "b"]

# # 常规统计方式
# dict1 = {}
#
# for l in list1:
#     if l not in dict1:
#         dict1[l] = 1
#     else:
#         dict1[l] += 1
#
# print(dict1)
# exit()

# # defaultdict方法
# dict1 = defaultdict(int)
#
# for l in list1:
#     dict1[l] += 1
#
# print(dict1)
# exit()

# # pandas 方法
# s1 = dict(pd.Series(list1).reset_index().groupby(0).size())
#
# print(s1)
#
# exit()

# Counter方法
count = Counter(list1)
print(count)

for k, v in count.items():
    print(k, "-->", v)
