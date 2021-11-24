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

# 一个点 / series
print(df.loc["a", "col1"])
print("\n")
print(type(df.loc["b":"c", "col1"]))
print("\n")

# 一行
print(df.loc["b"])
print("\n")

# 横向数据：多行
print(df.loc["a":"b"])
print("\n")
# 单行挑选
print(df.loc[[ "c","a"]])
print("\n")


