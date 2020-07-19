# coding:utf-8
# author:stay5sec
import os
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

import warnings

warnings.filterwarnings("ignore")

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@localhost:3306/sql1?charset=utf8')

# sql查询
sql = '''show tables;'''

df = pd.read_sql_query(sql, engine)

# print(df)
# print("\n")
# exit()

# for i in list(df["Tables_in_sql1"]):
#     print(i)
#
# exit()

data_path = "/Users/super/python/bili/data/"

for i in list(df["Tables_in_sql1"]):
    sql1 = """ select * from {} """.format(i)
    df = pd.read_sql_query(sql1, engine)
    df.to_excel(os.path.join(data_path, i + ".xlsx"), index=False)
    print("{}表-存放完毕……".format(i))
