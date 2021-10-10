# coding:utf-8
# author:stay5sec
# https://github.com/stay5sec/bibi_code

import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@localhost:3306/sql2?charset=utf8')

# 知识点：多表关联
sql = '''select * from film'''
df = pd.read_sql_query(sql, engine)

print("\n")
print(df.head())

sql = '''select * from category'''
df = pd.read_sql_query(sql, engine)

print("\n")
print(df.head())

sql = '''select * from film_category'''
df = pd.read_sql_query(sql, engine)

print("\n")
print(df.head())
print("\n")

# exit()


sql2 = """ select b.name,count(a.film_id)
              from (select * from film where description like "%%robot%%") a,category b, film_category c where 
             a.film_id=c.film_id and b.category_id=c.category_id
             group by name """

df2 = pd.read_sql_query(sql2, engine)

print(df2)
