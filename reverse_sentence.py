# -*- coding: utf-8 -*-

'''
给定一个句子（只包含字母和空格）， 将句子中的单词位置反转，
单词用空格分割, 单词之间只有一个空格，前后没有空格。
比如： （1） “hello xiao mi”-> “mi xiao hello”
'''


def reverse_sentence(sentence):
    a = sentence.split(' ')
    rev = ' '
    rev = rev.join(a[::-1])
    return print(rev)


sentence_ = input('Please input a sentence: ')
reverse_sentence(sentence_)
