#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Copyright (c) 2017 Xu Zhihao (Howe).  All rights reserved.

This program is free software; you can redistribute it and/or modify

"""
carray = False

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self):
        self.val = None
        self.next = None

class ListNode_handle:
    def __init__(self):
        self.cur_node = None

    def add(self, data):
        #add a new node pointed to previous node
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node

    def print_ListNode(self, node):
        while node:
            print '\nnode: ', node, ' value: ', node.val, ' next: ', node.next
            node = node.next


    def _reverse(self, nodelist):
        list = []
        while nodelist:
            list.append(nodelist.val)
            nodelist = nodelist.next
        result = ListNode()
        result_handle = ListNode_handle()
        for i in list:
            result = result_handle.add(i)
        return result

    def get_list(self, nodelist):
        list = []
        while nodelist:
            list.append(nodelist.val)
            nodelist = nodelist.next
        return list


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        global carry
        carry = False
        result_handle = ListNode_handle()
        result = ListNode()
        while l1 != None or l2 != None:
            if not carry:
                if l1 != None and l2 != None:
                    l3_val = l1.val + l2.val
                elif l1 == None and l2 != None:
                    l3_val = l2.val
                elif l1 != None and l2 == None:
                    l3_val = l1.val
                else:
                    pass
            else:
                if l1 != None and l2 != None:
                    l3_val = l1.val + l2.val + 1
                elif l1 == None and l2 != None:
                    l3_val = l2.val + 1
                elif l1 != None and l2 == None:
                    l3_val = l1.val + 1
                else :
                    pass
                carry = False
            if l3_val < 10:
                result = result_handle.add(l3_val)
            else:
                result = result_handle.add(l3_val%10)
                carry = True
            try:
                l1 = l1.next
            except:
                pass
            try:
                l2 = l2.next
            except:
                pass
        result = result_handle._reverse(result)
        result_list = []
        result_list = result_handle.get_list(result)
        if carry:
            result_list.append(1)
            result = result_handle.add(1)
            result = result_handle._reverse(result)
        result_handle.print_ListNode(result)
        return result_list

if __name__ == "__main__":
    # creat 2 linked lists
    ListNode_1 = ListNode_handle()
    l1 = ListNode()
    l1_list = [1,8,3]
    for i in l1_list:
        l1 = ListNode_1.add(i)

    ListNode_2 = ListNode_handle()
    l2 = ListNode()
    l2_list = [9]
    for i in l2_list:
        l2 = ListNode_2.add(i)
    #reverse 2 linked lists
    l1 = ListNode_1._reverse(l1)
    l2 = ListNode_2._reverse(l2)

    ListNode_1.print_ListNode(l1)
    #get result
    result = Solution().addTwoNumbers(l1, l2)
    print result