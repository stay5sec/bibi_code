# coding:utf-8
# author:stay5sec

import pandas as pd
import requests


pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

# desk path：/Users/super/Desktop/

# url = 'http://cn.epubee.com/books/?s=bjYlMjRweXRobyUyMw'
# html = requests.get(url).text
# print(html)
# exit()


# 数据提取
url = "http://cn.epubee.com/keys/get_ebook_list_search.asmx/getSearchList"

data = {"skey": 'python'}

html = requests.post(url, json=data).text

# print(type(html))
# print("\n")
# print(html)
# exit()

# html = eval(html)["d"]
# print(type(html))
# print(html)
# print(pd.DataFrame(html[0],index=[0]))
# exit()

html = eval(html)["d"]
df = pd.DataFrame()
for i in html:
    df = df.append(pd.DataFrame(i, index=[0]), ignore_index=True)

# print(df.head())
# exit()

# 数据清洗

df["BID"] = df["Title"].apply(lambda x: x.split("[")[1][1:-1])
df["Title"] = df["Title"].apply(lambda x: x.split("[")[0])

# print(df.head())
# exit()

df = (df.groupby("Title").apply(lambda x: list(x["BID"]))).reset_index()

df["book_num"] = df[0].map(len)

df.sort_values("book_num", ascending=0, inplace=True)

df.rename(columns={"Title": "书名", 0: "下载类型"}, inplace=True)


df.to_excel("/Users/super/Desktop/Python书籍2.xlsx", index=False)

print(df.head())
