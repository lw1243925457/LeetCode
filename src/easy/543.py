"""
543. 二叉树的直径
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。

通过次数25,560提交次数53,303

没有完全理清解答......
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        stack = []
        tree = root
        results = []
        while tree is not None or len(stack) != 0:
            while tree is not None:
                print(self.getHeight(tree.left, 0), self.getHeight(tree.right, 0))
                results.append(self.getHeight(tree.left, 0) + self.getHeight(tree.right, 0))
                stack.append(tree)
                tree = tree.left
            if len(stack) != 0:
                tree = stack.pop()
                tree = tree.right
        print(results)
        return max(results)

    def getHeight(self, root: TreeNode, height):
        if root is None:
            return height
        lh = self.getHeight(root.left, height + 1)
        rh = self.getHeight(root.right, height + 1)
        return max(lh, rh)


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)

    s = Solution()
    assert s.diameterOfBinaryTree(tree) == 3

    tree.left.right.right = TreeNode(6)
    assert s.diameterOfBinaryTree(tree) == 4

    tree.left.left.left = TreeNode(7)
    tree.left.left.left.left = TreeNode(8)
    tree.left.left.left.right = TreeNode(9)
    tree.left.left.left.left.left = TreeNode(10)
    tree.left.left.left.left.right = TreeNode(10)
    tree.left.left.left.right.left = TreeNode(9)

    tree.right.left = TreeNode(7)
    tree.right.left.left = TreeNode(7)
    tree.right.left.left.left = TreeNode(8)
    tree.right.left.left.right = TreeNode(9)
    tree.right.left.left.left.left = TreeNode(10)
    tree.right.left.left.left.right = TreeNode(10)
    tree.right.left.left.right.left = TreeNode(9)
    tree.right.left.left.right.right = TreeNode(9)
    tree.right.left.left.right.right = TreeNode(9)
    assert s.diameterOfBinaryTree(tree) == 10
