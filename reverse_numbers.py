# -*- coding: utf-8 -*-

'''
题目：
对于一个整数X，定义操作rev(X)为将X按数位翻转过来，并且去除掉前导0。例如:
如果 X = 123，则rev(X) = 321;
如果 X = 100，则rev(X) = 1.
现在给出整数x和y,要求rev(rev(x) + rev(y))为多少？
'''


def rev_str(str):
    return str[::-1]


def rev_str2(str):
    if str == '':
        return str
    else:
        return rev_str2(str[1:]) + str[0]


def rev_str3(str):
    str = list(str)
    # str =  str.reverse()
    str.reverse()
    a = ''
    return a.join(str)


def rev_num(num):
    a = rev_str3(num)
    a.strip('0')
    num = int(a)
    return num


num1 = input('Please input the first number: ')
num2 = input('Please input the second number: ')
num1 = rev_num(num1)
num2 = rev_num(num2)
sum_ = num1 + num2
print(sum_)
