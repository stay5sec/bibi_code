# coding:utf-8
# author:stay5sec
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=['a', 'b', 'c'],
                  columns=['col1', 'col2'])

print(df)
print("\n")

# 一个点 / 多个点
print(df.iloc[1, 0])
print("\n")

print(df.iloc[:2, 1])
print("\n")


# 一行
print(df.iloc[0])
print("\n")
# 横向数据：多行 变成了df
print(df.iloc[0:2])
print("\n")

print(df.head(2))

