# coding:utf-8
# author:stay5sec
# https://github.com/stay5sec/bibi_code

import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@localhost:3306/sql2?charset=utf8')

# 知识点：判定奇偶数
sql = '''select * from employees'''
df = pd.read_sql_query(sql, engine)

print("\n")
print(df)

sql1 = '''select emp_no,emp_no&1 emp_no2 from employees'''
df1 = pd.read_sql_query(sql1, engine)

print("\n")
print(df1)
print("\n")

sql2 = """select * from employees
        where emp_no&1=1 and last_name!="Mary" 
        order by hire_date desc; """

df2 = pd.read_sql_query(sql2, engine)

print(df2)
