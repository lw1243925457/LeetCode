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


解题思路：
参考网上的题解，先使用连续的1原理统计横向，再使用&叠加统计纵向
难搞，思想很奇妙，自己很难想到
"""
from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        amount = 0

        for i in range(0, len(mat)):
            for j in range(i, len(mat)):
                count = 0
                for k in range(0, len(mat[i])):
                    if mat[j][k] == 1:
                        count = count + 1
                        amount = amount + count
                    else:
                        count = 0

            for j in range(len(mat) - 1, i-1, -1):
                for k in range(0, len(mat[j])):
                    mat[j][k] = mat[j][k] & mat[j-1][k]
        return amount


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
