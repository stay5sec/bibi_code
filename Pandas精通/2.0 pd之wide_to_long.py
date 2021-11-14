# coding:utf-8
# author:stay5sec
import pandas as pd

from Func import opath

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

# desk path：/Users/super/Desktop/

df = pd.DataFrame({"A1970": {0: "a", 1: "b", 2: "c"},
                   "A1980": {0: "d", 1: "e", 2: "f"},
                   "B1970": {0: 2.5, 1: 1.2, 2: .7},
                   "B1980": {0: 3.2, 1: 1.3, 2: .1}
                   })

df["id"] = df.index
print(df)
print("\n")


df2 = pd.wide_to_long(df, ["A", "B"], i="id", j="year")

print(df2.reset_index())
print("\n")

df3 = pd.wide_to_long(df, ["A1","B1"], i="id", j="year")

print(df3.reset_index())

