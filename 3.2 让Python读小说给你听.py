# coding:utf-8
# author:stay5sec


with open("/Users/super/python/bili/data/xiaoshuo.txt", "r") as f:
    data = f.read()  # 读取文件
    print(data)

# exit()

import pyttsx3

# 初始化
engine = pyttsx3.init()

# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate-100)

engine.say(data)

engine.runAndWait()


