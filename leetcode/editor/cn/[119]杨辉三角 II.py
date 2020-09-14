# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。 
# 
#  
# 
#  在杨辉三角中，每个数是它左上方和右上方的数的和。 
# 
#  示例: 
# 
#  输入: 3
# 输出: [1,3,3,1]
#  
# 
#  进阶： 
# 
#  你可以优化你的算法到 O(k) 空间复杂度吗？ 
#  Related Topics 数组 
#  👍 178 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        return self._create([1], 2, rowIndex + 1)

    def _create(self, array, row, maxRow):
        if row > maxRow:
            return array

        nextArray = []
        for i in range(0, row):
            nextArray.append(self._getNumber(array, i))
        return self._create(nextArray, row + 1, maxRow)

    def _getNumber(self, array, col):
        num = 0
        if 0 <= col - 1 < len(array):
            num += array[col - 1]
        if 0 <= col < len(array):
            num += array[col]
        return num
# leetcode submit region end(Prohibit modification and deletion)
