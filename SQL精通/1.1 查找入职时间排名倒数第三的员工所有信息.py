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
sql = "select * from employees order by hire_date desc limit 2,1"


df = pd.read_sql_query(sql, engine)

print(df)
