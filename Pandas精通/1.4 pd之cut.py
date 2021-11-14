# coding:utf-8
# author:stay5sec
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

# desk path：/Users/super/Desktop/

df = pd.DataFrame([range(1, 11)], index=["col"]).T
# print(df)
# exit()

df["cut"] = pd.cut(df["col"], 3)

# print(df)
# print("\n")

df["cut1"] = pd.cut(df["col"], bins=[3, 6, 8])

print(df)
print("\n")

df["cut2"] = pd.cut(df["col"], bins=[3, 6, 8], right=False)

print(df)
print("\n")

df["cut3"] = pd.cut(df["col"], bins=[3, 6, 8,10], labels=["小", "中","大"], right=False)

print(df)
print("\n")
