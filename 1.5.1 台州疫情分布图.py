# coding:utf-8
# author:stay5sec

str = "温岭市30例、路桥区12例、临海市5例、黄岩区14例、三门县6例、天台县5例、椒江区6例、仙居县3例"
list1 = str.split("、")

# print(list1)
# exit()

list2 = list(map(lambda x: x[:3], list1))
list3 = list(map(lambda x: int(x[3:].replace("例", "")) * 10, list1))

# print(list2)
# print(list3)
# exit()

data1 = [list(z) for z in zip(list2, list3)]

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
            .add("", data1, "台州")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="台州疫情地图"),
            visualmap_opts=opts.VisualMapOpts(),
        )
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render("render2.html")


