#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Copyright (c) 2017 Xu Zhihao (Howe).  All rights reserved.

This program is free software; you can redistribute it and/or modify

"""
import time
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

class Solution1(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

if __name__ == "__main__":
    nums = [2, 7, 11, 15, 0]
    target = 9
    now = time.time()
    print Solution1().twoSum(nums, target)
    print time.time() - now

    now1 = time.time()
    print Solution().twoSum(nums, target)
    print time.time() - now1