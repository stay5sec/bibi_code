# coding:utf-8
# author:stay5sec
import pandas as pd
from pymongo import MongoClient

# desk path：/Users/super/Desktop/

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

# 初始化对象
conn = MongoClient()
table = conn.test.ttt3

# print(list(table.find()))
# exit()

# # 读取数据
# df = pd.DataFrame(list(table.find()))
# print(df.sample(10))
#
# exit()

# 新增数据:1/N
# table.insert_one({"name": "jack"})
# exit()
# table.insert_many([{"name": "linda"}, {"name": "lisa"}])
# exit()

# # 查询数据
# print(table.find_one())
# print("-" * 40)
# print("\n")
# for i in table.find():
#     print(i)
# exit()

# # 等值条件查询
# df = pd.DataFrame(list(table.find({"OriginWeather": "Rain"})))
# print(df.shape[0])
# print(df.sample(5))
#
# exit()

# # 非等值查询
# df = pd.DataFrame(list(table.find({"AvgTicketPrice": {"$gte": 950}})))
# print(df.shape[0])
# print(df.sample(5))
# exit()

# 正则查询
df = pd.DataFrame(list(table.find({"DestWeather": {"$regex": "^C"}})))

print(df["AvgTicketPrice"].mean())

