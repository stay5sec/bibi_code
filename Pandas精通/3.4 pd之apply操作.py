# coding:utf-8
# author:stay5sec
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

df = pd.DataFrame({'col1': ['1', '2', '3'],
                   'col2': ['one', 'two', 'one'],
                   'col3': [4, 5, 6],
                   })

print(df, "\n")

df["apply1"] = df["col1"].apply(lambda x: int(x))

print(df.info(), "\n")

df.loc["total"] = df[["col3", "apply1"]].apply(lambda x: x.sum(), axis=0)

# df["apply2"]=df["col3"]+df["apply1"]

# df["total"] = df[["col3", "apply1"]].apply(lambda x: x.sum(), axis=1)

print(df, "\n")


# def cal(x):
#     if x > 2:
#         return 'big'
#     else:
#         return 'small'
#
#
# df["apply2"] = df["apply1"].apply(lambda x: cal(x))
#
# print(df, "\n")

df["apply3"] = df["apply1"].apply(lambda x: 'big' if x >2 else 'small')

print(df, "\n")
