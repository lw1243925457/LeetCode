"""
18. 四数之和
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
通过次数92,766提交次数243,938
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums = sorted(nums)
        end = len(nums) - 1
        result = []
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = end
                while left < right:
                    if (nums[i] + nums[j] + nums[left] + nums[right]) == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left = self.movel(left, right, nums)
                        right = self.mover(left, right, nums)
                    elif (nums[i] + nums[j] + nums[left] + nums[right]) < target:
                        left = self.movel(left, right, nums)
                    elif (nums[i] + nums[j] + nums[left] + nums[right]) > target:
                        right = self.mover(left, right, nums)
        return result

    def movel(self, left, right, nums):
        temp = left + 1
        while temp < right and nums[temp] == nums[left]:
            temp = temp + 1
        return temp

    def mover(self, left, right, nums):
        temp = right - 1
        while temp > left and nums[temp] == nums[right]:
            temp = temp - 1
        return temp


if __name__ == "__main__":
    s = Solution()
    print(s.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
