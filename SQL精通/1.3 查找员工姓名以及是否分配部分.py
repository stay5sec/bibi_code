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
sql = "select * from employees "

sql1 = "select * from dept_emp"

df = pd.read_sql_query(sql, engine)

print("\n")
print(df)
print("\n")

df1 = pd.read_sql_query(sql1, engine)

print(df1)

# exit()

sql2 = """select a.last_name,a.first_name,b.dept_no from employees a 
        left join dept_emp b on a.emp_no=b.emp_no;"""

df2 = pd.read_sql_query(sql2, engine)

print("\n")
print(df2)
