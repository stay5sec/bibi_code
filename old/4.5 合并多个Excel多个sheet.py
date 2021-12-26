# coding:utf-8
# author:stay5sec
import pandas as pd
import os

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 500)

import warnings

warnings.filterwarnings("ignore")

path = "/Users/super/Desktop/合并Excel"

list_excel = os.listdir(path)

# print(list_excel)
# exit()

list_excel = [x for x in list_excel if not x.startswith(".DS")]

# print(list_excel)
# exit()

print(list_excel)

df_all = pd.DataFrame()
for l in list_excel:
    path_excel = os.path.join(path, l)

    sheets = pd.read_excel(path_excel, sheet_name=None)

    df = pd.DataFrame()
    for k, v in sheets.items():
        tmp = v[["name", "address"]]
        tmp["sheet名"] = k

        df = df.append(tmp)

    df["Excel名"] = l

    df_all = df_all.append(df, ignore_index=True)

print(df_all)

df_all.to_excel("/Users/super/Desktop/合并多个Excel多个sheet2.xlsx", index=False)
