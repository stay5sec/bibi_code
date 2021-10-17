# coding:utf-8
# author:stay5sec

import requests
from lxml import etree
import pandas as pd


pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

# 抓取网址
url = 'http://fundf10.eastmoney.com/FundArchivesDatas.aspx?type=jjcc&code=000689&topline=10&year=&month=&rt=0.4853159141166432'
url2= "http://fundf10.eastmoney.com/FundArchivesDatas.aspx?type=jjcc&code=000209&topline=10&year=&month=&rt=0.1651012588208438"

# 提取网页
txt = requests.get(url).text

print(txt)
exit()


html = etree.HTML(txt)

# //*[@id="tblite_hh"]/tbody/tr[1]/td[1]
# //*[@id="tblite_hh"]/tbody/tr[2]/td[1]

id = html.xpath('''//*[@id="tblite_hh"]/tbody/tr/text()''')

print(id)
exit()

# 年份提取xpath
'''//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/p[1]/text()[2]'''
'''//*[@id="content"]/div/div[1]/ol/li[2]/div/div[2]/div[2]/p[1]/text()[2]'''

year = html.xpath('''//li/div/div[2]/div[2]/p[1]/text()[2]''')

# print(year)
# exit()

# 评分提取xpath
'''//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[2]'''
'''//*[@id="content"]/div/div[1]/ol/li[2]/div/div[2]/div[2]/div/span[2]'''

score = html.xpath('''//li/div/div[2]/div[2]/div/span[2]/text()''')

# print(score)
# exit()

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

# print(df.head())
# exit()

# 保存数据
df.to_excel("/Users/super/Desktop/豆瓣T250电影.xlsx", index=False)
