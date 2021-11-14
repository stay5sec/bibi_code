# coding:utf-8
# author:stay5sec
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

months = pd.period_range(start='2017-10-02', end='2018-02-01', freq='M')

df = pd.DataFrame(months, columns=["months"])

df["years"] = pd.period_range(start='2016-10-01', end='2020-02-01', freq='Y')

df["days"] = pd.period_range(start='2016-10-01', end='2016-10-05', freq='D')


print(df)
