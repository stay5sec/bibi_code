# coding:utf-8
# author:stay5sec
import pandas as pd

# desk path：/Users/super/Desktop/

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

file = "/Users/super/python/bili/data/bd.txt"

with open(file) as f:
    data = f.readlines()

# print(data)
# exit()

# # 打印结果
# for i in data:
#     print(i)
#
# print(data)
# exit()

data = [x for x in data if x != "\n"]

# print(data)
# exit()

data = list(map(lambda x: x.replace("密码", "提取码").replace("\n", "")
                .replace("\xa0", "").replace("：", ": "), data))
# print(data)
# exit()

data = "|".join(data).split("|提取码: ")

# print(data)
# exit()

for i in range(len(data)):
    if i == 0:
        data[i] = data[i] + "|" + data[i + 1][:4]

    elif i == len(data) - 1:
        pass

    else:
        data[i] = data[i][5:] + "|" + data[i + 1][:4]

# print(data)
# exit()

# 清理被合并的标题
    data = list(map(lambda x: x.replace("链接", "|链接") if "|链接" not in x else x, data))

# print(data)
# exit()

# 清理被拆分的标题
data = list(
    map(lambda x: x[:x.find("|链接")].replace("|", "") + x[x.find("|链接"):] if "|" in x[:x.find("|链接")] else x, data))

# print(data)
# exit()

# 二重拆分
data = list(map(lambda x: x.split("|"), data))

# print(data)
# exit()

# 构建dataframe
df = pd.DataFrame(data)
df.columns = ["name", "url", "password"]
df.dropna(how="any", inplace=True)
df["url"] = df["url"].apply(lambda x: x.replace("链接: ", ""))

from prettytable import PrettyTable

table = PrettyTable(list(df.columns))
table.add_df(df.values.tolist())

print(table)

# 输出到桌面
df.to_excel("/Users/super/Desktop/福利.xlsx", index=False)
