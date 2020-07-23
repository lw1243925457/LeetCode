"""
111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

通过次数93,729提交次数218,080
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        depth = 1
        q = [root]
        while len(q) > 0:
            beforeSize = len(q)
            for i in range(0, beforeSize):
                item = q[i]
                if item.left is None and item.right is None:
                    return depth
                if item.left is not None:
                    q.append(item.left)
                if item.right is not None:
                    q.append(item.right)
            q = q[beforeSize:]
            depth = depth + 1
        return depth


if __name__ == "__main__":
    s = Solution()

    root = None
    print(s.minDepth(root))

    root = TreeNode(1)
    print(s.minDepth(root))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(3)
    print(s.minDepth(root))
