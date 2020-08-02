"""
37. 解数独
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。



一个数独。



答案被标成红色。

Note:

给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。
通过次数35,693提交次数57,325


解题思路：
1.暴力解：逐个将空格填上，判断是否符合，不符合返回重新填写，一个空格9种填写发，N个空格，判断是O(81)，好像可以，毕竟数量固定的，不大
2.填写优化：首先遍历一次，缓存已填写的数字，后面填写的从未出现的数字中获取
"""
from typing import List


class Solution:
    def __init__(self):
        self.rows = [{} for i in range(0, 9)]
        self.cols = [{} for i in range(0, 9)]
        self.boxs = [{} for i in range(0, 9)]

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    continue
                boxIndex = (i // 3) * 3 + j // 3
                num = int(board[i][j])
                self.rows[i][num] = 1
                self.cols[j][num] = 1
                self.boxs[boxIndex][num] = 1

        print(self.write(board, 0, 0))

    def write(self, board, i, j):
        if i == 8 and j == 8 and board[i][j] != ".":
            return True

        if board[i][j] == ".":
            for num in range(1, 10):
                boxIndex = (i // 3) * 3 + j // 3
                if self.canPlace(i, j, boxIndex, num):
                    self.rows[i][num] = 1
                    self.cols[j][num] = 1
                    self.boxs[boxIndex][num] = 1
                    board[i][j] = str(num)
                    nexti, nextj = self.nextPlace(i, j)
                    print(i, j, "write:", num)
                    if i == 1 and j == 6:
                        print(self.rows[i])
                        print(self.cols[j])
                        print(self.boxs[boxIndex])
                    if not self.write(board, nexti, nextj):
                        self.rows[i][num] = 0
                        self.cols[j][num] = 0
                        self.boxs[boxIndex][num] = 0
                        board[i][j] = "."
                        print(i, j, num, "write failed, back")
                    else:
                        print(i, j, num, "write successful")
                        return True
        else:
            num = int(board[i][j])
            boxIndex = (i // 3) * 3 + j // 3
            self.rows[i][num] = 1
            self.cols[j][num] = 1
            self.boxs[boxIndex][num] = 1
            print(i, j, "fill next .:", num)
            nexti, nextj = self.nextPlace(i, j)
            self.write(board, nexti, nextj)

        return False

    def canPlace(self, i, j, boxIndex, num):
        if self.rows[i].get(num, 0) == 0 and self.cols[j].get(num, 0) == 0 and self.boxs[boxIndex].get(num, 0) == 0:
            return True
        return False

    def nextPlace(self, i, j):
        if j == 8:
            return i+1, 0
        return i, j+1


if __name__ == "__main__":
    s = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s.solveSudoku(board)
    for item in board:
        print(item)
