"""
3. 秋叶收藏集
通过的用户数353
尝试过的用户数1242
用户总通过次数357
用户总提交次数2905
题目难度Medium
小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 leaves， 字符串 leaves 仅包含小写字符 r 和 y， 其中字符 r 表示一片红叶，字符 y 表示一片黄叶。
出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，但均需大于等于 1。每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。

示例 1：

输入：leaves = "rrryyyrryyyrr"

输出：2

解释：调整两次，将中间的两片红叶替换成黄叶，得到 "rrryyyyyyyyrr"

示例 2：

输入：leaves = "ryr"

输出：0

解释：已符合要求，不需要额外操作

提示：

3 <= leaves.length <= 10^5
leaves 中只包含字符 'r' 和字符 'y'
"""


class Solution:
    def minimumOperations(self, leaves: str) -> int:
        size = len(leaves)
        left, right = 0, size - 1
        count = 0

        for i in range(0, size):
            if leaves[i] == "y":
                break
            left += 1
        for i in range(size - 1, -1, -1):
            if leaves[i] == 'y':
                break
            right -= 1

        if left == right:
            return 0

        for i in range(left, right + 1):
            if leaves[i] == 'r':
                count += 1

        if count == 0:
            if (left == 0 and right == size - 1) or (left == size - 1 and right == 0):
                return 0
            return 1
        return count