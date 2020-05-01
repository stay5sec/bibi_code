# coding:utf-8
# author:Super

import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

from prettytable import PrettyTable

file = "/Users/super/Desktop/一份假数据.xlsx"

df = pd.read_excel(file)

# print(df)
# print("\n\n")
# exit()

# table = PrettyTable(['name', 'username', 'sex'])
# table.add_row(['胡桂芝', 'vcai', 'F'])
# table.add_row(['胡建', 'qianghan', 'M'])
# print(table)
# exit()


# # 取出所有列的列名
# print(df.columns)
# print(type(df.columns))
# exit()

# # 取出df中的行
# print(df.loc[0, :])
# exit()

# table = PrettyTable(list(df.columns))
# for i in range(df.shape[0]):
#     table.add_row(df.loc[i, :])
#
# print(table)
#
# exit()


# # ========更改这个类==============
# # print(df.values.tolist())
# # exit()
#
# table = PrettyTable(list(df.columns))
#
# table.add_df(df.values.tolist())
#
# print(table)
# exit()

# 计算大表add_row时间
import time

st = time.time()
# table = PrettyTable(list(df.columns))
#
# for j in range(200):
#     for i in range(df.shape[0]):
#         table.add_row(df.loc[i, :])
#
# print(table)
#
# print("消耗时间：{}".format(time.time()-st))

# =============建立一个大表==================
df2 = pd.DataFrame()
for j in range(100):
    df2 = df2.append(df, ignore_index=True)

print(df2.shape[0])

import time

st = time.time()

table = PrettyTable(list(df.columns))

table.add_df(df2.values.tolist())

print(table)

print("消耗时间：{}".format(time.time()-st))

