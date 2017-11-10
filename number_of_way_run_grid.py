# -*- coding: utf-8 -*-

'''
题目：
有一个X*Y的网格，小团要在此网格上从左上角到右下角，只能走格点且只能向右或向下走。
请设计一个算法，计算小团有多少种走法。给定两个正整数int x,int y，请返回小团的走法数目。
'''

'''
分析：
方法1：
X*Y个网格，从最左上方走到最左下方，而且每次只能向右或者向下走。可以把这个问题简化为组合问题。
左上角到右下角总共需要向右走X步，需要向下走Y步。所以总共有C, X+Y, X种走法。

'''


def c(n, k):
    n = int(n)
    k = int(k)
    fac_n = factorial(n)
    fac_k = factorial(k)
    fac_nk = factorial(n - k)
    # print(fac_n, fac_k, fac_nk)

    numerator = fac_n
    denominator= fac_nk * fac_k
    combination = numerator / denominator
    # print(combination)
    return combination


def factorial(m):
    if m <= 1:
        return 1
    else:
        return m * factorial(m - 1)


X = input('please input a X: ')
Y = input('please input a Y: ')
x = int(X)
y = int(Y)
z = x + y
a = c(z, y)
print('The form of the grid is  %d*%d ' % (x, y))
print('\nThe number of ways to go form the upper left corner to the bottom right corner is : %d' % a)
