# -*- coding: utf-8 -*-

'''
利用条件运算符的嵌套来完成此题：
学习成绩>=90分的同学用A表示，
60-89分之间的用B表示，
60分以下的用C表示。
'''

a = int(input('Please enter the grades in marks: '))
if a >= 90:
    print('A')
elif 60 <= a < 90:
    print('B')
else:
    print('C')
