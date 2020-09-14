# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。 
# 
#  例如： 
# 给定二叉树 [3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回锯齿形层次遍历如下： 
# 
#  [
#   [3],
#   [20,9],
#   [15,7]
# ]
#  
#  Related Topics 栈 树 广度优先搜索 
#  👍 262 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans = []
        stack = [root]
        changeDir = False
        while stack:
            nodes = []
            size = len(stack)
            for i in range(0, size):
                node = stack.pop(0)
                nodes.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            ans.append(nodes)
            if changeDir:
                ans[-1].reverse()
                changeDir = False
            else:
                changeDir = True
        return ans
# leetcode submit region end(Prohibit modification and deletion)
