# coding:utf-8
# author:stay5sec
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

# desk path：/Users/super/Desktop/

# cut(): 先划分成等宽的桶，然后将数据填充到所属的桶中，导致每个桶中数据的个数有多有少
# qcut():首先对数据进行排序，然后等宽分桶，每个桶内的数据量一样多

df = pd.DataFrame([1, 2, 3, 7, 8, 9], columns=["col"])
# df = pd.DataFrame([1, 2, 3, 4, 5, 6], columns=["col"])

# 1-3, 4-6, 7-9
df["cut"] = pd.cut(df["col"], 3)

# print(df)
print("\n")

# 1-2, 3-7, 8-9
df["cut2"] = pd.qcut(df["col"], 3)

print(df)
