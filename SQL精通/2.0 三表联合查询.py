# coding:utf-8
# author:stay5sec
# https://github.com/stay5sec/bibi_code

import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@localhost:3306/sql2?charset=utf8')

# 知识点：多表关联
sql = '''select * from employees'''
df = pd.read_sql_query(sql, engine)

print("\n")
print(df)

sql = '''select * from dept_emp'''
df = pd.read_sql_query(sql, engine)

print("\n")
print(df)

sql = '''select * from departments'''
df = pd.read_sql_query(sql, engine)

print("\n")
print(df)
print("\n")


sql2 = """select a.last_name,a.first_name,b.dept_name from employees a 
 left join (select * from dept_emp) c on a.emp_no=c.emp_no 
 left join (select * from departments) b on b.dept_no=c.dept_no """

df2 = pd.read_sql_query(sql2, engine)

print(df2)
