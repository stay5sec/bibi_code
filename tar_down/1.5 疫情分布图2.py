# coding:utf-8
# author:stay5sec

import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

str = "婺城区1例、金东区3例、东阳市10例、义乌市12例、永康市5例、浦江县3例"
list1 = str.split("、")

list2 = list(map(lambda x: x[:3], list1))
list3 = list(map(lambda x: int(x[3:].replace("例", ""))*10, list1))

# print(list2)
# exit()

data1 = [list(z) for z in zip(list2, list3)]

print(data1)
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
            title_opts=opts.TitleOpts(title="金华疫情地图"),
            visualmap_opts=opts.VisualMapOpts(),
        )
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render("render1.html")
