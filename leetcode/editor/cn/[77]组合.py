# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。 
# 
#  示例: 
# 
#  输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
#  Related Topics 回溯算法 
#  👍 342 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self._dfs(1, n, ans, [], k)
        return ans

    def _dfs(self, start, n, ans, path, k):
        if len(path) == k:
            ans.append(path.copy())
            return
        for i in range(start, n+1):
            path.append(i)
            self._dfs(i+1, n, ans, path, k)
            path.pop()

# leetcode submit region end(Prohibit modification and deletion)
