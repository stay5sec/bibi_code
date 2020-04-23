# coding:utf-8
# author:stay5sec

import os
import time

import pyttsx3

time.sleep(5)
# 时间格式化
file = time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".txt"

or_path = "/Users/super/python/bili/data"

if file in os.listdir(or_path):
    # 读取文件
    with open(os.path.join(or_path,file), "r") as f:
        data = f.read()

        # 初始化
        engine = pyttsx3.init()

        engine.say(data)

        engine.runAndWait()
