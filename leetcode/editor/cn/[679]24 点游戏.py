# 你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。 
# 
#  示例 1: 
# 
#  输入: [4, 1, 8, 7]
# 输出: True
# 解释: (8-4) * (7-1) = 24
#  
# 
#  示例 2: 
# 
#  输入: [1, 2, 1, 2]
# 输出: False
#  
# 
#  注意: 
# 
#  
#  除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。 
#  每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1 是不允
# 许的。 
#  你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。 
#  
#  Related Topics 深度优先搜索 
#  👍 161 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """解题思路：
    一、四个数加括号单独枚举有点复杂，可以简化成 （a * b) * (c * d)
        即两两数相操作后结果在操作
    """

    def judgePoint24(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            tempi = nums.copy()
            tempi.remove(nums[i])
            for j in range(0, len(nums)):
                if i == j:
                    continue
                tempj = tempi.copy()
                tempj.remove(nums[j])
                print(nums[i], nums[j], tempj)
                for k in range(0, 4):
                    num5 = self._operation(nums[i], nums[j], k)
                    if num5 is None:
                        continue
                    for m in range(0, 4):
                        num6 = self._operation(tempj[0], tempj[1], m)
                        if num6 is None:
                            continue
                        for n in range(0, 4):
                            if self._operation(num5, num6, n) == 24 or self._operation(num6, num5, n) == 24:
                                print(nums[i], nums[j], k, tempj[0], tempj[1], m, num5, num6, n)
                                return True
                    for m in range(0, 4):
                        num6 = self._operation(tempj[1], tempj[0], m)
                        if num6 is None:
                            continue
                        for n in range(0, 4):
                            if self._operation(num5, num6, n) == 24 or self._operation(num6, num5, n) == 24:
                                print(nums[i], nums[j], k, tempj[0], tempj[1], m, num5, num6, n)
                                return True
        return False

    def _operation(self, param1, param2, k):
        if k == 0:
            return param1 + param2
        if k == 1:
            return param1 - param2
        if k == 2:
            return param1 * param2
        if k == 3:
            if param2 == 0:
                return None
            return param2 / param2


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    assert not solution.judgePoint24([1, 2, 1, 2])
    assert not solution.judgePoint24([1, 5, 9, 1])
    assert solution.judgePoint24([1, 8, 2, 5])
    assert solution.judgePoint24([3, 9, 7, 7])
