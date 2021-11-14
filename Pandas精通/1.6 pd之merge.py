# coding:utf-8
# author:stay5sec
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

df = pd.read_hdf("/Users/super/python/bili/data/jijin.h5")

print(df.head())
print("\n")

df1 = df.groupby("基金名称").size().reset_index()

print(df1.head())
print("\n")

df = pd.merge(df, df1, on="基金名称", how="left")

print(df.sample(5))