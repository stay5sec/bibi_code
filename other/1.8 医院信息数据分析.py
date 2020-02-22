# coding:utf-8
# author:stay5sec
import pandas as pd

# desk path：/Users/super/Desktop/

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

df=pd.read_excel("/Users/super/Desktop/电脑/Material/哔哩/other_help/实习表格.xlsx",skiprows=1)

df=df[df["序号"].notnull()]

print(df.sample())
exit()

df1=df[df["医院地址"].apply(lambda x:"金华" in x)]

print(df1)


