# coding:utf-8
# author:stay5sec

import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

from numpy import array, uint8, average

from PIL import Image

# desk path：/Users/super/Desktop/

# 读取图片
image = Image.open("/Users/super/Desktop/new_year.png")
# print(image)
# exit()

# 转化为数组
image = array(image)
# print(image)
# exit()

# 宽度/高度/通道
w, h, d = image.shape

# print("\n")
# print(w, h, d)
# exit()

image.resize(w * h, d)

# print(pd.DataFrame(image))
# exit()

image = uint8(average(image, axis=1)).reshape((w, h))


image = Image.fromarray(image, mode="L")

# print(image)
# exit()

image.show()

image.save("/Users/super/Desktop/new_year3.png")
