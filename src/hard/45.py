"""
45. 跳跃游戏 II
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。


解题思路：
使用动态规划
当前位置所需最小步数=min（nums【：i】）+1
遍历生成dp一次，内嵌最小步数查找一次，时间复杂度O(N^2)
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        if n == 2:
            return 1

        dp = [0, 1] + ([2 ** 31 + 1] * (n - 2))
        for i in range(2, n):
            for j in range(0, i):
                if j + nums[j] >= i and dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1
        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.jump([2, 3, 1, 1, 4]))
    print(solution.jump([3, 2, 1]))
