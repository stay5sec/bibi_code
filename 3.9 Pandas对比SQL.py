# coding:utf-8
# author:stay5sec

import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

import warnings

warnings.filterwarnings("ignore")

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@localhost:3306/test?charset=utf8')

# sql查询
sql = '''select * from data0718;'''

# sql1=""" select uid,max(login_time) max_time from data0718 group by uid; """

df = pd.read_sql_query(sql, engine)

print(df)
print("\n")
# exit()

# # 取出登入最大值
# print(df.groupby("uid")["login_time"].max().reset_index())
# exit()

# 取出登入time最大值以及其他列
df = df.sort_values("login_time", ascending=0)

print(df.groupby("uid").first())