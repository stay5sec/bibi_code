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
# sql = '''show tables;'''

# sql = "select * from employees order by hire_date desc"

# sql="select max(hire_date) from employees"

sql="select * from employees where hire_date in (select max(hire_date) from employees)"

df = pd.read_sql_query(sql, engine)

print(df)
