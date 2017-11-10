# -*- coding: utf-8 -*-

'''
题目：
打印九九乘法表
'''

for i in range(1, 10):
    for j in range(1, 10):
        if j % 9 == 1:
            print()
        if i <= j:
            print("%d*%d=%d\t" % (i, j, i * j), end='')


