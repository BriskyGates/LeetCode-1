#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Copyright (c) 2017 Xu Zhihao (Howe).  All rights reserved.

This program is free software; you can redistribute it and/or modify

"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        [[result.extend([j, i]) for i in range(len(nums)) if nums[i] + nums[j] == target and i != j and result == []] for j in range(len(nums))]
        return result


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print Solution().twoSum(nums, target)