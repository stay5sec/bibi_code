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

from sklearn.datasets import load_iris

df = pd.DataFrame(load_iris().data)

# print(df.head())
# exit()


sns.pairplot(df)
plt.show()

# print(titanic.head())





