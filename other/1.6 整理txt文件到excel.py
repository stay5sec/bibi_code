# coding:utf-8
# author:stay5sec
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

with open("/Users/super/Desktop/001.txt", "r") as f:  # 打开文件
    data = f.readlines()  # 读取文件

df = pd.DataFrame()
list1 = []
for i in data:
    if i == "\n" or i == ' ':
        pass
    else:
        list1.append(i.replace("\n", ""))

list1 = list1[7:]

# print(list1)
# print(len(list1))
# exit()

count = 0
list2 = []
for i in range(0, len(list1) - 7, 7):
    count += 1
    l = list1[i:i + 7]
    list2.append(l)

# print(list2)

df = pd.DataFrame(list2)

df.columns = [0, "备注", "姓名", "学号", "身份", "疑似或者确诊", "上报时间"]

del df[0]

df = df[["姓名", "学号", "身份", "疑似或者确诊", "上报时间", "备注"]]

df.to_excel("/Users/super/Desktop/test.xlsx", index=False)

print(df)
