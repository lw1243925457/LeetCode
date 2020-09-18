# 计算给定二叉树的所有左叶子之和。 
# 
#  示例： 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24 
# 
#  
#  Related Topics 树 
#  👍 190 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self._leftAmount(root)

    def _leftAmount(self, node):
        if not node:
            return 0
        amount = 0
        if node.left and not node.left.left and not node.left.right:
            amount += node.left.val
        amount += self._leftAmount(node.left)
        amount += self._leftAmount(node.right)
        return amount
# leetcode submit region end(Prohibit modification and deletion)
