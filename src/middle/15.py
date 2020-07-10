"""
15. 三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。



示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
通过次数272,739提交次数957,380
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        res = []
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k = len(nums) - 1
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                while nums[j] + nums[k] > -nums[i]:
                    k = k - 1
                if k <= j:
                    break
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])

        print(res)
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    s.threeSum(nums)
    s.threeSum([0, 0, 0, 0])
    s.threeSum([1, -1, -1, 0])
    s.threeSum([-1, 0, 1, 2, -1, -4])
