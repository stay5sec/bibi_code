# coding:utf-8
# author:stay5sec
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

print(df)
print("\n")

df = df.T

print(df)
print("\n")
# exit()

df.insert(1, 2, [88, 88])

print(df)
print("\n")

df = df.T

print(df)
