"""
329. 矩阵中的最长递增路径
给定一个整数矩阵，找出最长递增路径的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

示例 1:

输入: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
输出: 4
解释: 最长递增路径为 [1, 2, 6, 9]。
示例 2:

输入: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
输出: 4
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
通过次数18,107提交次数42,734
"""
from functools import lru_cache
from typing import List


class Solution:
    def __init__(self):
        # 上下左右移动
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if matrix is None or len(matrix) == 0:
            return 0

        @lru_cache(None)
        def dfs(row, col):
            best = 1
            for dx, dy in self.directions:
                newRow = row + dx
                newCol = col + dy
                if 0 <= newRow < n and 0 <= newCol < m and matrix[newRow][newCol] > matrix[row][col]:
                    best = max(best, dfs(newRow,newCol) + 1)
            return best

        n = len(matrix)
        m = len(matrix[0])
        ans = 0
        for i in range(0, n):
            for j in range(0, m):
                ans = max(ans, dfs(i, j))
        return ans




if __name__ == "__main__":
    s = Solution()
    nums = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]
    print(s.longestIncreasingPath(nums))
