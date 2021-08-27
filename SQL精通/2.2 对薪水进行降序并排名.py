# coding:utf-8
# author:stay5sec
# https://github.com/stay5sec/bibi_code

import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@localhost:3306/sql2?charset=utf8')

# 知识点：降序排名
sql = '''select * from salaries'''
df = pd.read_sql_query(sql, engine)

print("\n")
print(df)

sql1 = """select a.emp_no,a.salary, b.salary rank
            from salaries a,salaries b
            where a.salary <= b.salary
            """
df1 = pd.read_sql_query(sql1, engine)

print("\n")
print(df1)

df11=df1.groupby(["emp_no","salary"]).size()

print(df11)
exit()


sql2 = """select a.emp_no,a.salary,count(distinct b.salary) rank
            from salaries a,salaries b
            where a.salary <= b.salary
            group by a.emp_no order by rank; """

df2 = pd.read_sql_query(sql2, engine)

print("\n")
print(df2)
