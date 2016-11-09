#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'askshjcn'

'''
test3
hannuota youxi
'''
def move(n, a, b, c):
	if n == 1:
		print(a, "-->", c)
	else:
		move(n-1, a, c, b)
		print(a, "-->", c)
		move(n-1, b, a, c)

n = int(input('enter a number: '))
move(n, 'A', 'B', 'C')
