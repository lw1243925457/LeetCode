# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。 
# 
#  说明： 
# 
#  
#  所有数字都是正整数。 
#  解集不能包含重复的组合。 
#  
# 
#  示例 1: 
# 
#  输入: k = 3, n = 7
# 输出: [[1,2,4]]
#  
# 
#  示例 2: 
# 
#  输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
#  
#  Related Topics 数组 回溯算法 
#  👍 170 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        self._dfs(1, 0, [], k, n, ans)
        return ans

    def _dfs(self, start, amount, path, k, n, ans):
        if len(path) == k:
            if amount == n:
                ans.append(path.copy())
            return
        for i in range(start, 10):
            path.append(i)
            self._dfs(i + 1, amount + i, path, k, n, ans)
            path.pop()


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    print(Solution().combinationSum3(k=3, n=7))
    print(Solution().combinationSum3(k=3, n=9))
    print(Solution().combinationSum3(k=2, n=18))
