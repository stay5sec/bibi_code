# coding:utf-8
# author:stay5sec

import redis

# # 原始操作
# r = redis.Redis(host='localhost', port=6379, decode_responses=True)
#
# r.set('name', 'jack')
# print(r.get('name'))
# print(type(r.get('name')))
#
# exit()

# 优化操作
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

# r.set('name2', ' mayun')
# name2 = r.get('name2')
# print(name2)
#
# # exit()
#
# # 合并string
# r.append("name", name2)
# print(r["name"])
# exit()

# 集合操作演示
r.sadd("set1", "1", "2", "3")
print("set1 members:", r.smembers('set1'))

r.sadd("set2", "4", "2", "3")
print("set2 members:", r.smembers('set2'))

# 取出不同
print(r.sdiff("set1", "set2"))

# 取出集合长度
print(r.scard("set1"))
