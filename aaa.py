# coding:utf-8
# author:stay5sec
import pandas as pd
from Func import excel_beautiful

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

df = pd.read_excel("/Users/super/Desktop/豆瓣T250电影.xlsx")

excel_beautiful("豆瓣T250电影", 1, "美化后的结果")

# print(df)
