# 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节
# 点值之和。 
# 
#  
# 
#  例如： 
# 
#  输入: 原始二叉搜索树:
#               5
#             /   \
#            2     13
# 
# 输出: 转换为累加树:
#              18
#             /   \
#           20     13
#  
# 
#  
# 
#  注意：本题和 1038: https://leetcode-cn.com/problems/binary-search-tree-to-greater-s
# um-tree/ 相同 
#  Related Topics 树 
#  👍 339 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.total = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        self._add(root)
        return root

    def _add(self, node):
        if not node:
            return
        self._add(node.right)
        self.total += node.val
        node.val = self.total
        self._add(node.left)

# leetcode submit region end(Prohibit modification and deletion)
