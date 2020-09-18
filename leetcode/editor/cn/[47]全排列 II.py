# 给定一个可包含重复数字的序列，返回所有不重复的全排列。 
# 
#  示例: 
# 
#  输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ] 
#  Related Topics 回溯算法 
#  👍 401 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        self._permutation(nums, ans, [])
        return ans

    def _permutation(self, nums, ans, path):
        if not nums:
            ans.append(path.copy())
            return
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self._permutation(nums[:i] + nums[i+1:], ans, path)
            path.pop()
# leetcode submit region end(Prohibit modification and deletion)
