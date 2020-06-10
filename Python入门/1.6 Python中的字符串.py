# coding:utf-8
# author:stay5sec

# 定义：在Python中，如果我们把单个或多个字符用单引号或者双引号包围起来，就可以表示一个字符串

# s1 = '1: hello, world!'
#
# s2 = "2: hello, world!"
#
# # 以三个双引号或单引号开头的字符串可以折行
# s3 = """
# 3: hello, world!
# ~~~~~
# 12345
# """
# print(s1, s2, s3, sep="\n")
#
# exit()

# # 转义
# s1 = '1: \thello, world!'
# s2 = '2: \\hello, world!'
# s3 = '3: \nhello, world!'
#
# print(s1, s2, s3, sep="\n")
# exit()

# # 八进制或者十六进制数  不被转义r
# s1 = '\x61\x62\x63'
# s2 = '\u4e94\u79d2'
# s3 = '五秒'
# print(s1, s2, s3, sep="\n")
# exit()

# print("五秒".encode("unicode_escape"))

# s1 = 'hello ' * 3
# print(s1)  # hello hello hello
#
# s2 = 'world'
# s1 += s2
# print(s1)  # hello hello hello world
#
# print('ll' in s1)  # True
# print('good' in s1)  # False
#
# exit()

# for i in range(0,10,2):
#     print(i)
#
# exit()

str2 = 'abc123456'
# # 从字符串中取出指定位置的字符(下标运算)
# print(str2[2])  # c
#
# # 字符串切片(从指定的开始索引到指定的结束索引)
# print(str2[2:5])  # c12
# print(str2[2:])  # c123456
# print(str2[2::2])  # c246
#
# print(str2[::2])  # ac246
# print(str2[::-1])  # 654321cba
#
# print(str2[-3:-1])  # 45


# str1 = 'hello, world!'
# # 通过内置函数len计算字符串的长度
# print(len(str1))  # 13
#
# # 获得字符串首字母大写的拷贝
# print(str1.capitalize())  # Hello, world!
#
# # 获得字符串每个单词首字母大写的拷贝
# print(str1.title())  # Hello, World!
#
# # 获得字符串变大写后的拷贝
# print(str1.upper())  # HELLO, WORLD!
#
# # 从字符串中查找子串所在位置
# print(str1.find('or'))  # 8
# print(str1.find('shit'))  # -1
#
# # 检查字符串是否以指定的字符串开头
# print(str1.startswith('He'))  # False
# print(str1.startswith('hel'))  # True
#
# # 检查字符串是否以指定的字符串结尾
# print(str1.endswith('!'))  # True
#
# # 将字符串以指定的宽度居中并在两侧填充指定的字符
# print(str1.center(50, '*'))
#
# # 将字符串以指定的宽度靠右放置左侧填充指定的字符
# print(str1.rjust(50, ' '))
# # exit()

# str2 = 'abc123456'
# # 检查字符串是否由数字构成
# print(str2.isdigit())  # False
#
# # 检查字符串是否以字母构成
# print(str2.isalpha())  # False
#
# # 检查字符串是否以数字和字母构成
# print(str2.isalnum())  # True
#
# exit()

# str3 = '  jackfrued@126.com '
# print(str3)
#
# # 获得字符串修剪左右两侧空格之后的拷贝
# print(str3.strip())
#
# exit()

# 格式化输出字符串
a, b = 5, 10

print(str(a) + " * " + str(b) + " = " + str(a * b))

print('{0} * {1} = {2}'.format(a, b, a * b))
# exit()

# 3.6以后的语法糖
print(f'{a} * {b} = {a * b}')
