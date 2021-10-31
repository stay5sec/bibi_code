# coding:utf-8
# author:stay5sec
import pandas as pd

from Func import opath

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

# desk path：/Users/super/Desktop/

df = pd.read_hdf("/Users/super/python/bili/data/jijin.h5")

# df=df.groupby("基金编码").head(10)
#
# print(df.head())
#
# print("\n")


df = df[df["股票名称"].str.contains("TTT")]

df.reset_index(drop=True,inplace=True)

print(df)


