# coding:utf-8
# author:stay5sec
import pandas as pd
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

# desk path：/Users/super/Desktop/

df = pd.read_hdf("/Users/super/python/bili/data/jijin.h5")

print(df.head())

print("\n")

# print(df.info())

# print(df.groupby("基金名称").size().head())

print(df[df["基金名称"]=="万家消费成长"])

