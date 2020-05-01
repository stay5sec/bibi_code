# coding:utf-8
# author:stay5sec
import pandas as pd
from pymongo import MongoClient

# desk path：/Users/super/Desktop/

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

df = pd.read_excel("/Users/super/Desktop/es.xlsx")

# print(df.head())
# print("\n")

df_t = df.T.to_dict().values()

# print(df_t)
# exit()

# 初始化对象
conn = MongoClient()
table = conn.test.ttt3

table.insert_many(df_t)

