# coding:utf-8
# author:stay5sec

import pandas as pd
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

import warnings

warnings.filterwarnings("ignore")

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@localhost:3306/es?charset=utf8')

# engine = create_engine('mysql+pymysql://hadoop:mysql@localhost:3306/hive?charset=utf8')


df = pd.read_excel("/Users/super/Desktop/es.xlsx")

df.to_sql('es_data', engine, index=False, if_exists='append')




