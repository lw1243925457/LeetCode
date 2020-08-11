"""
130. 被围绕的区域
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。


解题思路:
有点下围棋的感觉。。。
参考官方题解的解法
"""
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) < 3:
            return

        n, m = len(board), len(board[0])

        def dfs(x: int, y:int):
            if x < 0 or x >= n or y < 0 or y >= m or board[x][y] != 'O':
                return
            board[x][y] = 'A'
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        for i in range(0, n):
            dfs(i, 0)
            dfs(i, m-1)

        for i in range(0, m):
            dfs(0, i)
            dfs(n-1, i)

        for i in range(0, n):
            for j in range(0, m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'
