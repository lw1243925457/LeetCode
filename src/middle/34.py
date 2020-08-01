"""
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
通过次数115,588提交次数288,738


解题思路：
二分查找的变形，这次试用非递归试试
当mid找到时，扩散返回结果即可
高票提交的边界判断给了我一些启示，就加了加，果然有用，就击败90%多了
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        if target < nums[0]:
            return [-1, -1]
        if target > nums[n-1]:
            return [-1, -1]

        left = 0
        right = n - 1
        mid = int((left + right) / 2)

        while left <= right:
            if nums[left] == target:
                return self.centerF(nums, left)
            if nums[right] == target:
                return self.centerF(nums, right)
            if nums[mid] == target:
                return self.centerF(nums, mid)
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            mid = int((left + right) / 2)
        return [-1, -1]

    def centerF(self, nums, mid):
        left = mid
        right = mid
        n = len(nums)
        for i in range(mid - 1, -1, -1):
            if nums[i] == nums[mid]:
                left = i
            else:
                break

        for i in range(mid + 1, n):
            if nums[i] == nums[mid]:
                right = i
            else:
                break
        return [left, right]


if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([], 2))
    print(s.searchRange([1], 2))
    print(s.searchRange([1], 1))
    print(s.searchRange([1, 2, 3, 3, 3, 4, 5, 6, 7, 8], 3))
    print(s.searchRange([1, 2, 3, 3, 3, 4, 5, 6, 7, 8], 9))
