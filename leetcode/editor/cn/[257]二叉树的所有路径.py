# 给定一个二叉树，返回所有从根节点到叶子节点的路径。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例: 
# 
#  输入:
# 
#    1
#  /   \
# 2     3
#  \
#   5
# 
# 输出: ["1->2->5", "1->3"]
# 
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3 
#  Related Topics 树 深度优先搜索 
#  👍 313 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = []

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        self.dfs(root, [])
        return self.ans

    def dfs(self, node, path):
        if node.left is None and node.right is None:
            self.ans.append("->".join(path[::] + [str(node.val)]))
        if node.left is not None:
            self.dfs(node.left, path[::] + [str(node.val)])
        if node.right is not None:
            self.dfs(node.right, path[::] + [str(node.val)])

# leetcode submit region end(Prohibit modification and deletion)
