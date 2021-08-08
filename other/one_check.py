# coding:utf-8
# author:stay5sec
import pandas as pd
import datetime

# desk path：/Users/super/Desktop/

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

df = pd.read_excel("/Users/super/Desktop/电脑/Material/one_check.xlsx")

df["per"] = (df["三个月一次"] - df["三个月一次"].shift(1)) / df["三个月一次"]

# other_per = (df.loc[1, "剩余"] - df["三个月一次"].sum()) / df.loc[1, "剩余"]

mouth = df["一个月一次"].mean()

df2 = pd.DataFrame()

y = 2021
m = 0

count = 1
for i in range(1, 121):
    df2.loc[i, "第X个月"] = i

    df2.loc[i, "每月递减"] = int(mouth)

    m += 1
    if m % 3 == 0:
        df2.loc[i, "季度递减"] = df.loc[6, "三个月一次"]
        # *pow(1 + df.loc[6, "per"], count)
        count += 1
    else:
        df2.loc[i, "季度递减"] = 0

    df2.loc[i, "time"] = i % 12

    df2.loc[i, "time2"] = "{}-{}".format(y, int(df2.loc[i, "time"]))

    if df2.loc[i, "time"] >= 11:
        y += 1

df2["del"] = df2["每月递减"] + df2["季度递减"]

df2["cumsun"] = df2["del"].cumsum()

df2["剩余"] = df.loc[0, "剩余"] - df2["cumsun"]

df2["单价"] = (df.loc[0, "剩余"] * df.loc[2, "剩余"]) / 100 / df2["剩余"]

df2["单价2"] = 200 * pow(10, 8) / df2["剩余"]

print(df2)

df2.to_excel("/Users/super/Desktop/df2.xlsx",index=False)
