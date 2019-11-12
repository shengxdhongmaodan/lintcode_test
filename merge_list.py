#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@author  : shengxd
@Contact : shengxd@huahuan.com
@File    :   merge_list.py
@Time    :   2019/11/11 18:06
@Desc    :

"""
"""
Definition of ListNode
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """

    def mergeTwoLists(self, l1, l2):
        # write your code herel
        merge_list = []
        if l1 == None and l2 == None:
            return
        elif l1 == None and l2 != None:
            return l2
        elif l1 != None and l2 == None:
            return l1
        elif l1 != None and l2 != None:
            while l1:
                merge_list.append(l1.val)
                l1 = l1.next
            while l2:
                merge_list.append(l2.val)
                l2 = l2.next
            merge_list.sort()
            head_node = ListNode(merge_list[0])
            p = head_node
            for i in range(1, len(merge_list)):
                node = ListNode(merge_list[i])
                p.next = node
                p = p.next
            return head_node