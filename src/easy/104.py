"""
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

通过次数222,019提交次数299,188


解题思路：
使用二叉树的层次遍历，记录并输出一共多少层即可
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        depth = 1
        stack1 = [root]
        while len(stack1) != 0:
            temp = []
            for item in stack1:
                if item.left is not None:
                    temp.append(item.left)
                if item.right is not None:
                    temp.append(item.right)

            if len(temp) != 0:
                depth += 1
            stack1 = temp

        return depth


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    s = Solution()
    print(s.maxDepth(root))
