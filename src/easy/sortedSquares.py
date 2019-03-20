#!/usr/bin/env python
# @Time    : 2019/3/20 19:24
# @Author  : LiuWei
# @Site    : 
# @File    : sortedSquares.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# 977. 有序数组的平方
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = []

        middle = 0
        for i in range(0, len(A)):
            if A[i] >= 0:
                middle = i
                break

        length = len(A)
        left = middle - 1
        right = middle
        while True:
            if left < 0 and right >= length:
                break

            if left < 0 and right < length:
                result.append(A[right] * A[right])
                right = right + 1
                continue

            if left >= 0 and right >= length:
                result.append(A[left] * A[left])
                left = left - 1
                continue

            if left >= 0 and right < length:
                if abs(A[left]) > abs(A[right]):
                    result.append(A[right] * A[right])
                    right = right + 1
                else:
                    result.append(A[left] * A[left])
                    left = left - 1
        return result


if __name__ == "__main__":
    #[-1,2,2]
    #输入：[-4, -1, 0, 3, 10]
    #输出：[0, 1, 9, 16, 100]
    solution = Solution()
    print(solution.sortedSquares([-4, -1, 0, 3, 10]))