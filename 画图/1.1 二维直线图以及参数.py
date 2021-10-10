# coding:utf-8
# author:stay5sec

import matplotlib.pyplot as plt
import numpy as np

# x轴为0到2派之间的100个数
x = np.arange(0, 2 * np.pi, np.pi / 100)

y = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y, x, y2)

plt.xlabel('x label')
plt.ylabel('y label')
plt.title("sin cos")

plt.show()

# 颜色字符
# 'b' 蓝色 'm' 洋红色
# 'g' 绿色 'y' 黄色
# 'r' 红色 'k' 黑色
# 'w' 白色 'c' 青绿色

# 标记字符
# '.' 点标记
# ',' 像素标记(极小点)
# 'o' 实心圈标记
# 'v' 倒三角标记
# '^' 上三角标记
# '>' 右三角标记
