"""
99. 恢复二叉搜索树
二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。

示例 1:

输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2
示例 2:

输入: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

输出: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
进阶:

使用 O(n) 空间复杂度的解法很容易实现。
你能想出一个只使用常数空间的解决方案吗？
通过次数29,923提交次数49,480


解题思路：
1.中序遍历数组递增，遍历一次数组，把不符合递增的位置找出来，进行交换即可
    1.中序遍历得到数组
    2.当查找到不符合条件的项，记录位置（技巧，先记录第一个，第二个记录为第一个加一，后面更新第二个
    3.交换节点的值即可

2.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nums = []

        def midOrder(node: TreeNode):
            if node:
                midOrder(node.left)
                nums.append(node)
                midOrder(node.right)

        p = root
        midOrder(p)

        p1, p2 = None, None
        for i in range(0, len(nums)-1):
            if nums[i].val > nums[i+1].val:
                if p1 is None:
                    p1 = nums[i]
                    p2 = nums[i+1]
                else:
                    p2 = nums[i+1]

        for i in range(0, len(nums)):
            print(nums[i].val, end=" ")
        print()
        print(p1.val)
        if p1 and p2:
            p1.val, p2.val = p2.val, p1.val
        elif not p2:
            p1.val, p1.right.val = p1.right.val, p1.val


def midPrint(node):
    if node:
        midPrint(node.left)
        print(node.val, end=" ")
        midPrint(node.right)


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(3)
    tree.left.right = TreeNode(2)

    solve = Solution()
    solve.recoverTree(tree)

    midPrint(tree)
