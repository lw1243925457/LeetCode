# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。 
# 
#  说明：解集不能包含重复的子集。 
# 
#  示例: 
# 
#  输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ] 
#  Related Topics 位运算 数组 回溯算法 
#  👍 788 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        self._findSub(nums, [], ans, 0)
        return ans

    def _findSub(self, nums, path, ans, index):
        if len(nums) == 0:
            return
        for i in range(index, len(nums)):
            path.append(nums[i])
            ans.append(path.copy())
            self._findSub(nums, path, ans, i + 1)
            path.pop()
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    print(Solution().subsets([1, 2, 3]))
