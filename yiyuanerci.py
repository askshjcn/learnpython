#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'askshjcn'

'''
test2
hanshu diaoyong
'''

import math

def fangc(a, b, c):
	if a == 0:
		x = -c/b
		return x
	else:
		x = (-b+math.sqrt(b*b-4*a*c))/(2*a)
		y = (-b-math.sqrt(b*b-4*a*c))/(2*a)
		return x, y

print('ax2+bx+c=0,input a, b, c, get x')
a = input('a=')
b = input('b=')
c = input('c=')
a1 = float(a)
b1 = float(b)
c1 = float(c)
x = fangc(a1, b1, c1)
print('x = ',x)
