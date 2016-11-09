#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
decorators
'''

__author__ = 'askshjcn'

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' %func.__name__)
        return func(*args, **kw)
    return wrapper
    
@log
def now():
    print('2016-11-9')
    
now()
