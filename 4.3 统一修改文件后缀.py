# coding:utf-8
# author:stay5sec

import shutil
import os

tar_path = "/Users/super/Desktop/books"

out_path = "/Users/super/Desktop/books2"

# 判断文件是否存在
if os.path.exists(out_path):
    print("请查看已存在文件！")  # 存在文件：让其查看情况
    exit()
else:
    os.mkdir(out_path)
    print("输出文件夹创建完毕……")

for f in os.listdir(tar_path):
    # print(f)

    f_new = f.split(".")[0] + ".html"

    # print(f_new)
    # exit()

    tar_file = os.path.join(tar_path, f)
    out_file = os.path.join(out_path, f_new)

    shutil.copy(tar_file, out_file)

    print("{} - 文件修改完毕".format(f))


# from Func import change_file_suffix
# change_file_suffix(tar_path,out_path+"3","pdf")
