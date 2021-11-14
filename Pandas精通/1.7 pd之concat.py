# coding:utf-8
# author:stay5sec
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

import warnings

warnings.filterwarnings("ignore")

df = pd.read_hdf("/Users/super/python/bili/data/jijin.h5")

df = df[df.columns[-2:]]

print(df.head())
print("\n")

df1 = df.groupby("基金名称").size().reset_index()
# df1.rename(columns={"基金名称":"基金名称2"},inplace=True)

print(df1.head())
print("\n")

df2 = pd.concat([df.head(), df1.head()], ignore_index=True)

print(df2)
print("\n")

df3 = pd.concat([df.head(), df1.head()], axis=1)

print(df3)
