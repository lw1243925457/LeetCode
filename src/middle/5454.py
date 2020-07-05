"""
5454. 统计全 1 子矩形 显示英文描述
通过的用户数666
尝试过的用户数1067
用户总通过次数670
用户总提交次数1559
题目难度Medium
给你一个只包含 0 和 1 的 rows * columns 矩阵 mat ，请你返回有多少个 子矩形 的元素全部都是 1 。



示例 1：

输入：mat = [[1,0,1],
            [1,1,0],
            [1,1,0]]
输出：13
解释：
有 6 个 1x1 的矩形。
有 2 个 1x2 的矩形。
有 3 个 2x1 的矩形。
有 1 个 2x2 的矩形。
有 1 个 3x1 的矩形。
矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13 。
示例 2：

输入：mat = [[0,1,1,0],
            [0,1,1,1],
            [1,1,1,0]]
输出：24
解释：
有 8 个 1x1 的子矩形。
有 5 个 1x2 的子矩形。
有 2 个 1x3 的子矩形。
有 4 个 2x1 的子矩形。
有 2 个 2x2 的子矩形。
有 2 个 3x1 的子矩形。
有 1 个 3x2 的子矩形。
矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24 。
示例 3：

输入：mat = [[1,1,1,1,1,1]]
输出：21
示例 4：

输入：mat = [[1,0,1],[0,1,0],[1,0,1]]
输出：5


提示：

1 <= rows <= 150
1 <= columns <= 150
0 <= mat[i][j] <= 1
"""
from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        amount = 0
        for i in range(0, len(mat)):
            for j in range(0, len(mat[i])):
                if mat[i][j] == 1:
                    amount += 1
                    amount += self.up(mat, i, j)
                    amount += self.left(mat, i, j)
                    amount += self.center(mat, i, j, 2, 2)
                # print(i, j, amount)
        print(amount)
        return amount

    def up(self, mat, i, j):
        amount = 0
        size = 1
        while i - size >= 0:
            if mat[i - size][j] == 1:
                amount += 1
                size += 1
            else:
                return amount
        return amount

    def left(self, mat, i, j):
        amount = 0
        size = 1
        while j - size >= 0:
            if mat[i][j - size] == 1:
                amount += 1
                size += 1
            else:
                return amount
        return amount

    def center(self, mat, i, j, hs, ws):
        if i - hs + 1 < 0 or j - ws + 1 < 0:
            return 0
        # print(i, j, cs, "center:", mat[i - cs + 1][j], mat[i][j - cs + 1], mat[i - cs + 1][j - cs + 1])
        if mat[i - hs + 1][j] == 1 and mat[i][j - ws + 1] == 1 and mat[i - hs + 1][j - ws + 1] == 1:
            return 1 + self.center(mat, i, j, hs + 1, ws) + self.center(mat, i, j, hs, ws + 1) + self.center(mat, i, j,
                                                                                                             hs + 1,
                                                                                                             ws + 1)
        return 0


if __name__ == "__main__":
    s = Solution()
    mat = [[1, 0, 1],
           [1, 1, 0],
           [1, 1, 0]]
    assert s.numSubmat(mat) == 13
    mat = [[0, 1, 1, 0],
           [0, 1, 1, 1],
           [1, 1, 1, 0]]
    assert s.numSubmat(mat) == 24
    mat = [[1, 1, 1, 1, 1, 1]]
    assert s.numSubmat(mat) == 21
    mat = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    assert s.numSubmat(mat) == 5
    mat = [[1, 0, 0, 1, 0, 1, 0, 1],
           [1, 0, 1, 1, 0, 1, 0, 0],
           [1, 1, 1, 0, 1, 0, 0, 1],
           [0, 0, 1, 1, 1, 1, 0, 0],
           [0, 0, 1, 1, 1, 1, 0, 1],
           [1, 1, 0, 1, 1, 1, 0, 0]]
    assert s.numSubmat(mat) == 82
