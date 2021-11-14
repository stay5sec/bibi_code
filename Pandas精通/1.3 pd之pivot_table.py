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

df2 = pd.melt(df, id_vars=['基金名称'], value_vars=['股票名称'])

print(df2)
print("\n")

df3 = pd.pivot_table(df2, index="基金名称", columns="variable", values="value", aggfunc=list)
print(df3.reset_index())