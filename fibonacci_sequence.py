# -*- coding: utf-8 -*-

'''
题目：
假设第一个月初有一对刚出生的兔子
两个月之后（第三个月初）它们可以生育
每月每对成年的兔子会产下一对小兔子
假设在考察期间兔子不会死去
输入月份，打印该月有多少只兔子
'''
'''
f(n) = 0, n = 0
f(n) = 1, n = 1
f(n) = f(n-1) + f(n-2), n > 1
'''

# method 1
def rabbits(month):
    month = int(month)
    if month == 0:
        return 0
    elif month == 1:
        return 1
    else:
        return rabbits(month - 1) + rabbits(month - 2)


month_ = int(input('Lease input the month: '))
print('There are %d rabbits in the %dth month.' %(rabbits(month_), month_))


