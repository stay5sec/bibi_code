# coding:utf-8
# author:stay5sec
import pandas as pd
from elasticsearch import Elasticsearch

# desk path：/Users/super/Desktop/

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

# 实例化对象
es = Elasticsearch(hosts="http://localhost:9200/")

total_count = es.count(index="kibana_sample_data_flights")['count']

print('总数据量：', total_count)

# exit()

query_json = {
    "query": {
        "match_all": {}
    },"size": 1000
}

data = es.search(index="kibana_sample_data_flights", body=query_json)

# print(data)
# exit()

data = data["hits"]["hits"]

# print(data)
# exit()

df = pd.DataFrame(data)

# print(df)
# exit()

df = pd.DataFrame(list(df["_source"]))

# print(df)
# exit()

df = df[["FlightNum", "OriginCityName", "DestCountry", "OriginWeather", "AvgTicketPrice", "DestWeather", "timestamp"]]

# print(df)
# exit()

df.to_excel("/Users/super/Desktop/es.xlsx", index=False)

print('\n')

print(df.info())
