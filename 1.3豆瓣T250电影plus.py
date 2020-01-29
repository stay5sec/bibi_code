# coding:utf-8
# author:stay5sec

import requests
from lxml import etree
import pandas as pd
from fake_useragent import UserAgent

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

# for i in range(0, 249, 25):
#     print(i)
# exit()

# 抓取网址
url = 'https://movie.douban.com/top250'

# 随机UA
headers = {
    'User-Agent': UserAgent().random
}


def data(url):
    # 提取网页
    txt = requests.get(url, headers=headers).text
    html = etree.HTML(txt)

    # 电影名称提取xpath
    name = html.xpath('''//li/div/div[2]/div[1]/a/span[1]/text()''')

    # 年份提取xpath
    year = html.xpath('''//li/div/div[2]/div[2]/p[1]/text()[2]''')

    # 评分提取xpath
    score = html.xpath('''//li/div/div[2]/div[2]/div/span[2]/text()''')

    # 数据放入表格
    df = pd.DataFrame([name, year, score]).T

    # 列名重置
    df.columns = ["name", "more", "score"]

    # 提取具体数据
    df["year"] = df["more"].apply(lambda x: x.split("/")[0].strip())
    df["country"] = df["more"].apply(lambda x: x.split("/")[1].strip())
    df["type"] = df["more"].apply(lambda x: x.split("/")[2].strip())

    # 删除多余列
    del df["more"]

    return df


df_all = pd.DataFrame()
for i in range(0, 249, 25):
    # 生成翻页网址
    url1 = url + "?start={}".format(i)

    print(url1)
    print("-" * 30)

    # 提取分页数据
    df = data(url1)

    print("第{}页抓取完毕(^_^)".format(int(i/25)+1))

    # 将每页数据存入一个df
    df_all = df_all.append(df, ignore_index=True)

name = "豆瓣T250电影all"

# 保存数据
df_all.to_excel("/Users/super/Desktop/{}.xlsx".format(name), index=False)

from Func import excel_beautiful

excel_beautiful(name, 1, "豆瓣T250电影all_clean")
