#!/usr/bin/env python
# @Time    : 2019/3/21 21:08
# @Author  : LiuWei
# @Site    : 
# @File    : twoSum.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# 1. 两数之和
# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
# 执行用时 : 5728 ms, 在Two Sum的Python3提交中击败了30.74% 的用户
# 内存消耗 : 13.8 MB, 在Two Sum的Python3提交中击败了0.84% 的用户
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == "__main__":
    solution = Solution()
    ret = solution.twoSum([2, 7, 11, 15], 9)
    print(ret)
