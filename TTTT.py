# coding:utf-8
# author:stay5sec
import pandas as pd
from collections import *

# desk path：/Users/super/Desktop/
x="300|套小程序|链接"
print(x[:x.find("|链接")].replace("|", ""))
exit()

dict1 = {}

dict1["name"] = "jack"

dict1["set"] = {1, 2, 3}

dict1["list"] = [4, 5, 6]

# print(dict1["set"])
#
# exit()

print(dict1.keys())

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.difference(set2))
exit()
