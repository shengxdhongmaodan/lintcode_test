#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@author  : shengxd
@Contact : shengxd@huahuan.com
@File    :   delete_linked_list.py
@Time    :   2019/11/11 15:43
@Desc    :
372. 在O(1)时间复杂度删除链表节点
中文English
给定一个单链表中的一个等待被删除的节点(非表头或表尾)。请在在 O(1) 时间复杂度删除该链表节点。

样例
样例 1：

输入：
1->2->3->4->null
3
输出：
1->2->4->null
样例 2：

输入：
1->3->5->null
3
输出：
1->5->null

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
    @param: node: the node in the list should be deleted
    @return: nothing
    """
    # def get_node(self,val_list):
    #     self.head_node = ListNode(val_list[0])
    #     p = self.head_node
    #     for i in range(1,len(val_list)):
    #         node = ListNode(val_list[i])
    #         node.value = val_list[i]
    #         p.next = node
    #         p = p.next

    def deleteNode(self, node):
        # write your code here
        val_list = [1, 2, 3, 4]
        head_node = ListNode(val_list[0])
        p = head_node
        for i in range(1, len(val_list)):
            link_node = ListNode(val_list[i])
            link_node.val = val_list[i]
            p.next = link_node
            p = p.next

        if head_node.val == node.val:
            head_node = head_node.next
            return head_node
        else:
            p = head_node
            q = p.next
            while q:
                if q.val == node.val:
                    p.next = q.next
                    break
                else:
                    p = q
                    q = q.next
        return head_node


if __name__ == "__main__":
    s = Solution()
    node = ListNode(3)
    s.deleteNode(node)
