#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Copyright (c) 2017 Xu Zhihao (Howe).  All rights reserved.

This program is free software; you can redistribute it and/or modify

"""

# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                print i, nums[i]
                print buff_dict
                return [buff_dict[nums[i]], i]
            else:
                print i, target - nums[i]
                buff_dict[target - nums[i]] = i


if __name__ == "__main__":
    string = "abcabcbb"
    result = Solution().twoSum([1,4,3,5,2,6], 6)
    print result