#!/usr/bin/env python
# @Time    : 2019/3/26 18:49
# @Author  : LiuWei
# @Site    : 
# @File    : rotateString.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# 796. 旋转字符串
"""
给定两个字符串, A 和 B。

A 的旋转操作就是将 A 最左边的字符移动到最右边。 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。如果在若干次旋转操作之后，A 能变成B，那么返回True。

示例 1:
输入: A = 'abcde', B = 'cdeab'
输出: true

示例 2:
输入: A = 'abcde', B = 'abced'
输出: false

注意：

A 和 B 长度不超过 100。

前提：两字符串长度相等才有可能返回true
边界：空字符串，直接相等
遍历B字符串，寻找到相等于A首字母位置，将字符串分成两相等
验证两部分是否相等
切割时的极端情况：第一位就相等，0；最后一位相等
第一位相等：判断整个字符串是否相等即可
最后一位是否相等：A去首，B去尾后判断是否相等
一般情况：A[0:len(B)-index] A[len(B)-index:] B[:index] B[index:]

执行用时 : 52 ms, 在Rotate String的Python3提交中击败了19.91% 的用户
内存消耗 : 13 MB, 在Rotate String的Python3提交中击败了0.00% 的用户

直击灵魂的Python解答
return len(A) == len(B) and B in A + A
"""
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        if A == "" and B == "":
            return True

        AFirst = A[0]
        length = len(A)
        for i in range(0, length):
            if B[i] == AFirst:
                if i == 0 and A == B:
                    return True
                if i == (length - 1) and A[1:] == B[:length - 1]:
                    return True
                # print(i, A[0:length - i], B[i:], A[length - i:], B[:i])
                if A[0:length - i] == B[i:] and A[length - i:] == B[:i]:
                    return True
        return False


if __name__ == "__main__":
    solution = Solution()
    A = 'abcde'
    B = 'cdeab'
    if solution.rotateString(A, B):
        print("YES")
    else:
        print("ERROR")

    A = 'abcde'
    B = 'abced'
    if not solution.rotateString(A, B):
        print("YES")
    else:
        print("ERROR")
