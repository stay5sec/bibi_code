# coding:utf-8
# author:stay5sec
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

days = pd.date_range(start='2021-09-27', end='2021-10-09')

print(days)
exit()

df = pd.DataFrame(days, columns=["date_range"])

# print(df)

days2 = pd.bdate_range(start='2021-09-27', end='2021-10-09')

# print(days2)

days2 = [str(x)[:10] if x in days2 else "lost" for x in days]

df["bdate_range"] = days2

print(df)
