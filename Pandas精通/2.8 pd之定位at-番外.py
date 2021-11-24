# coding:utf-8
# author:stay5sec
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
                  index=[4, 5, 6], columns=['A', 'B', 'C'])

print(df)
print("\n")

# 选择
print("第一次挑选出来的数：", df.at[4, "B"])

print("第二次挑选出来的数：", df.iat[0, 1])

# df.at[4, "A"] = 88
# df.at[5, "B"] = 88
# df.at[6, "C"] = 88
#
# print("\n")
# print(df)

for i in range(3):
    df.iat[i, i] = 77

print("\n")
print(df)
