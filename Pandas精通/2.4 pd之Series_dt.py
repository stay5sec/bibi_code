# coding:utf-8
# author:stay5sec
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

days = pd.date_range(start='2021-12-31 23:59:30',
                      end='2022-01-01 00:00:20', freq="5s")

df = pd.DataFrame(days, columns=["time"])

print(df)
print("\n")

df["year"] = df["time"].dt.year
df["month"] = df["time"].dt.month
df["day"] = df["time"].dt.day
df["hour"] = df["time"].dt.hour
df["min"] = df["time"].dt.minute
df["second"] = df["time"].dt.second

print(df)
print("\n")

print(df.info())

