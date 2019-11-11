#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@author  : shengxd
@Contact : shengxd@huahuan.com
@File    :   binary_tree.py
@Time    :   2019/11/7 17:10
@Desc    :
根据前序遍历和中序遍历树构造二叉树.
preorder and inorder traversal of a tree
你可以假设树中不存在相同数值的节点
样例
样例 1:

输入：[],[]
输出：{}
解释：
二叉树为空
样例 2:

输入：[2,1,3],[1,2,3]
输出：{2,1,3}
解释：
二叉树如下
  2
 / \
1   3

前序遍历为先遍历根结点，中序遍历根结点在中间
1.前序遍历，取最前面的数字，建立根结点
2.在中序遍历数组中寻找根结点的位置
3.中序遍历根结点前的子数组为该根结点的左子树的中序遍历，长度leftlenght；根结点后的子数组为该根结点的右子树的中序遍历，长度为rightlength；
4.前序遍历根结点后先遍历左子树，后遍历右子树；所以前序遍历数组根结点向后leftlenght长度的子数组为左子树的前序遍历，再往后为右子树的中序遍历
5.迭代创建左右子树
"""


"""
Definition of TreeNode:

"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if preorder == [] or inorder == []:
            return None
        if set(preorder) != set(inorder):
            return None
        # 创建根节点
        root_tree_node = TreeNode(preorder[0])
        # 判断根节点是否在中序列表中
        if root_tree_node.val not in inorder:
            return None
        else:
            root_tree_node_index = inorder.index(root_tree_node.val)
            # 得到左子树的前序和中序遍历列表
            left_tree_preorder = preorder[1:(root_tree_node_index+1)]
            left_tree_inorder = inorder[:root_tree_node_index]
            # 得到右子树的前序和中序遍历列表
            right_tree_preorder = preorder[(root_tree_node_index+1):]
            right_tree_inorder = inorder[(root_tree_node_index+1):]

            # 创建左右子树节点,递归调用
            root_tree_node.left = self.buildTree(left_tree_preorder, left_tree_inorder)
            root_tree_node.right = self.buildTree(right_tree_preorder, right_tree_inorder)

            return root_tree_node


if __name__ == "__main__":
    s = Solution()
    s.buildTree([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7])





