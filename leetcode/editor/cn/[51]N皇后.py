# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  
# 
#  上图为 8 皇后问题的一种解法。 
# 
#  给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。 
# 
#  每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
# 
#  
# 
#  示例： 
# 
#  输入：4
# 输出：[
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#  
# 
#  
# 
#  提示： 
# 
#  
#  皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。 
#  
#  Related Topics 回溯算法 
#  👍 529 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、递归回溯：枚举尝试，记录已放置行和对角线，时间复杂度O(N^N)
    """

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        grid = [["."] * n for _ in range(0, n)]
        self._dfs(ans, grid, 0, n)
        return ans

    def _dfs(self, ans, grid, row, rows):
        # print(row, rows, grid)
        if row >= rows:
            res = []
            for i in grid:
                res.append("".join(i))
            ans.append(res)
            return

        for col in range(0, rows):
            if not self._checkCol(col, row, grid) or not self._checkDiagonal(row, col, grid, rows):
                continue
            grid[row][col] = "Q"
            self._dfs(ans, grid, row + 1, rows)
            grid[row][col] = "."

    def _checkCol(self, col, row, grid):
        for i in range(row, -1, -1):
            if grid[i][col] == "Q":
                return False
        return True

    def _checkDiagonal(self, row, col, grid, cols):
        i, j = row, col
        while i - 1 >= 0 and j - 1 >= 0:
            if grid[i - 1][j - 1] == "Q":
                return False
            i -= 1
            j -= 1
        i, j = row, col
        while i - 1 >= 0 and j + 1 < cols:
            if grid[i - 1][j + 1] == "Q":
                return False
            i -= 1
            j += 1
        return True


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    res = Solution().solveNQueens(4)
    for i in res:
        for j in i:
            print(j)
        print("***********")
