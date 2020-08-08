"""
40. 组合总和 II
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
通过次数73,426提交次数117,664


解题思路：
递归回溯即可
避免重复的那个思路我是想到了的，但没有正确的改写使用与递归，教训
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def find(index: int, amount: int, group: List[int]):
            print(candidates, index, group, amount)
            if amount == target:
                ans.append(group.copy())
                return

            for i in range(index, n):
                if amount + candidates[i] > target:
                    break
                if i > index and candidates[i - 1] == candidates[i]:
                    continue
                group.append(candidates[i])
                find(i+1, amount + candidates[i], group)
                group.pop()

        ans = []
        n = len(candidates)
        if n == 0:
            return []
        candidates.sort()
        find(0, 0, [])
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
