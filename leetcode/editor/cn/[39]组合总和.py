# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
# 
#  candidates 中的数字可以无限制重复被选取。 
# 
#  说明： 
# 
#  
#  所有数字（包括 target）都是正整数。 
#  解集不能包含重复的组合。 
#  
# 
#  示例 1： 
# 
#  输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
#   [7],
#   [2,2,3]
# ]
#  
# 
#  示例 2： 
# 
#  输入：candidates = [2,3,5], target = 8,
# 所求解集为：
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= candidates.length <= 30 
#  1 <= candidates[i] <= 200 
#  candidate 中的每个元素都是独一无二的。 
#  1 <= target <= 500 
#  
#  Related Topics 数组 回溯算法 
#  👍 853 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self._dfs(candidates, 0, [], 0, ans, target)
        return ans

    def _dfs(self, candidates, start, path, amount, ans, target):
        if amount == target:
            ans.append(path.copy())
            return
        if amount > target:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            self._dfs(candidates, i, path, amount+candidates[i], ans, target)
            path.pop()
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    print(Solution().combinationSum([], 1))
    print(Solution().combinationSum([6, 7, 2, 3], 7))
    print(Solution().combinationSum([5, 2, 3], 8))
