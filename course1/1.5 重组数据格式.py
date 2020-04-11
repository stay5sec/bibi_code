# coding:utf-8
# author:stay5sec
import pandas as pd

# desk path：/Users/super/Desktop/

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

df = pd.read_excel("/Users/super/Desktop/data.xlsx")

df["第一列"].fillna(method="ffill", inplace=True)

df["第一列"] = df["第一列"].apply(lambda x: int(x))

# print(df)
# exit()

s1 = df.groupby("第一列")["第二列"].apply(lambda x: list(x))

# print(type(s1))
# print("分割线".center(30,"-"))
# print(s1)
# exit()

dict1 = dict(s1)

# print("\n")
# print(dict1)

print(dict1[3])

