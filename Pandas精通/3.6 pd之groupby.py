# -*- coding: utf-8 -*-
# author:stay5sec
import pandas as pd

from Func import opath

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 100)

import warnings

warnings.filterwarnings("ignore")

# 1,读取数据
df = pd.DataFrame([["a", "b", "a", "b"], [1, 2, 3, 4], [11, 22, 33, 44]], index=["name", "id", "age"]).T

print(df.head())
print("\n")

print(df.groupby("name",as_index=False)["id", "age"].sum())
