# coding:utf-8
# author:stay5sec

# # 原始输出
# for i in range(1, 11):
#     print(i)
# exit()

# # 判断输出
# for i in range(1, 11):
#     if i > 5:
#         print(i)
# exit()

# # 多判断案例
# chengji = {"jack": 45, "tony": 80, "5sec": 60}
#
# for name, score in chengji.items():
#     if score > 60:
#         print("{}的成绩：优秀".format(name))
#     elif score == 60:
#         print("{}的成绩：及格".format(name))
#     else:
#         print("{}的成绩：不及格".format(name))
#
# exit()

# # 嵌套判定案例
# chengji = {"jack": 45, "tony": 80, "5sec": 60, "tom": 81}
#
# for name, score in chengji.items():
#     if score > 60:
#         if name.endswith("m"):
#             print("{}的成绩：优秀".format(name))
#     elif score == 60:
#         print("{}的成绩：及格".format(name))
#     else:
#         print("{}的成绩：不及格".format(name))
#
# exit()

# 一行代码写判断
score = 60

# if score > 60:
#     print("good")
# else:
#     print("terrible")
#
# exit()

# print("good" if score > 60 else "terrible")
#
# exit()

# # 一行代码写多判断
# if score > 60:
#     print("good")
# elif score == 60:
#     print("fine")
# else:
#     print("terrible")
#
# exit()

print("good" if score > 60 else "fine" if score == 60 else "terrible")
