#!/usr/bin/env python
# @Time    : 2019/6/10 9:25
# @Author  : LiuWei
# @Site    : 
# @File    : 771.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each
character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a"
is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for item in J:
            for jtem in S:
                if item == jtem:
                    count = count + 1
        return count


if __name__ == "__main__":
    solution = Solution()

    J = "aA"
    S = "aAAbbbb"
    assert solution.numJewelsInStones(J, S) == 3

    J = "z"
    S = "ZZ"
    assert solution.numJewelsInStones(J, S) == 0
