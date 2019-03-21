#!/usr/bin/env python
# @Time    : 2019/3/21 8:41
# @Author  : LiuWei
# @Site    : 
# @File    : majorityElement.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# 169. 求众数
# 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在众数。
# 输入: [3,2,3]
# 输出: 3
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        statistics = {}
        max = len(nums) / 2

        for num in nums:
            if num in statistics:
                statistics[num] = statistics[num] + 1
            else:
                statistics[num] = 1

        for num in statistics:
            if statistics[num] >= max:
                return num


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 3]
    print(solution.majorityElement(nums))

    nums = [2,2,1,1,1,2,2]
    print(solution.majorityElement(nums))

    nums = [6,5,5]
    print(solution.majorityElement(nums))