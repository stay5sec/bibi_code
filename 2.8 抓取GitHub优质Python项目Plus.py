# coding:utf-8
# author:Super

from pyquery import PyQuery
import requests
import re
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)


def df_one(page):
    url = "https://github.com/521xueweihan/HelloGitHub/blob/master/content/{}/HelloGitHub{}.md".format(page, page)

    html = requests.get(url).text
    res = PyQuery(html)

    article = res("article").text()

    content = article.split("\n🔙\n返回目录\n🔙\n\n")

    summary = list(filter(lambda x: "🎉\n目录" in x, content))[0]
    summary = summary.split("🎉\n目录")[1].split("Tips：")[0].split("\n")
    summary = [x for x in summary if x != '']
    title = article.split("\n")[0]
    objs = article.split("Tips：")[1].split("\n🔙\n返回目录\n🔙\n\n")
    py = [x for x in objs if "Python 项目" in x][0]

    py = re.sub("示例代码如下：\n.*\n", "\n", py)
    py = re.sub("示例代码如下：\n.*", "", py)
    py = py.split("\n")[2:]

    df = pd.DataFrame()

    count = 0
    for i in py:
        df.loc[count, "期刊"] = title
        df.loc[count, "目录"] = str(summary)
        df.loc[count, "项目"] = i
        count += 1

    return df


# print(df_one(15))
# exit()

x, y = 0, 0
df_all = pd.DataFrame()
for i in range(10, 48):
    try:
        df_all = df_all.append(df_one(i))
        print("第{}期数据抓取完毕!".format(i))
        x += 1

    except Exception as e:
        print(">" * 20)
        print("第{}期数据抓取失败!".format(i))
        y += 1

print("下载成功次数：{}\n下载失败次数:{}".format(x, y))

df_all.to_excel("/Users/super/Desktop/github_task.xlsx", index=False)
