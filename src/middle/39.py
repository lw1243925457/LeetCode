"""
39. 组合总和
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]


提示：

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500


解题思路：
递归回溯：结束条件，大于目标
学到的关键点：
1.排序加其实序列，排除重复答案
2.回溯：入栈--递归--出栈
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        ans = []

        def find(added: int, nums: List[int], start, end):
            if added == target:
                ans.append(nums.copy())

            for i in range(start, end):
                num = candidates[i]
                if added + num > target:
                    break
                else:
                    nums.append(num)
                    find(added + num, nums, i, end)
                    nums.pop()

        candidates.sort()
        find(0, [], 0, len(candidates))
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum(candidates=[2, 3, 6, 7], target=7))
    print(s.combinationSum(candidates=[2, 3, 5], target=8))
