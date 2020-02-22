# coding:utf-8
# author:stay5sec
import pandas as pd
import datetime

# desk path：/Users/super/Desktop/

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

df = pd.read_excel("/Users/super/Desktop/电脑/Material/哔哩/other_help/test0219.xlsx")
print(df)
print("分割".center(40, "-"))

df = df.fillna("None")

df = df.T

for c in df.columns:

    print(df[c].unique())

exit()

count = 0
df1 = pd.DataFrame()
for c in df.columns:
    df1.loc[count, "列名"] = c
    df1.loc[count, "list"] = str(df[c].unique())
    count += 1

print(df1)
exit()

df["dup"] = df["列1"] + "," + df["列2"] + "," + df["列3"] + "," + df["列4"]

df["dup_cal"] = df["dup"].apply(lambda x: set(x.split(",")))

print(df)

exit()

# print(df.groupby("列1")["列2"].unique().reset_index())
# exit()

df1 = df.groupby(["列1"]).apply(lambda x: len(list(x["列2"].unique()))).reset_index()

# print(df1)
# exit()

df = pd.merge(df, df1, on="列1", how="left")

df.rename(columns={0: "count"}, inplace=True)

print(df)
exit()

# df1.rename(columns={0:"count"},inplace=True)
#
# df2=df.groupby("列1").first().reset_index()
# del df2["列2"]
#
# df3=pd.merge(df1,df2,on="列1",how="left")
#
# print(df3)
