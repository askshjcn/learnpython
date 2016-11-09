#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' class @property '

__author__ = 'askshjcn'


class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be a integer!')
        if value < 640:
            raise ValueError('width is too small!')
        if value > 3000:
            raise ValueError('width is too large!')
        self._width = value

    @property
    def height(self):
        return height._width

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be a integer!')
        if value < 480:
            raise ValueError('height is too small!')
        if value > 1080:
            raise ValueError('height is too large!')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' %s.resolution
