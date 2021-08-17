# coding:utf-8
# author:stay5sec

import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

import warnings

warnings.filterwarnings("ignore")

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@localhost:3306/sql2?charset=utf8')

# sql查询 查找所有已经分配部门的员工的last_name和first_name以及dept_no
sql = "select * from salaries "

sql1 = "select * from dept_manager"

df = pd.read_sql_query(sql, engine)

print("\n")
print(df)
print("\n")

df1 = pd.read_sql_query(sql1, engine)

print(df1)

# exit()

sql2 = """select a.emp_no,a.salary,a.from_date,a.to_date,b.dept_no 
from salaries a inner join dept_manager b on a.emp_no=b.emp_no 
order by a.emp_no;"""

df2 = pd.read_sql_query(sql2, engine)

print("\n")
print(df2)
