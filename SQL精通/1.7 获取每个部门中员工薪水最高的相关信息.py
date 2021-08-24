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

sql1 = '''select * from dept_emp'''

df1 = pd.read_sql_query(sql1, engine)

print("\n")
print(df1)
print("\n")
# exit()


sql2 = """select d.dept_no,d.emp_no,max(s.salary) as max_salary 
            from dept_emp d inner join salaries s 
            on d.emp_no=s.emp_no 
            group by d.dept_no; """

df2 = pd.read_sql_query(sql2, engine)

print(df2)
