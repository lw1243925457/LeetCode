# 小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 `leaves`， 字符串 `leaves` 仅包含小写字符 `r` 和 `
# y`， 其中字符 `r` 表示一片红叶，字符 `y` 表示一片黄叶。
# 出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，但均需大于等于 1。每次调整操作，小扣可以将一片红叶替
# 换成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。
# 
# **示例 1：**
# >输入：`leaves = "rrryyyrryyyrr"`
# >
# >输出：`2`
# >
# >解释：调整两次，将中间的两片红叶替换成黄叶，得到 "rrryyyyyyyyrr"
# 
# **示例 2：**
# >输入：`leaves = "ryr"`
# >
# >输出：`0`
# >
# >解释：已符合要求，不需要额外操作
# 
# **提示：**
# - `3 <= leaves.length <= 10^5`
# - `leaves` 中只包含字符 `'r'` 和字符 `'y'` 👍 26 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumOperations(self, leaves: str) -> int:
        size = len(leaves)
        left, right = 0, size - 1
        count = 0
        ybefore = False

        while left < size:
            if leaves[left] == "y":
                ybefore = True
                count += 1
                left += 1
            else:
                break
        while right > left and right >= 0:
            if leaves[right] == "y":
                count += 1
                right -= 1
            else:
                break

        for i in range(left, right+1):
            if ybefore and i > 0 and leaves[i] == "r":
                count += 1
        print(count)
        return count
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().minimumOperations("yry") == 3
    assert Solution().minimumOperations("ryyyr") == 0
    assert Solution().minimumOperations("ryr") == 0
