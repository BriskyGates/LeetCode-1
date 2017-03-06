#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Copyright (c) 2017 Xu Zhihao (Howe).  All rights reserved.

This program is free software; you can redistribute it and/or modify

"""


class Solution(object):
    def findMedianSortedArrays1(self, nums1, nums2):
        # return self.time_complex_n(nums1, nums2)
        return self.time_complex_logn(nums1, nums2)

    def time_complex_logn(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        tl = m + n
        middle,carray = (tl,2)
        index_1 = None
        index_2 = None
        if carray: #even
            pass
        else:      #odd
            pass

    def find(self, nums1, nums2, n, m):
        pass

    def binary_check(self, num, begin, end, list):
        pass


    def time_complex_n(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        index, carry = divmod(len(nums), 2)
        if carry == 1:
            result = float(nums[index])
        else:
            result = (nums[index] + nums[index-1])/2.0
        return result

    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

if __name__ == '__main__':

    nums1 = [1, 7]
    nums2 = [2, 3, 4, 5, 6, 8]
    print Solution().findMedianSortedArrays(nums1, nums2)
