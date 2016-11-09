#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'askshjcn'

'''
test1
BMI Calculate
'''

h = input('input your height:(m)')
height = float(h)
w = input('input your weight:(kg)')
weight = float(w)
bmi = weight/(height*height)
print('Your BMI is ', bmi)

if bmi > 25:
	print('your are so fat')
elif bmi > 18:
	print('you have a nice body')
else:
	print('you too shou le')
