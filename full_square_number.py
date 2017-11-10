# -*- coding: utf-8 -*-

'''
题目：
一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
'''

import math

num = 1
while True:
    sqrt_100 = math.sqrt(num + 100)
    sqrt_268 = math.sqrt(num + 268)
    a = sqrt_100 - int(sqrt_100)
    b = sqrt_268 - int(sqrt_268)
    if a == 0 and b == 0:
        print(num)
        break
    else:
        num += 1



