# coding:utf-8
# author:Super

import matplotlib.pyplot as plt


# sar = 4000
# per = 1000 / sar + 1
# print(per)
# exit()

# # 小甲理想状态
# for i in range(10):
#     sar = 4000
#     per = 1000 / sar + 1
#     print("第{}年工资：{}".format(i + 1, int(sar * pow(per, i))))
#
# exit()

# # 函数封装
# def cal(add, year=10):
#     for i in range(year):
#         sar = 4000
#         per = add / sar + 1
#         print("第{}年工资：{}".format(i + 1, int(sar * pow(per, i))))
#
#
# cal(1000)
# print("\n")
# cal(500)
# exit()


# # 画图对比
# def cal(add, year=10):
#     list1 = []
#     for i in range(year):
#         sar = 4000
#         per = add / sar + 1
#         list1.append(int(sar * pow(per, i)))
#     return list1
#
# plt.figure(figsize=(12, 8))
# plt.plot(cal(1000), marker='.')
# plt.plot(cal(500), marker='.')
# plt.show()
# exit()

# # 修正之后的薪资（1，加成太高；2，天花板）
# sar = 4000
# per = 1000 / sar + 1
# for i in range(12):
#
#     if i <= 1:
#         sar = int(sar * pow(per, i))
#         print("第{}年工资：{}".format(i + 1, sar))
#     elif sar >= 10000:
#         print("第{}年工资：{}".format(i + 1, int(sar)))
#     else:
#         sar *= 1.1
#         print("第{}年工资：{}".format(i + 1, int(sar)))
# exit()


# 再次封装
def cal(add, thb, year=40):
    sar = 4000
    per = add / sar + 1
    list1 = []
    for i in range(year):
        if i <= 1:
            sar = int(sar * pow(per, i))
            list1.append(int(sar))
        elif sar >= thb:
            list1.append(int(sar))
        else:
            sar *= 1.1
            list1.append(int(sar))

    return list1


import pandas as pd

df = pd.DataFrame()

df["jia"] = cal(1000, 20000)
df["yi"] = cal(500, 10000)

df["cha"] = df["jia"] - df["yi"]

df["mou"] = df["cha"] * 12

df["cum"] = df["mou"].cumsum()

print(df)
exit()

# 再次作图
plt.figure(figsize=(12, 8))
plt.plot(df["cum"], marker='.')
plt.show()
