#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Copyright (c) 2017 Xu Zhihao (Howe).  All rights reserved.

This program is free software; you can redistribute it and/or modify

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = result = ''
        for i in s:
            if i not in temp:
                temp += i
            else:
                index = temp.index(i)
                temp = temp[index+1:] + i
            if len(result) < len(temp):
                result = temp
            print temp, result
        return len(result)



if __name__ == "__main__":
    string = "abcabcbb"
    result = Solution().lengthOfLongestSubstring(string)
    print result