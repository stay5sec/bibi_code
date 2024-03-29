# coding:utf-8
# author:stay5sec

import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

import warnings

warnings.filterwarnings("ignore")

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@localhost:3306/sql2?charset=utf8')

# sql查询
sql = "select * from employees order by hire_date desc  "

sql1 = "select * from employees order by hire_date desc limit 2,2"

df = pd.read_sql_query(sql1, engine)

print(df)
