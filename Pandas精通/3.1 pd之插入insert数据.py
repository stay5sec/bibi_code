# coding:utf-8
# author:stay5sec
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

print(df)
print("\n")

df.insert(1, "newcol", [99, 99])

print(df)
print("\n")

df.insert(3, "newcol", [100, 100], allow_duplicates=True)

print(df)
print("\n")

df.insert(0, "col0", pd.Series([5, 6], index=[1, 2]))

print(df)



