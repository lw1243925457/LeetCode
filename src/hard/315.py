"""
315. 计算右侧小于当前元素的个数
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例:

输入: [5,2,6,1]
输出: [2,1,1,0]
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.
"""
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0] * len(nums)
        for i in range(0, len(nums)):
            for j in range(len(nums) - 1, i, -1):
                if nums[j] < nums[i]:
                    counts[i] += 1
        print(counts)
        return counts


if __name__ == "__main__":
    s = Solution()
    assert s.countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0]
