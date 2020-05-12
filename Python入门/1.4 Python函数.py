# coding:utf-8
# author:stay5sec

# # 单身女青年小王的择偶标准
# status = input("小王碰到了：")
# if status == "渣男":
#     print("忽略……")
# elif status == "程序员":
#     print("备胎……")
# elif status == "男神":
#     print("准备生猴子……")
# else:
#     print("继续相亲……")
#
# exit()

# 小王的妹妹初长成……

# 函数封装
def cal(name):
    status = input("{}碰到了：".format(name))
    if status == "渣男":
        print("忽略……")
    elif status == "程序员":
        print("备胎……")
    elif status == "男神":
        print("准备生猴子……")
    else:
        print("继续相亲……")


# cal("小王")
# cal("小王的妹妹")
# exit()


# 函数封装：参数判断
def cal2(name, type):
    status = input("{}碰到了：".format(name))
    if status == "渣男":
        print("忽略……")
    elif status == "程序员":
        print("备胎……")
    elif status == "男神":
        if type == "不婚族":
            print("just 炮友……")
        else:
            print("准备生猴子……")
    else:
        print("继续相亲……")

# cal2("小红", "不婚族")
# exit()

# def cal3():
#     pass

# 函数封装：默认值
def cal3(name, type="结婚族"):
    status = input("{}碰到了：".format(name))
    if status == "渣男":
        print("忽略……")
    elif status == "程序员":
        print("备胎……")
    elif status == "男神":
        if type == "不婚族":
            print("just 炮友……")
        else:
            print("准备生猴子……")
    else:
        print("继续相亲……")

# cal3("大红","不婚族")
print(cal3("大红"))
exit()


# 函数封装：返回值
def cal4(name, type="结婚族"):
    status = input("{}碰到了：".format(name))
    if status == "渣男":
        return "忽略……"
    elif status == "程序员":
        return "备胎……"
    elif status == "男神":
        if type == "不婚族":
            return "just 炮友……"
        else:
            return "准备生猴子……"
    else:
        return "继续相亲……"


result = cal4("小红")
print("小红告诉老爸，自己的结果是：", result)
