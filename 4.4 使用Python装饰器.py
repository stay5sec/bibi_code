# coding:utf-8
# author:stay5sec

def max_range(func):
    def check3(n):
        if n <= 10:
            res = func(n)

            return res
        else:
            return "\n数字太大了，计算机吃不消了……"

    return check3


@max_range
def add(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

@max_range
def multi(n):
    mus = 1

    for i in range(1, n):
        mus *= i
    return mus

print(multi(10))
print(multi(11))
exit()


print(add(10))
print(add(11))
exit()


def multi(n):
    mus = 1

    if n <= 10:
        for i in range(1, n):
            mus *= i
        return mus
    else:
        return "\n数字太大了，计算机吃不消了……"


# print(multi(10))
# print(multi(11))
# exit()


def add2(n):
    sum = 0

    if n <= 10:

        for i in range(n):
            sum += i

        return sum

    else:
        return "\n数字太大了，计算机吃不消了……"


print(add2(100))
