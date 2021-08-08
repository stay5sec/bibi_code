# coding:utf-8
# author:stay5sec

import pandas as pd
import numpy as np

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

seed = np.random.RandomState(2)
x = seed.randint(100, size=30)

# print(type(x))
# print(x)
# exit()

# # 普通青年：排序 - 观察
# print(np.sort(x))
# exit()

# # 文艺青年：画图 - 观察
# import matplotlib.pyplot as plt
#
# plt.hist(x, rwidth=0.8)
# plt.show()
# exit()

# # 2B青年：定义函数
# def cut(i):
#     if i < 10:
#         y = [0, 10]
#     elif i > 10:
#         y = [10, 20]
#     # …………


# #斜杠青年：pd.cut
y = pd.cut(x, 6)
# print(y)
# exit()

# # 普通公司员工：美化
# y = pd.cut(x, 6)
# df=pd.DataFrame(pd.value_counts(y)).reset_index()
# print(df)
# exit()

# # 高级员工：优化
# y = pd.cut(x, 5, labels=["1 较小", "2 小值", "3 中间", "4 大值", "5 较大"])
# df = pd.DataFrame(pd.value_counts(y)).reset_index()
# df.columns = ["Flag", "计数"]
# df.sort_values("Flag", inplace=True)
# print(df)
# exit()

# 数据分析师
df = pd.DataFrame([x, y]).T
s1 = df.groupby(1).size()
s2 = df.groupby(1)[0].apply(lambda x: np.sort(list(x)))
df = pd.DataFrame([s1, s2]).T.reset_index()
df.columns = ["Flag", "计数", "具体数值"]
print(df)
