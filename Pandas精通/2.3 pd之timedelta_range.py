# coding:utf-8
# author:stay5sec
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

freq = pd.timedelta_range(start='0 day', end='1 days', freq='6H')

days = pd.date_range(start='2017-10-01', end='2017-10-05')

days2 = pd.date_range(start='2017-10-01', end='2017-10-02',freq="6H")

df2=pd.DataFrame(days2,columns=["days2"])

print(df2)
exit()

df = pd.DataFrame([freq, days], index=["时间差", "days"]).T

df.insert(1, "spl", ["|"] * 5)

df["finally_time"] = df["days"] + df["时间差"]

df.insert(3, "spl2", ["|"] * 5)

print(df)
print("\n")
