# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。 
# 
#  
# 
#  在杨辉三角中，每个数是它左上方和右上方的数的和。 
# 
#  示例: 
# 
#  输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ] 
#  Related Topics 数组 
#  👍 349 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        ans = [[1]]
        if numRows == 1:
            return ans

        self._create(2, numRows, ans)
        return ans

    def _create(self, index, numRows, ans):
        if index > numRows:
            return

        ans.append([])
        for i in range(0, index):
            ans[-1].append(self._getNum(ans[-2], i))
        self._create(index + 1, numRows, ans)

    def _getNum(self, array, col):
        num = 0
        if 0 <= col - 1 < len(array):
            num += array[col - 1]
        if 0 <= col < len(array):
            num += array[col]
        return num
# leetcode submit region end(Prohibit modification and deletion)
