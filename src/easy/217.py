"""
217. 存在重复元素
给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。



示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
通过次数158,723提交次数300,270


解题思路：
一个hashmap统计判断即可，数据只比遍历一次，时间复杂度O(N)
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if num in count:
                return True
            else:
                count[num] = 1
        return False
