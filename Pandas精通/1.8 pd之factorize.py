# coding:utf-8
# author:stay5sec
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

import warnings

warnings.filterwarnings("ignore")

df = pd.DataFrame(['a', 'b', 'b', 'a', 'c', 'b'], columns=["col"])

print(df)
print("\n")

codes, uniques = pd.factorize(df["col"])

df["分类"] = codes

print(df)
print("\n")
print(list(uniques))
print(uniques)
