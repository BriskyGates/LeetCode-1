#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Copyright (c) 2017 Xu Zhihao (Howe).  All rights reserved.

This program is free software; you can redistribute it and/or modify

"""


class Solution:
    def str_compress(self, s):
        result = temp = seg = ''
        cout = 1
        for i in s:
            if i.__hash__() == temp.__hash__():
                cout += 1
                seg = i + str(cout)
            else:
                if seg != '':
                    result += seg
                temp = seg = i
                cout = 1
        return result + seg


if __name__ == "__main__":
    s = 'aaaabbbccccabsdsdaaadddddd'
    print Solution().str_compress(s)


