# -*- coding: utf-8 -*-

'''
输入两个字符串，从第一字符串中删除第二个字符串中所有的字符。
例如，输入”They are students.”和”aeiou”，
则删除之后的第一个字符串变成”Thy r stdnts.”
'''

# a = input('please input the first string: ')
# b = input('please input the second string: ')
# b = set(b)
#
# for i in b:
#     a = a.replace(i, '')
# print(a)



def delete_str(str1, str2):
    len2 = len(str2)
    len1 = len(str1)

    for i in range(len2 - 1):
        for j in range(len1 - 1):
            if str1[j] == str2[i]:
                str1 = str1[:j] + str1[j + 1:]
    return str1


a = input('Please input the first string: ')
b = input('Please input the second string: ')

del_ = delete_str(a, b)
print(del_)
