# 给定一个二叉树，检查它是否是镜像对称的。 
# 
#  
# 
#  例如，二叉树 [1,2,2,3,4,4,3] 是对称的。 
# 
#      1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#  
# 
#  
# 
#  但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的: 
# 
#      1
#    / \
#   2   2
#    \   \
#    3    3
#  
# 
#  
# 
#  进阶： 
# 
#  你可以运用递归和迭代两种方法解决这个问题吗？ 
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 980 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """解题思路：
    一、比较两节点是否相等，两子树节点是否镜像相等
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        """迭代"""
        if not root:
            return True
        stack = [root, root]
        while len(stack) > 0:
            left = stack.pop()
            right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
        return True

    def isSymmetric2(self, root: TreeNode) -> bool:
        """递归"""
        if not root:
            return True
        return self.check(root.left, root.right)

    def check(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return left.val == right.val and self.check(left.left, right.right) and self.check(left.right, right.left)


# leetcode submit region end(Prohibit modification and deletion)
