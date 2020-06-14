# coding:utf-8
# author:stay5sec

import pandas as pd
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

# df=pd.read_csv("titanic.csv")
#
# print(df.shape)
# print(df.head())
# exit()

import matplotlib.pyplot as plt
import seaborn as sns


# from sklearn.datasets import load_iris
#
# iris = load_iris()
#
# # 获取特征集和分类标识
# features = iris.data
# labels = iris.target
#
# # 花萼长度、花萼宽度、花瓣长度、花瓣宽度
#
# df=pd.DataFrame(features)
# df["labels"]=labels
#
# df.columns=["花萼长度","花萼宽度","花瓣长度","花瓣宽度","种类"]
#
# print(df.head())
# exit()
tips = sns.load_dataset("tips")
plt.figure(figsize=(14,8))
sns.kdeplot(tips[["total_bill","tip"]],shade=True,shade_lowest=False)
plt.grid()

# sns.pairplot(df)
plt.show()







