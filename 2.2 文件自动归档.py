# coding:utf-8
# author:Super

import shutil
import os

# 定义被移动/目标路径
be_move = "/Users/super/Desktop/"
tar_path = r"/Users/super/Desktop/电脑/Material/哔哩/"

# ==============第一步：查看移动区域的文件======================
# print(os.listdir(be_move))
# exit()

# ==========第二步：规范移动的标准（哪些需要移动，哪些不要）=============

keep_file = {'.DS_Store', '.localized', '电脑', '模板'}

# 要被移动的就是剔除保存的
all_file = set(os.listdir(be_move))
move_file = all_file - keep_file

# print(move_file)
# exit()

# ===============第三步：目标文件的筛选===================
tar_files = os.listdir(tar_path)
# print(tar_files)
# exit()
tar_files.remove('.DS_Store')

# 提取文件名中最大的数值
max_tar = max(list(map(lambda x: float(x.split(" ")[0]), tar_files)))

# print(max_tar)
# print(type(max_tar))
# exit()

# ===============第四步：生成移动文件名称===================
py_path = "/Users/super/python/bili/"

# 同理
py_files = os.listdir(py_path)

py_files = list(filter(lambda x: ".py" in x and len(x) > 11, py_files))

# print(py_files)
# exit()

# 提取文件名中最大的数值
max_py = max(list(map(lambda x: float(x.split(" ")[0]), py_files)))

# 提取py文件名称
name = list(filter(lambda x: str(max_py) in x, py_files))[0][:-3]

# print(name)
# exit()

# 合成目标路径
tar_path_new = os.path.join(tar_path, name)

# print(tar_path_new)
# exit()


# ==================第五步：判断是否执行过操作===========================
if max_py <= max_tar:
    print("\n文件已移动过,请确认：\n")
    # 如果已经复制过文件了，就打印出来看看
    print(os.listdir(tar_path_new))

else:
    # 否则就创建py代码名称的文件
    os.mkdir(tar_path_new)

    for i in move_file:
        # 判断文件还是文件夹

        shutil.move(os.path.join(be_move, i), tar_path_new)

        print("- {} --->>>---".format(i))
