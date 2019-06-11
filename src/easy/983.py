#!/usr/bin/env python
# @Time    : 2019/6/11 11:14
# @Author  : LiuWei
# @Site    : 
# @File    : 983.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
"""
938. Range Sum of BST
Easy

344

54

Favorite

Share
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.



Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23


Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.

为啥我的遍历的解决方案所花费的时间比较长,性能上有其他能优化的地方?
"""


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        result = 0
        if root is not None:
            if root.val >= L and root.val <= R:
                result = result + root.val
            result = result + self.rangeSumBST(root.left, L, R)
            result = result + self.rangeSumBST(root.right, L, R)
            return result
        return result


if __name__ == "__main__":
    root = TreeNode(2)
    tree1 = TreeNode(3)
    tree2 = TreeNode(4)
    root.left = tree1
    root.right = tree2

    tree3 = TreeNode(6)
    tree4 = TreeNode(4)
    tree1.left = tree3
    tree2.right = tree4

    solution = Solution()
    assert solution.rangeSumBST(root, 0, 5) == 13
