# -*- coding: utf-8 -*-

import requests
import os
import pandas as pd
import re
import numpy as np

from Func import opath

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

import warnings

warnings.filterwarnings("ignore")


def cal(no, y):
    # 抓取网址
    url = 'http://fundf10.eastmoney.com/FundArchivesDatas.aspx?type=jjcc&code={}&topline=10&year=&month=&rt=0.4853159141166432'.format(
        no)

    # 提取网页
    txt2 = requests.get(url).text

    txt2 = eval(
        txt2[12:-1].replace("content", "\"content\"").replace("arryear", "\"arryear\"").replace("curyear",
                                                                                                "\"curyear\""))

    a = txt2["content"]

    b = re.findall(r"<td.*?</td>", a)

    c = re.sub(r"<.*?>", "|", "".join(b))

    c = c.replace("||||", "|").replace("||", "|").replace("||", "|").replace("||", "|")
    c = c.replace("变动详情|股吧|行情|档案|", "").replace("股吧|行情|档案|", "")
    c = c.replace("（万股）|持仓市值|（万元）|", "").replace("最新价|涨跌幅|相关资讯|占净值|", "").replace("|相关资讯|占净值", "")

    d = [x for x in c.split("|") if len(x) >= 1]

    df = pd.DataFrame(np.array(d).reshape(int(len(d) / 6), 6))

    df["基金编码"] = no
    df["基金名称"] = y

    return df


if os.path.exists(opath("df3.h5")):
    df3 = pd.read_hdf(opath("df3.h5"))
    print("\n读取数据中……\n")

else:

    url3 = "https://fund.eastmoney.com/js/fundcode_search.js"
    txt3 = requests.get(url3).text
    t3 = txt3[8:-1]
    df3 = pd.DataFrame(eval(t3))
    df3.to_hdf(opath("df3.h5"), key="data")
    print("\n抓取数据中……\n")

df3 = df3[df3[3] == "股票型"]

df3.reset_index(drop=True, inplace=True)

# print(df3.head())
# exit()

df = pd.DataFrame()
for i in range(df3.shape[0]):
    x = df3.loc[i, 0]
    y = df3.loc[i, 2]

    try:
        _df = cal(x, y)

    except Exception as e:
        print("{}编号出现了问题……".format(x))
        _df = pd.DataFrame()

    df = df.append(_df, ignore_index=True)

    # if i > 2:
    #     df.to_excel(opath("kan.xlsx"), index=False)
    #     df.to_hdf(opath("jijin.h5"), key="data")
    #     break

df.rename(columns={0: "序号", 1: "股票代码", 2: "股票名称", 3: "占净值", 4: "持股数", 5: "持仓市值"}, inplace=True)

print(df.shape[0])
print(df.head())

df.to_hdf(opath("jijin.h5"), key="data")
