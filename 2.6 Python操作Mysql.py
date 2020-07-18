# coding:utf-8
# author:stay5sec
# mysql本地的密码：root

import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

import warnings

warnings.filterwarnings("ignore")

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@localhost:3306/es?charset=utf8')

# # sql查询
# sql = '''select * from es_data2;'''
#
# # 数据提取
# df = pd.read_sql_query(sql, engine)
#
# print(df)
# exit()

# # 只查询5行
sql = '''select * from es_data limit 5;'''
# sql = '''select * from es_data2 limit 5,5;'''

# # WHERE 子句
# sql = '''select * from es_data2 where AvgTicketPrice > 900;'''

# # LIKE 子句
# sql = '''select * from es_data2 where OriginCityName like '%%City';'''

# # UNION 操作符
# sql = '''select * from es_data2 where DestCountry like 'AU' union select * from es_data2 where DestWeather like 'Rain';'''
#
# sql = '''select * from es_data2 where DestCountry like 'AU' or DestWeather like 'Rain';'''

# # 排序
# sql = '''select * from es_data2 order by AvgTicketPrice desc limit 10;'''

# # 分组
# sql = '''select DestCountry,count(*) from es_data2 group by DestCountry;'''

# # 多重分组
# sql = '''select DestCountry,DestWeather,count(*) from es_data2 group by DestCountry,DestWeather;'''

# # 聚合之后再筛选
# sql = '''select DestCountry,DestWeather,count(*) as c from es_data2 group by DestCountry,DestWeather having c > 25;'''

# # 正则表达式
# sql = '''select * from es_data2 where OriginCityName regexp 'New+';'''

df = pd.read_sql_query(sql, engine)

print(df)

