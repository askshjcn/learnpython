#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
str to int
'''

__author__ = 'Ma Jie'

from functools import reduce
def str2int(s):
    def str2char(x, y):
        return 10 * x + y
    def char2int(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    n = reduce(str2char, map(char2int, s))
    return n

s = input('please input a int number:')
print(s)
print(str2int(s))
