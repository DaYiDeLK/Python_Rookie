# -*- coding: utf-8 -*-

'''
题目：
遍历并打印0到100，
如果数字能被3整除，显示Fizz；
如果数字能被5整除，显示Buzz；
如果能同时被3和5整除，就显示FizzBuzz。
结果应该类似：0,1,2，Fizz，4，Buzz，Fizz……14，FizzBuzz，16……
'''

for i in range(0, 101):
    if i == 0:
        print(i)
    elif i % 3 == 0:
        if i % 5 == 0:
            print('FizzBuzz')
        else:
            print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
