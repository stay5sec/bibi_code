# coding:utf-8
# author:stay5sec
import pandas as pd

from Func import opath

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

d = {'col1': [1, 2], 'col2': [3, 4]}

df = pd.DataFrame(data=d)

print(df)
print("\n")

df.to_excel(opath("df.xlsx"))


df2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                   columns=['a', 'b', 'c'],index=[1,3,5])

print(df2)
df2.to_excel(opath("df2.xlsx"))
