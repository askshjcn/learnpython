#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
yanghuisanjiao
get a generator
'''

__author__ = 'Ma Jie'

def yanghuisanjiao():
    L = [1]
    n = 1
    while True:
        try:
            yield L
            L.append(0)
            L = [L[i - 1] + L[i] for i in range(len(L))]
        except StopIteration as e:
            print('fanhui yanghuisanjiao:', e.values)
            break

n = 0
for t in yanghuisanjiao():
    print(t)
    n = n + 1
    if n == 10:
        break
