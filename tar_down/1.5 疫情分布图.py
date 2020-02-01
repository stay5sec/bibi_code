# coding:utf-8
# author:stay5sec

import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

data = pd.read_excel("/Users/super/Desktop/浙江疫情分布.xlsx")

data["city1"] = data["city"] + "市"

# print(data)
# exit()

data1 = [list(z) for z in zip(data["city1"], data["count"])]

# print(data1)
# exit()

from pyecharts import options as opts
from pyecharts.charts import Map, Page
from pyecharts.faker import Collector

C = Collector()


@C.funcs
def map_guangdong() -> Map:
    c = (
        Map()
            .add("", data1, "金华")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="浙江疫情地图"),
            visualmap_opts=opts.VisualMapOpts(),
        )
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render("render1.html")
