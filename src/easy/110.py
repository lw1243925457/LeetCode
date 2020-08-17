"""
110. 平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。


解题思路：
获取左右子树搞定，判断是否符合标准返回
这题需要注意的是左右子树也需要满足标准，当某一个子树不满足标准时，就是false
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = True

    def isBalanced(self, root: TreeNode) -> bool:
        self.dfs(root, 0)
        return self.ans

    def dfs(self, node: TreeNode, height: int) -> int:
        if not node:
            return height - 1
        left = self.dfs(node.left, height + 1)
        right = self.dfs(node.right, height + 1)
        if abs(left - right) > 1:
            self.ans = False
        if left > right:
            return left
        return right


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(9)
    solution = Solution()
    print(solution.isBalanced(root))

    root.left.left = TreeNode(9)
    root.left.left.left = TreeNode(9)
    print(solution.isBalanced(root))

    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(9)
    print(solution.isBalanced(root))
