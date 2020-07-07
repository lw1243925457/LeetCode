"""
112. 路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

通过次数102,080提交次数202,614
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        return self.canAdd(root, sum, 0)

    def canAdd(self, root, sum, value):
        if root.left is None and root.right is None:
            if root.val + value == sum:
                return True
            else:
                return False

        left = False
        if root.left is not None:
            left = self.canAdd(root.left, sum, root.val + value)

        right = False
        if root.right is not None:
            right = self.canAdd(root.right, sum, root.val + value)

        return left or right
