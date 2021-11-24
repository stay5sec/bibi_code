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
print(df.at[4, "B"])

# 赋值
df.at[4, "B"] = 88
print("\n")
print(df)

# 选择
print("\n")
print(df.iat[0, 1])
