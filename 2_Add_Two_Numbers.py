#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Copyright (c) 2017 Xu Zhihao (Howe).  All rights reserved.

This program is free software; you can redistribute it and/or modify

"""
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

    def print_ListNode(self):
        node = self.cur_node
        while node:
            print '\n\nnode: ', node, ' value: ', node.val, ' next: ', node.next
            node = node.next



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = False
        new_node = ListNode()




if __name__ == "__main__":
    # creat 2 linked lists
    ListNode_1 = ListNode_handle()
    ListNode_1.add(2)
    ListNode_1.add(4)
    ListNode_1.add(3)
    ListNode_2 = ListNode_handle()
    ListNode_2.add(5)
    ListNode_2.add(6)
    ListNode_2.add(4)

    ListNode_1.print_ListNode()
    ListNode_2.print_ListNode()

