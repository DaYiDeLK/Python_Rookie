# -*- coding: utf-8 -*-

'''
输入三个整数x,y,z，请把这三个数由小到大输出。
'''


a = int(input('please give a number: '))
b = int(input('please give a number: '))
c = int(input('please give a number: '))

if a > b:
    temp = a
    a = b
    b = temp
if a > c:
    temp = a
    a = c
    c = temp
if b > c:
    temp = b
    b = c
    c = temp

print(a, b, c)
