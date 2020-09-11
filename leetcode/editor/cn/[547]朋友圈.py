# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 
# 的朋友。所谓的朋友圈，是指所有朋友的集合。 
# 
#  给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你
# 必须输出所有学生中的已知的朋友圈总数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# 输出：2 
# 解释：已知学生 0 和学生 1 互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回 2 。
#  
# 
#  示例 2： 
# 
#  输入：
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# 输出：1
# 解释：已知学生 0 和学生 1 互为朋友，学生 1 和学生 2 互为朋友，所以学生 0 和学生 2 也是朋友，所以他们三个在一个朋友圈，返回 1 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 200 
#  M[i][i] == 1 
#  M[i][j] == M[j][i] 
#  
#  Related Topics 深度优先搜索 并查集 
#  👍 314 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、此题和岛屿类似，套用岛屿的解题思路，联通1及其周围的1即可
    """

    def findCircleNum(self, M: List[List[int]]) -> int:
        ans = 0
        w, h = len(M[0]), len(M)
        for i in range(0, h):
            for j in range(0, h):
                if M[i][j] == 1:
                    ans += 1
                    self._dfs(M, i, j, h, w)
        return ans

    def _dfs(self, M, i, j, h, w):
        if i < 0 or i >= h or j < 0 or j >= w or M[i][j] != 1:
            return
        M[i][j] = 0
        self._dfs(M, i - 1, j, h, w)
        self._dfs(M, i + 1, j, h, w)
        self._dfs(M, i, j - 1, h, w)
        self._dfs(M, i, j + 1, h, w)
        self._dfs(M, i - 1, j-1, h, w)
        self._dfs(M, i + 1, j+1, h, w)
        self._dfs(M, i + 1, j-1, h, w)
        self._dfs(M, i + 1, j - 1, h, w)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    M = [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]
    print(Solution().findCircleNum(M))
    M = [[1, 0, 0, 1],
         [0, 1, 1, 0],
         [0, 1, 1, 1],
         [1, 0, 1, 1]]
    print(Solution().findCircleNum(M))
