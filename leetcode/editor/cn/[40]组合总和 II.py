# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
# 
#  candidates 中的每个数字在每个组合中只能使用一次。 
# 
#  说明： 
# 
#  
#  所有数字（包括目标数）都是正整数。 
#  解集不能包含重复的组合。 
#  
# 
#  示例 1: 
# 
#  输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
#  
# 
#  示例 2: 
# 
#  输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ] 
#  Related Topics 数组 回溯算法 
#  👍 357 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self._dfs(ans, target, 0, [], 0, candidates)
        return ans

    def _dfs(self, ans, target, amount, path, start, candidates):
        if amount == target:
            ans.append(path.copy())
            return
        if amount > target:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            self._dfs(ans, target, amount + candidates[i], path, i + 1, candidates)
            path.pop()


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    print(Solution().combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
    print(Solution().combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
