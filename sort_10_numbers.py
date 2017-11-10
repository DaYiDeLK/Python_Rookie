# -*- coding: utf-8 -*-

'''
对10个数进行排序
'''

a = [2, 3, 5, 75, 23, 41, 25, 3, 45, 10]
len_ = len(a)
# print(len_)
print(a)
for i in range(len_ - 1):
    for j in range(len_ - 1 - i):
        if a[j] > a[j + 1]:
            temp = a[j + 1]
            a[j + 1] = a[j]
            a[j] = temp
print(a)