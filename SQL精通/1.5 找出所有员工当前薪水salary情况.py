# coding:utf-8
# author:stay5sec
# https://github.com/stay5sec/bibi_code

import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@localhost:3306/sql2?charset=utf8')

# sql查询
sql = '''select * from salaries'''

df = pd.read_sql_query(sql, engine)

print("\n")
print(df)
print("\n")
# exit()

sql1 = "select salary from salaries group by salary order by salary desc"

df1 = pd.read_sql_query(sql1, engine)

print(df1)
