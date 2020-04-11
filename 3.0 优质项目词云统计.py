# coding:utf-8
# author:stay5sec

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import jieba
import pandas as pd
import re

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

file = '/Users/super/Desktop/py_obj_clean.xlsx'

# 读取数据
df = pd.read_excel(file)
# print(df.head())
# exit()

chinese = u"([\u4e00-\u9fff]+)"
pattern = re.compile(chinese)

# 使用正则提取中文
df["项目2"] = df["项目"].apply(lambda x: pattern.findall(x))
# print(df["项目2"].sample(5))
# exit()

# print(type(df.loc[65,"项目2"]))
# print(df.loc[65,"项目2"])
# print(''.join(df.loc[65,"项目2"]))
# print(list(jieba.cut(''.join(df.loc[65,"项目2"]))))
# exit()

# 合并list、切割文本、再次合并list
df["项目2"] = df["项目2"].apply(lambda x: " ".join(jieba.cut("".join(x))))
# print(df["项目2"].sample(5))
# exit()

# 合并全部文字
content = " ".join(df["项目2"])

# print(content)
# exit()

# 添加停用此
stopwords = set(STOPWORDS)

for i in {"一个", "可以","通过","项目","使用","实现"}:
    stopwords.add(i)

# 实例化对象
wc = WordCloud(
    # win和mac导入不一致
    font_path="/System/Library/fonts/PingFang.ttc",
    max_words=100,
    width=2000,
    height=1200,
    stopwords=stopwords
)

# 生成数据
wordcloud = wc.generate(content)

print(type(wordcloud))

# 保存数据
wordcloud.to_file("/Users/super/Desktop/wc_{}.jpg".format("python"))

# 显示词云文件
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
