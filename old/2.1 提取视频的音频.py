# coding:utf-8
# author:stay5sec

import time
from moviepy.editor import *

video_path = "/Users/super/Desktop/good_night.mp4"
audio_path = "/Users/super/Desktop/audio.wav"

st = time.time()

# moviepy.VideoFileClip: 读取视频到内存，返回一个VideoFileClip的对象
video = VideoFileClip(video_path)

# 获取视频的音频部分
audio = video.audio

# 将视频中的音频部分提取出来，写入audio.wav
audio.write_audiofile(audio_path)

print("消耗时间：{}".format(time.time() - st))
