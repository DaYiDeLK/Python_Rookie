# -*- coding: utf-8 -*-

'''
题目：判断一个数是不是12321或者123321这种对称形式
'''


a = input("please enter a 5 bits number: ")
# count = 0
# for i in range(len(a) - 1):
#     if a[i] == a[-i-1]:
#         count += 1
#     else:
#         pass
#
# if count == len(a) - 1:
#     print('right')
# else:
#     print('wrong')


for i in range(len(a) - 1):
    if a[i] != a[-i-1]:
        examiner = 'wrong';
        # break
    else:
        examiner = 'right';

print(examiner)