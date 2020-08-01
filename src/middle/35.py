"""
35. 搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0
通过次数219,971提交次数471,797


解题思路：
1.遍历数组，存在返回，大于向后移，小于返回当前下标
2.二分查找变形，存在返回，不存在最后判断mid，小于mid返回mid，大于mid返回mid+1
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if target < nums[0]:
            return 0
        if target > nums[n-1]:
            return n

        left = 0
        right = n - 1
        mid = int((right + left) / 2)
        while left <= right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            mid = int((right + left) / 2)

        if nums[mid] > target:
            return mid
        else:
            return mid + 1


if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([], 2))
    print(s.searchInsert([1, 2, 3, 4, 5, 6, 7, 8], 9))
    print(s.searchInsert([1, 2, 3, 4, 5, 6, 7, 8], 0))
    print(s.searchInsert([1, 2, 3, 4, 5, 6, 7, 8], 4))
    print(s.searchInsert([1, 2, 3, 5, 6, 7, 8], 4))
    print(s.searchInsert([1, 2, 3, 5, 7, 8], 4))
