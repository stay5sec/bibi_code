# coding:utf-8
# author:stay5sec

list1 = [1, 3, 5, 7, 100]
print(list1)  # [1, 3, 5, 7, 100]

# 乘号表示列表元素的重复
list2 = ['hello'] * 3
print(list2)  # ['hello', 'hello', 'hello']

# 计算列表长度(元素个数)
print(len(list1))  # 5

# 下标(索引)运算
print(list1[3])  # 7
print(list1[-1])  # 100

# 切片操作
print(list1[2:4])
print(list1[::-1])

# 替换
list1[2] = 300
print(list1)  # [1, 3, 300, 7, 100]

# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])

# 通过for循环遍历列表元素
for elem in list1:
    print(elem)

# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)

list1 = [1, 3, 5, 7, 100]
# 添加元素
list1.append(200)
list1.insert(1, 400)

# 排序
print(sorted(list1))
print(sorted(list1, reverse=True))

# 合并两个列表
list1.extend([1000, 2000])
list1 += [1000, 2000]

# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
    list1.remove(3)

# 指定的位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)

# 清空列表元素
list1.clear()
print(list1)
