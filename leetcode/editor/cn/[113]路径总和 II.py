# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例: 
# 给定如下二叉树，以及目标和 sum = 22， 
# 
#                5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
#  
# 
#  返回: 
# 
#  [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#  
#  Related Topics 树 深度优先搜索 
#  👍 302 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        self._dfs(root, sum, [], 0, ans)
        return ans

    def _dfs(self, node, sum, path, count, ans):
        if not node.left and not node.right:
            if count + node.val == sum:
                ans.append(path.copy() + [node.val])
            return
        count += node.val
        path.append(node.val)
        if node.left:
            self._dfs(node.left, sum, path, count, ans)
        if node.right:
            self._dfs(node.right, sum, path, count, ans)
        path.pop()
# leetcode submit region end(Prohibit modification and deletion)
