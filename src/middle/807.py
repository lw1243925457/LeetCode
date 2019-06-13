#!/usr/bin/env python
# @Time    : 2019/6/13 17:05
# @Author  : LiuWei
# @Site    : 
# @File    : 807.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
"""
807. Max Increase to Keep City Skyline
Medium

523

128

Favorite

Share
In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well.

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?

Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation:
The grid is:
[ [3, 0, 8, 4],
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]

Notes:

1 < grid.length = grid[0].length <= 50.
All heights grid[i][j] are in the range [0, 100].
All buildings in grid[i][j] occupy the entire grid cell: that is, they are a 1 x 1 x grid[i][j] rectangular prism.

解题思路:
1.找出上下看的最高建筑列表L1
2.找出左右看的最高建筑列表L2
3.遍历整个二位数组,每个对应的值为Min(L1[i],L2[j]),累计后减去原来建筑的总高度

Runtime: 44 ms, faster than 93.63% of Python3 online submissions for Max Increase to Keep City Skyline.
Memory Usage: 13.3 MB, less than 35.09% of Python3 online submissions for Max Increase to Keep City Skyline.
"""
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        L1 = []
        L2 = []

        origin = 0
        for i in range(0, len(grid[0])):
            for j in range(0, len(grid)):
                origin = origin + grid[i][j]
                if len(L1) == i:
                    L1.append(grid[j][i])
                if grid[j][i] > L1[i]:
                    L1[i] = grid[j][i]

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if len(L2) == i:
                    L2.append(grid[i][j])
                if grid[i][j] > L2[i]:
                    L2[i] = grid[i][j]

        result = 0
        for i in range(0, len(L2)):
            for j in range(0, len(L1)):
                result = result + min(L1[j], L2[i])
        return result - origin


if __name__ == "__main__":
    solution = Solution()
    grid = [[3, 0, 8, 4],
            [2, 4, 5, 7],
            [9, 2, 6, 3],
            [0, 3, 1, 0]]
    assert solution.maxIncreaseKeepingSkyline(grid) == 35
