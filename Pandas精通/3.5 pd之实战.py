# -*- coding: utf-8 -*-
# author:stay5sec
import pandas as pd

from Func import opath

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 100)

import warnings

warnings.filterwarnings("ignore")

# 1,读取数据
df = pd.read_table(opath("a.txt"))

print(df.head())
print("\n")

# 2 将列名放入数据中
df = df.T

df.insert(0, "-1", ["第1章 课程介绍 试看1 节 | 12分钟"])

df = df.T

df.columns = ["col"]

print(df.head())
print("\n")

# # 3 选出需要的章、节
# df["useful"]=df["col"].apply(lambda x:x if "章 " in x else "")
# df["useful"] = df["col"].apply(lambda x: x if "章 " in x or "-" in x else "")

df["useful"] = df["col"].apply(lambda x: x if "章 " in x or ("-" in x and "本章将" not in x) else "")

df = df[df["useful"] != ""]

print(df.head())
print("\n")
# exit()

# 4 分类出【章节】和 【目录】
df["list"] = df["useful"].apply(lambda x: x if x.startswith("第") else None)

df["list"] = df["list"].fillna(method="ffill")

del df["col"]

print(df.head(8))
print("\n")


# 清洗数据
df = df[df["useful"].apply(lambda x: not x.startswith("第"))]

df["章节"] = df["list"].apply(lambda x: x.split(" | ")[0])
df["章节时长"] = df["list"].apply(lambda x: x.split(" | ")[1])

# 处理视频
df["视频名称"] = df["useful"].apply(lambda x: x.split(" (")[0])
# df["视频时长"]=df["useful"].apply(lambda x:x.split(" (")[1])

df["视频时长"] = df["useful"].apply(lambda x: x.split(" (")[1][:-1] if " (" in x else None)


df["视频时长"] = df["视频时长"].fillna("讨论题")
df["视频名称"] = df["视频名称"].str.replace("【讨论题】", "")

df = df[df.columns[-4:]]

print(df.head())
print("\n")

# 最后规整
df["章节"] = df["章节"].apply(lambda x: x.split(" 试看")[0])
df["视频名称"] = df["视频名称"].str.replace("（新）", "")

df.reset_index(inplace=True)

df2 = df.groupby("章节").first().reset_index()

df = df.append(df2)

# df.to_excel(opath("6.xlsx"),index=False)

df.sort_values("index", inplace=True)

df.reset_index(drop=True, inplace=True)

for i in range(df.shape[0] - 1):
    if df.loc[i, "index"] == df.loc[i + 1, "index"]:
        df.loc[i] = ["", "", "", "", ""]

# print(df.head())
# exit()

del df["index"]
print(df.head())

df.to_excel(opath("see_12.xlsx"), index=False)
