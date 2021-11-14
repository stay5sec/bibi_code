# coding:utf-8
# author:stay5sec
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

# desk path：/Users/super/Desktop/

df = pd.read_hdf("/Users/super/python/bili/data/jijin.h5")

# groupby的操作，以后再说
df = df.groupby("基金名称").head(2).head(4)

print(df)
print("\n")

df1 = df.pivot(index='基金名称', columns='股票名称', values='持股数')

print(df1)
print("\n")

# exit()

df["持股数"] = df["持股数"].str.replace(",", "").map(float)

df2 = pd.pivot_table(df, index="基金名称", columns="股票名称", values="持股数")
print(df2)
