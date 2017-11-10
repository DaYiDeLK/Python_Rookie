# -*- coding: utf-8 -*-

'''
题目：
用python写冒泡排序
'''

a = [66, 2, 31, 4, 556, 74, 56, 13, 64, 3]

# len_ = len(a)
# for j in range(len_ - 1):
#     for i in range(len_ - 1 - j):
#         if a[i] > a[i + 1]:
#             b = a[i + 1]
#             a[i + 1] = a[i]
#             a[i] = b
#
# print(a)

len_ = len(a)
for i in range(len_ - 1):
    for j in range(len_ - 1 - i):
        if a[j] < a[j+1]:
            temp = a[j+1]
            a[j+1] = a[j]
            a[j] = temp

print(a)