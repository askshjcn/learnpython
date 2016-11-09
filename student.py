#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' class test '

__author__ = 'askshjcn'

import sys

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            #raise ValueError('bad score')
            self.__score = score / 10


args = sys.argv
bart = Student(args[1], args[2])
bart.print_score()
bart.set_score(1000)
bart.print_score()
bart.set_score(99)
bart.print_score()