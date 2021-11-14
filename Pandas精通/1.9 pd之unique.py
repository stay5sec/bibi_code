# coding:utf-8
# author:stay5sec
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

import warnings

warnings.filterwarnings("ignore")

df = pd.DataFrame(['b', 'b', 'a', 'c', 'b'])

print(df.head())
print("\n")

codes, uniques = pd.factorize(df[0])

print("这是factorize产生的索引：", list(codes))
print("这是factorize产生的唯一值：", list(uniques))
print("-" * 40)

uniques2 = pd.unique(df[0])

print("这是unique产生的唯一值：", uniques2)
print("\n")

df2=pd.DataFrame(uniques2)

print(df2)

df2.reset_index(inplace=True)



df2=pd.merge(df,df2,on=0,how="left")

print(df2)

print("这是unique产生的索引：", list(df2["index"]))


