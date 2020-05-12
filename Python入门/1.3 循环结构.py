# coding:utf-8
# author:stay5sec

# list1 = [1, 2, 3, 4, 5]
# for i in list1:
#     print(i)
#
# exit()

# # 按照元素输出
# list_love = ["我爱你!"] * 100
# for i in list_love:
#     print(i)
#
# exit()

# print(type(range(10)))
# print(list(range(10)))
# exit()

# # 按照次数输出
# for i in range(1,101):
#     print("第{}次输出：我爱你!".format(i))
#
# exit()

# i = 0
# while i < 100:
#     print("第{}次输出：我爱你!".format(i))
#     i += 1
# exit()

status = "无司机接单"
while True:
    print("找车中……")
    if status == "有司机接单":
        break


status = "单身狗"
while True:
    print("孤独寂寞冷……")
    if status == "渣男":
        continue
    elif status=="程序员":
        print("备胎")
    elif status=="男神！":
        break

