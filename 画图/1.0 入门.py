# coding:utf-8
# author:stay5sec

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)

# print(type(x))
# print(x)
# exit()

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()

plt.show()