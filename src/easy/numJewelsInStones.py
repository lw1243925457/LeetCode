#!/usr/bin/env python
# @Time    : 2019/1/14 22:15
# @Author  : LiuWei
# @Site    : 
# @File    : numJewelsInStones.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# 771. 宝石与石头


class Solution:
    """
    J 中不会出现重复
    S 中会出现重复
    第一层遍历J，第二层遍历S
    当J中的字母与S中相等时统计+1
    """
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = 0
        for ichar in J:
            for jchar in S:
                if ichar == jchar:
                    jewels = jewels + 1
        return jewels


if __name__ == "__main__":
    solution = Solution()
    assert solution.numJewelsInStones("aA", "AAAbbbbb") == 3
