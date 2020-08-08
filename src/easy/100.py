"""
100. 相同的树
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false
通过次数110,615提交次数188,281


解题思路：
中序遍历，比较即可,中序遍历思路错了
应该使用前序遍历，还原成原本输入的数组形式即可，需要注意的是为空填充-1或null也行
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def preOrder(node: TreeNode, nums: List[int]) -> None:
            if not node:
                return
            nums.append(node.val)
            if node.left:
                preOrder(node.left, nums)
            else:
                nums.append(-1)
            if node.right:
                preOrder(node.right, nums)
            else:
                nums.append(-1)

        pnums = []
        qnums = []
        preOrder(p, pnums)
        preOrder(q, qnums)

        if len(pnums) != len(qnums):
            return False

        for i in range(0, len(pnums)):
            if pnums[i] != qnums[i]:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    node1 = TreeNode(1)
    node1.left = TreeNode(1)

    node2 = TreeNode(1)
    node2.right = TreeNode(1)
    print(s.isSameTree(node1, node2))

