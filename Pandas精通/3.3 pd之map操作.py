# coding:utf-8
# author:stay5sec
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

df = pd.DataFrame({'col1': ['1', '2', '3'],
                   'col2': ['one', 'two', 'one']})

print(df.info(), "\n")

df["map1"] = df["col1"].map(float)

print(df, "\n")

df["map2"] = df["col2"].map({"one": "一", "two": "贰"})

print(df, "\n")


def cal(x):
    if x > 2:
        return 'big'
    else:
        return 'small'


df["map3"] = df["map1"].map(cal)

print(df, "\n")
