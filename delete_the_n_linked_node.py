#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@author  : shengxd
@Contact : shengxd@huahuan.com
@File    :   delete_the_n_linked_node.py
@Time    :   2019/11/11 18:30
@Desc    :

"""
# import os
"""
Definition of ListNode
"""


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next



class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        val_list = []
        if head == None:
            return head
        p = head
        while p:
            val_list.append(p.val)
            p = p.next
        if n > len(val_list):
            return head
        val_list.pop(-n)
        if len(val_list) == 0:
            return
        else:
            head_node = ListNode(val_list[0])
            q = head_node
            for i in range(1, len(val_list)):
                node = ListNode(val_list[i])
                q.next = node
                q = q.next
            return head_node