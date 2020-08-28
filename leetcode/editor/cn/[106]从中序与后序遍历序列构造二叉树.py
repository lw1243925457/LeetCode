# 根据一棵树的中序遍历与后序遍历构造二叉树。 
# 
#  注意: 
# 你可以假设树中没有重复的元素。 
# 
#  例如，给出 
# 
#  中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3] 
# 
#  返回如下的二叉树： 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
#  Related Topics 树 深度优先搜索 数组 
#  👍 272 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inSize, postSize = len(inorder), len(postorder)
        if inSize != postSize or inSize == 0:
            return None

        inIndex, postIndex = {}, {}
        for i in range(0, postSize):
            inIndex[inorder[i]] = i
            postIndex[postorder[i]] = i
        tree = self._build(inorder, 0, inSize - 1, postorder, 0, postSize - 1, inIndex, postIndex)
        return tree

    def _build(self, inorder, inl, inr, postorder, postl, postr, inIndex, postIndex):
        if inl > inr or postl > postr:
            return None

        father = postorder[postr]
        tree = TreeNode(father)

        inFatherPos = inIndex[father]
        lchildrenLength = inFatherPos - inl
        linr = inFatherPos - 1
        lpostr = postl + lchildrenLength - 1
        rinl = inFatherPos + 1
        rpostl = postl + lchildrenLength
        tree.left = self._build(inorder, inl, linr, postorder, postl, lpostr, inIndex, postIndex)
        tree.right = self._build(inorder, rinl, inr, postorder, rpostl, postr - 1, inIndex, postIndex)
        return tree


# leetcode submit region end(Prohibit modification and deletion)


def preorder(node):
    if not node:
        return
    print(node.val, end=" ")
    preorder(node.left)
    preorder(node.right)


if __name__ == "__main__":
    tree = Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    # preorder(tree)
