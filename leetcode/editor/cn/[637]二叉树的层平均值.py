# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。 
# 
#  
# 
#  示例 1： 
# 
#  输入：
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 输出：[3, 14.5, 11]
# 解释：
# 第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  节点值的范围在32位有符号整数范围内。 
#  
#  Related Topics 树 
#  👍 165 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return []

        ans = []
        stack = [root]

        while stack:
            size = len(stack)
            amount = 0
            for i in range(0, size):
                node = stack.pop(0)
                amount += node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            ans.append(amount / size)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
