# coding:utf-8
# author:stay5sec
import pandas as pd
from collections import *

# desk path：/Users/super/Desktop/
from Func import opath

# df = pd.read_excel(opath("1-202105工资.xlsx"), skiprows=1)
#
# print(df.head())


# df=df[(df["姓名"].isnull())&(df["应发工资"].notnull())][["序号","应发工资"]]
#
# df=df.head(df.shape[0]-1)
#
# df["应发工资"]=df["应发工资"].apply(lambda x:round(x,2))
#
# df["flag"]="202105工资"
#
#
# print(df)

df = pd.read_excel(opath("1-202105工资.xlsx"), skiprows=1)

df=df[(df["姓名"].notnull())&(df["应发工资"].notnull())][["姓名","应发工资","实发工资"]]

df["应发工资"]=df["应发工资"].apply(lambda x:round(x,2))

print(df)
