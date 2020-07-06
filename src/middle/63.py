"""
63. 不同路径 II
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？



网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
通过次数67,463提交次数198,138
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = []
        for i in range(0, len(obstacleGrid)):
            dp.append([])
            for j in range(0, len(obstacleGrid[i])):
                dp[i].append(0)
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        else:
            dp[0][0] = 0

        for i in range(0, len(obstacleGrid)):
            for j in range(0, len(obstacleGrid[i])):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 0:
                    if i - 1 >= 0:
                        dp[i][j] += dp[i - 1][j]
                    if j - 1 >= 0:
                        dp[i][j] += dp[i][j - 1]
                else:
                    continue

        print(dp[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1])
        return dp[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]


if __name__ == "__main__":
    s = Solution()
    map = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert s.uniquePathsWithObstacles(map) == 2
    map = [[0]]
    assert s.uniquePathsWithObstacles(map) == 1
