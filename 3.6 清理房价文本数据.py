# coding:utf-8
# author:stay5sec
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

# desk path：/Users/super/Desktop/
# https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html

df = pd.read_csv(r'/Users/super/app/data/cal_housing.domain', sep=',', header=None)

# print(df)
# exit()

columns = list(df[0].apply(lambda x: x.split(":")[0]))

# print(columns)
# exit()

df2 = pd.read_csv(r'/Users/super/app/data/cal_housing.data', sep=',', header=None)

df2.columns = columns

# print(df2.head())
# exit()

print(df2.info())

df2.to_excel("/Users/super/Desktop/check.xlsx", index=False)
