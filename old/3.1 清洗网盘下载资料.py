# coding:utf-8
# author:Super

import shutil
import os
import re

# 定义被移动/目标路径
be_move = "/Users/super/Desktop/从1开始学Python"
tar_path = "/Users/super/Desktop/"

# # ==============第一步：挑选移动区域的文件======================
# for x, y, z in os.walk(be_move):
#     # print(x)
#     # print(z)
#
#     # for file in z:
#     #     if file.endswith("mp4"):
#     #         print(file)
#     #
#     for file in z:
#         if file.endswith("mp4") or file.endswith("mp3"):
#             print(file)
#
# exit()



list_or = []
dup = []
for t in ["mp4", "mp3"]:
    for x, y, z in os.walk(be_move):
        for file in z:
            if file.endswith(t):
                name = os.path.splitext(file)[0]
                type = os.path.splitext(file)[1]

                if name in dup:
                    print("{} 这个文件出现不同类型的版本……".format(file))
                else:
                    dup.append(name)
                    f = os.path.join(x, file)
                    list_or.append(f)

# print(list_or)
# exit()

tar_file = input("\n请输入你想移动的文件名称：")

# 判断目标文件是否存在
tar_files = os.listdir(tar_path)

if tar_file in tar_files:
    shutil.rmtree(os.path.join(tar_path, tar_file))
    print("目标文件已存在,并且删除……")

os.mkdir(os.path.join(tar_path, tar_file))
print("目标文件已创建")

# 构建最后确定的目录结构
def tar_path_finally(x):
    return os.path.join(tar_path, tar_file, x)

# 使用正则清洗数据
role_dict = {'\[.*\]': "",
             " _ ": "-",
             "_": "-",
             "（": "(",
             "）": ")",
             "丨": "-"}

# 开始拷贝文件
for f in list_or:
    file_name = os.path.basename(f)

    for k, v in role_dict.items():
        file_name = re.sub(k, v, file_name)

    shutil.copyfile(f, tar_path_finally(file_name))
