# coding:utf-8
# author:stay5sec
import pandas as pd
from Func import excel_beautiful


print("方敏笑在哪？")

exit()


def spam(div):
    try:
        return 42 / div
    except ZeroDivisionError:
        print("error")


spam(0)

print(spam(0))
exit()

# desk path：/Users/super/Desktop/


print("a" / "b")
exit()

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

df = pd.read_excel("/Users/super/Desktop/豆瓣T250电影.xlsx")

excel_beautiful("豆瓣T250电影", 1, "美化后的结果")

# print(df)
