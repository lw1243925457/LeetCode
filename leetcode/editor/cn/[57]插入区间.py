# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。 
# 
#  在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。 
# 
#  
# 
#  示例 1： 
# 
#  输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
#  
# 
#  示例 2： 
# 
#  输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
#  
# 
#  
# 
#  注意：输入类型已在 2019 年 4 月 15 日更改。请重置为默认代码定义以获取新的方法签名。 
#  Related Topics 排序 数组 
#  👍 293 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    1.[0,1] -- [2,3]
    2.[0,2] -- [2,3]
    3.[1,4] -- [2,3]
    4.[3,4] -- [2,3]
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals or len(intervals) == 0:
            return [newInterval]
        if not intervals or len(newInterval) == 0:
            return intervals

        ans = []
        added = False
        for interval in intervals:
            if added:
                ans.append(interval)
                continue
            if interval[1] < newInterval[0]:
                ans.append(interval)
            elif interval[0] > newInterval[1]:
                if not added:
                    ans.append(newInterval)
                    added = True
                ans.append(interval)
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        if not added:
            ans = ans + [newInterval]
        # print(ans)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    assert Solution().insert(intervals = [[1,3],[6,9]], newInterval = [2,5]) == [[1,5],[6,9]]
    assert Solution().insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]) == [[1,2],[3,10],[12,16]]
    assert Solution().insert([], [2,3]) == [[2, 3]]
    assert Solution().insert([[2, 3]], []) == [[2, 3]]
    assert Solution().insert([[1, 5]], [2, 3]) == [[1, 5]]
    assert Solution().insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
    assert Solution().insert([[2,5],[6,7],[8,9]], [0, 1]) == [[0,1],[2,5],[6,7],[8,9]]
