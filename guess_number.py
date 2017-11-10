# -*- coding: utf-8 -*-

'''
题目：
随机选择一个三位以内的数字作为答案。用户输入一个数字，程序会提示大了或是小了，直到用户猜中。
'''

import random

ans = random.randrange(1, 1000)
# ans = 200
while True:
    num = int(input('Please guess a number between 1 to 1000: '))
    if num < ans:
        print('Bigger！')
    elif num > ans:
        print('Smaller.')
    else:
        print('You are right!!!')
        break
