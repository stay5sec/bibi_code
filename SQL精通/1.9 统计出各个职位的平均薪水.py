# coding:utf-8
# author:stay5sec
# https://github.com/stay5sec/bibi_code

import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@localhost:3306/sql2?charset=utf8')

# 知识点：平均值
sql = '''select * from titles'''
df = pd.read_sql_query(sql, engine)

print("\n")
print(df)

sql1 = '''select * from salaries'''
df1 = pd.read_sql_query(sql1, engine)

print("\n")
print(df1)
print("\n")

sql2 = """select title,min(salary) 最小薪水 from titles a
            inner join salaries b on a.emp_no=b.emp_no 
            group by a.title; """

df2 = pd.read_sql_query(sql2, engine)

print(df2)
