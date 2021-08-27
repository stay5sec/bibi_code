# coding:utf-8
# author:stay5sec
# https://github.com/stay5sec/bibi_code

import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@localhost:3306/sql2?charset=utf8')

# 知识点：单表重复匹配
sql = '''select * from salaries'''
df = pd.read_sql_query(sql, engine)

print("\n")
print(df)

sql = '''select * from employees'''
df = pd.read_sql_query(sql, engine)

print("\n")
print(df)

sql2 = """select a.emp_no, (b.salary - c.salary) as growth
    from employees as a 
    inner join salaries as b
    on a.emp_no = b.emp_no and b.to_date = '9999-01-01'
    inner join salaries as c
    on a.emp_no = c.emp_no and a.hire_date = c.from_date
    order by growth asc """

df2 = pd.read_sql_query(sql2, engine)

print("\n")
print(df2)
