# coding:utf-8
# author:stay5sec

# 读取文件
with open("/Users/super/python/bili/data/xiaoshuo.txt", "r") as f:
    data = f.read()
    print(data)


import pyttsx3

# 初始化
engine = pyttsx3.init()

# # 音色
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

# # 音速
# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate-80)

engine.say(data)

engine.runAndWait()


